from fastapi import APIRouter, Body, Query
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DAO.MangoDB import MangoDB
from ..MlModels.Synonyms import WordnetAPI
from ..MlModels.NLPTextProcessor import DepparseTextProcessor
from typing import List, Optional, Dict, Set

router = APIRouter(prefix="/search", tags=["search"], responses={400: {"description": "bed params"}})



@router.post("/find_adj")
def search_by_words(words: List[str] = Body(examples=[["машина"]]),
                    marks: Optional[List[str]] = Body(default=None, examples=[["Kia"]]),
                    models: Optional[List[str]] = Body(default=None, examples=[["K5"]]),
                    body_types: Optional[List[str]] = Body(default=None, examples=[["SEDAN"]])):
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


@router.post("/synonims")
def get_synonyms(word: str = Query(examples=["машина"])) -> List[str]:
    word_lemma = DepparseTextProcessor.get_lemma(word)
    wiki_wordnet = WordnetAPI()
    synonyms = wiki_wordnet.get_synonyms(word_lemma)
    if (word.lower() not in synonyms):
        synonyms.append(word.lower())
    return synonyms