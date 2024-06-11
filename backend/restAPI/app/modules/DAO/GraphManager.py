from .MangoDB import MangoDB
from ..DataModels.Text import Text
from typing import Dict, List, Any, Optional, Union, Tuple
from logging import error, info, warning

class GraphManager:
    plus_selector = "Плюсы, отмеченные автором"
    minus_selector = "Минусы, отмеченные автором"

    def __init__(self, client: MangoDB):
        self._client = client

    def get_pros_cons(self, selector: str,
                      marks: List[str] = None,
                      models: List[str] = None,
                      body_types: List[str] = None,
                      sentiments: List[str] = None) -> List[Tuple[str, int]]:
        self._client.get_collection("texts")
        query = {
                **({"mark": {"$in": marks}} if marks is not None else {}),
                **({"model": {"$in": models}} if models is not None else {}),
                **({"body_type": {"$in": body_types}} if body_types is not None else {}),
                **({"other_data.text_sentiment.label": {"$in": sentiments}} if sentiments is not None else {}),
                f"other_data.{selector}": {"$exists": True, "$ne": "null"}
        }
        info(f"Query to get pros or cons: {query}")
        result_set = self._client.find(query, [f"other_data.{selector}"])
        words = sum(map(lambda x: list(x["other_data"][selector].strip().split(", ")), result_set), [])
        words_counted = [(i,  words.count(i)) for i in set(words)]
        return words_counted

    def get_pros(self, *args, **kwargs):
        return self.get_pros_cons(self.plus_selector, *args, **kwargs)

    def get_cons(self, *args, **kwargs):
        return self.get_pros_cons(self.minus_selector, *args, **kwargs)

    def sentiment_chart(self, marks: List[str] = None,
                        models: List[str] = None,
                        body_types: List[str] = None,
                        sources: List[str] = None) -> List[Tuple[str, int]]:
        self._client.get_collection("texts")
        query = {
            **({"mark": {"$in": marks}} if marks is not None else {}),
            **({"model": {"$in": models}} if models is not None else {}),
            **({"body_type": {"$in": body_types}} if body_types is not None else {}),
            **({"other_data.source": {"$in": sources}} if sources is not None else {}),
            "other_data.text_sentiment.label": {"$exists": True, "$ne": "null"}
        }
        result_set = self._client.find(query, ["other_data.text_sentiment.label"])
        texts_sentiments = sum(map(lambda x: [x["other_data"]["text_sentiment"]["label"]], result_set), [])
        sentiments_counted = [(i, texts_sentiments.count(i)) for i in set(texts_sentiments)]
        sentiments_counted = list(filter(lambda x: x[0] not in ['SPEECH', 'SKIP'], sentiments_counted))
        return sentiments_counted

    def avg_persanal_score_chart(self, marks: List[str] = None,
                        models: List[str] = None,
                        body_types: List[str] = None,
                        sentiments: List[str] = None) -> List[Tuple[str, int]]:
        self._client.get_collection("texts")
        selector = 'оценка автора'
        query = {
            **({"mark": {"$in": marks}} if marks is not None else {}),
            **({"model": {"$in": models}} if models is not None else {}),
            **({"body_type": {"$in": body_types}} if body_types is not None else {}),
            **({"other_data.text_sentiment.label": {"$in": sentiments}} if sentiments is not None else {}),
            f"other_data.{selector}": {"$exists": True, "$ne": "null"}
        }
        # print(query)
        all_scores = {}
        for persanal_scores in map(lambda x: x["other_data"][selector],
                                   list(self._client.find(query, [f"other_data.{selector}"]))):
            for i in (persanal_scores.keys() - all_scores.keys()):
                all_scores[i] = []
            for i in persanal_scores:
                try:
                    score = int(persanal_scores[i])
                    all_scores[i] += [score]
                except ValueError:
                    print(persanal_scores[i])
                    continue
        avg_scores = []
        for i in all_scores:
            avg_scores += [(i, sum(all_scores[i]) / len(all_scores[i]))]
        return avg_scores