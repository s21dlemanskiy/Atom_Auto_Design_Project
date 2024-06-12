from fastapi import APIRouter
from ..DAO.MangoDB import MangoDB
from typing import List, Optional, Dict, Set, Tuple


router = APIRouter(prefix="/vars", tags=["vars"], responses={400: {"description": "bed params"}})


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

@router.get("/get_sentiments")
def get_all_sources(skip_bad_sentiments: bool = True) -> Set[str]:
    ignore_values = ["SPEECH", "SKIP"]
    result = None
    with MangoDB() as client:
        client.get_collection("texts")
        query = {
            "filter": {"other_data.text_sentiment.label": {"$exists": True, "$ne": "null"}},
            "projection": ["other_data.text_sentiment.label"]
        }
        result_set = client.find(**query)
        result = set(list(map(lambda row: row["other_data"].get("text_sentiment").get("label"), result_set)))
    if skip_bad_sentiments:
        result = set(filter(lambda x: x not in ignore_values, result))
    return result


@router.get("/get_key_words")
def get_all_sources() -> List[Tuple[str, int]]:
    result = None
    with MangoDB() as client:
        client.get_collection("adjectives")
        query = {
            "filter": {"key_word.lemma": {"$exists": True, "$ne": "null"}},
            "projection": ["key_word.lemma"]
        }
        result_set = client.find(**query)
        lemmas = list(map(lambda row: row["key_word"].get("lemma"), result_set))
        result = [(lemma, lemmas.count(lemma)) for lemma in set(lemmas)]
    result.sort(key=lambda x: x[1])
    return result
