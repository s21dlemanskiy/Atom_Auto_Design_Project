from fastapi import APIRouter
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DAO.MangoDB import MangoDB
from ..MlModels.Synonyms import WordnetAPI
from ..MlModels.NLPTextProcessor import DepparseTextProcessor
from typing import List, Optional, Dict, Set

router = APIRouter(prefix="/search", tags=["search"], responses={400: {"description": "bed params"}})

@router.post("/find_adj")
def search_by_words(words: List[str],
                    marks: Optional[List[str]]=None,
                    models: Optional[List[str]]=None,
                    body_types: Optional[List[str]]=None):
    result = {}
    with MangoDB() as client:
        adjective_mg = AdjectiveManager(client)
        map_texts_adjectives = adjective_mg.get_adjectives_by_nouns(words, marks=marks, models=models, bodys=body_types)
        for text_id in map_texts_adjectives.keys():
            result[text_id] = {}
            result[text_id]["adjectives"] = list(map(lambda x: x.to_dict(id_to_string=True),
                                                                   map_texts_adjectives[text_id]["adjectives"]))
            result[text_id]["text"] = map_texts_adjectives[text_id]["text"].to_dict(ignore_id=True)
            if "source" in result[text_id]["text"]["other_data"]:
                result[text_id]["text"]["source"] = result[text_id]["text"]["other_data"]["source"]
            if "text_sentiment" in result[text_id]["text"]["other_data"]:
                result[text_id]["text"]["text_sentiment"] = result[text_id]["text"]["other_data"]["text_sentiment"]
            del result[text_id]["text"]["other_data"]
    return result


@router.get("/get_cars")
def get_all_marks_models_bodys() -> Dict[str, Dict[str, Set[str]]]:
    result = {}
    with MangoDB() as client:
        client.get_collection("texts")
        query = {"filter":{}, "projection": ["mark", "model", "body_type"]}
        result_set = client.find(**query)
        for row in result_set:
            if row["mark"] not in result.keys():
                result[row["mark"]] = dict()
            mark_description = result[row["mark"]]
            if row["model"] not in mark_description.keys():
                mark_description[row["model"]] = set()
            model_description = mark_description[row["model"]]
            model_description.add(row["body_type"])
    return result


@router.get("/get_sources")
def get_all_sources() -> Set[str]:
    result = None
    with MangoDB() as client:
        client.get_collection("texts")
        query = {"filter": {"other_data.source": {"$exists": True}}, "projection": ["other_data.source"]}
        result_set = client.find(**query)
        result = set(list(map(lambda row: row["other_data"].get("source", None), result_set)))
    return result


@router.post("/synonims")
def get_synonyms(word: str) -> List[str]:
    word_lemma = DepparseTextProcessor.get_lemma(word)
    wiki_wordnet = WordnetAPI()
    synonyms = wiki_wordnet.get_synonyms(word_lemma)
    if (word.lower() not in synonyms):
        synonyms.append(word.lower())
    return synonyms