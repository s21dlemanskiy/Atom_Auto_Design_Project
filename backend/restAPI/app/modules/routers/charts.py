from fastapi import APIRouter, Body
from ..DAO.GraphManager import GraphManager
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DAO.MangoDB import MangoDB
from typing import List, Optional, Dict, Set, Tuple

from ..DataModels import Adjective
from ..DataModels.Text import Text

router = APIRouter(prefix="/charts", tags=["charts"], responses={400: {"description": "bed params"}})

@router.post("/sentiment_chart")
def get_sentiment_chart_data(marks: List[str] = Body(default=None, examples=[["Kia"]]),
                             models: List[str] = Body(default=None, examples=[["K5"]]),
                             body_types: List[str] = Body(default=None, examples=[["SEDAN"]]),
                             sources: List[str] = Body(default=None, examples=[["avito"]]),
                             skip_bad_sentiments: bool = True) -> List[Tuple[str, int]]:
    ignore_values = ["SPEECH", "SKIP"]
    data = []
    with MangoDB() as client:
        graph_manager = GraphManager(client)
        data = graph_manager.sentiment_chart(marks=marks,
                        models=models,
                        body_types=body_types,
                        sources=sources)
    if skip_bad_sentiments:
        data = list(filter(lambda x: x[0] not in ignore_values, data))
    return data


@router.post("/pros_chart")
def get_pros_chart_data(marks: List[str] = Body(default=None, examples=[["Kia"]]),
                        models: List[str] = Body(default=None, examples=[["K5"]]),
                        body_types: List[str] = Body(default=None, examples=[["SEDAN"]]),
                        sentiments: List[str] = Body(default=None, examples=[["POSITIVE"]])) -> List[Tuple[str, int]]:
    data = []
    with MangoDB() as client:
        graph_manager = GraphManager(client)
        data = graph_manager.get_pros(marks=marks,
                                      models=models,
                                      body_types=body_types,
                                      sentiments=sentiments)
    data.sort(key=lambda x: x[1])
    return data


@router.post("/cons_chart")
def get_cons_chart_data(marks: List[str] = Body(default=None, examples=[["Kia"]]),
                        models: List[str] = Body(default=None, examples=[["K5"]]),
                        body_types: List[str] = Body(default=None, examples=[["SEDAN"]]),
                        sentiments: List[str] = Body(default=None, examples=[["POSITIVE"]])) -> List[Tuple[str, int]]:
    data = []
    with MangoDB() as client:
        graph_manager = GraphManager(client)
        data = graph_manager.get_cons(marks=marks,
                                      models=models,
                                      body_types=body_types,
                                      sentiments=sentiments)
    data.sort(key=lambda x: x[1])
    return data


@router.post("/avg_personal_score_chart")
def get_personal_score_chart_data(marks: List[str] = Body(default=None, examples=[["Kia"]]),
                                  models: List[str] = Body(default=None, examples=[["K5"]]),
                                  body_types: List[str] = Body(default=None, examples=[["SEDAN"]]),
                                  sentiments: List[str] = Body(default=None, examples=[["POSITIVE"]]))\
        -> List[Tuple[str, float]]:
    data = []
    with MangoDB() as client:
        graph_manager = GraphManager(client)
        data = graph_manager.avg_persanal_score_chart(marks=marks,
                                      models=models,
                                      body_types=body_types,
                                      sentiments=sentiments)
    data.sort(key=lambda x: x[1])
    return data


# @router.post("/avg_personal_score_chart")
# def get_sentiment_chart_data(marks: List[str] = None,
#                              models: List[str] = None,
#                              body_types: List[str] = None,
#                              sentiments: List[str] = None) -> List[Tuple[str, int]]:
#     data = []
#     with MangoDB() as client:
#         graph_manager = GraphManager(client)
#         data = graph_manager.avg_persanal_score_chart(marks=marks,
#                                       models=models,
#                                       body_types=body_types,
#                                       sentiments=sentiments)
#     return data


@router.post("/word_cloud")
def search_by_words(words: List[str] = Body(examples=[["машина"]]),
                    marks: List[str] = Body(default=None, examples=[["Kia"]]),
                    models: List[str] = Body(default=None, examples=[["K5"]]),
                    body_types: List[str] = Body(default=None, examples=[["SEDAN"]]),
                    sentiments: List[str] = Body(default=None, examples=[["POSITIVE"]]),
                    sources: List[str] = Body(default=None, examples=[["avito"]])) -> List[Tuple[str, int]]:
    all_adjectives = []
    with MangoDB() as client:
        adjective_mg = AdjectiveManager(client)
        map_texts_adjectives = adjective_mg.get_adjectives_by_nouns(words, marks=marks, models=models, bodys=body_types)
        for text_id in map_texts_adjectives.keys():
            adjectives: List[Adjective] = map_texts_adjectives[text_id]["adjectives"]
            text: Text = map_texts_adjectives[text_id]["text"]
            if sources is not None:
                if 'source' not in text.other_data.keys():
                    continue
                if text.other_data["source"] not in sources:
                    continue
            if sentiments is not None:
                if "text_sentiment" not in text.other_data:
                    continue
                if "label" not in text.other_data["text_sentiment"]:
                    continue
                if text.other_data["text_sentiment"]["label"] not in sentiments:
                    continue
            all_adjectives += list(map(lambda x: x.adjective.lemma, adjectives))
    return [(adj, all_adjectives.count(adj)) for adj in set(all_adjectives)]

