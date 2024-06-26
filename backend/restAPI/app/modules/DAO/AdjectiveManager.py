from .MangoDB import MangoDB
from ..DataModels.Text import Text
from ..DataModels.Adjective import Adjective
from typing import Dict, List, Any, Optional, Union
from logging import error, info, warning


class AdjectiveManager:
    def __init__(self, client: MangoDB):
        self._client = client

    def add_adjectives(self, adjectives: List[Dict[str, Any]]):
        if len(adjectives) == 0:
            return []
        self._client.get_collection("adjectives")
        result = self._client.insert_many(adjectives)
        info(f"Insert adjectives count:{len(result.inserted_ids)}")
        return result.inserted_ids

    def get_adjectives_by_noun(self, noun_lemma: str) -> Dict[str, Dict[str, Union[List[Adjective], Text]]]:
        result = {}
        self._client.get_collection("adjectives")
        result_set = self._client.find({"key_word.lemma": noun_lemma.lower()})
        self._client.get_collection("texts")
        for adj in result_set:
            adj: Adjective = Adjective.from_dict(adj)
            text_id = adj.key_word.text_id
            if str(text_id) in result.keys():
                result[str(text_id)]["adjectives"].append(adj)
                continue
            text: Optional[Dict[Any]] = self._client.find_one({"_id": text_id})
            if text is None:
                info(f"No text with id {text_id}. Adjectives from this text skiped")
                continue
            text: Text = Text.from_dict(text)
            result[str(text_id)] = {"adjectives": [adj], "text": text}
        return result

    def get_adjectives_by_nouns(self, noun_lemmas: List[str],
                                marks: List[str]=None,
                                models: List[str]=None,
                                bodys: List[str]=None) -> Dict[str, Dict[str, Union[List[Adjective], Text]]]:
        result = {}
        self._client.get_collection("adjectives")
        noun_lemmas = list(map(lambda x: x.lower(), noun_lemmas))
        query = {"key_word.lemma": {"$in": noun_lemmas}}
        result_set = self._client.find(query)
        self._client.get_collection("texts")
        text_ids = []
        for adj in result_set:
            adj: Adjective = Adjective.from_dict(adj)
            text_id = adj.key_word.text_id
            if str(text_id) in result.keys():
                result[str(text_id)]["adjectives"].append(adj)
                continue
            result[str(text_id)] = {"adjectives": [adj]}
            text_ids.append(text_id)
        query = {
            "_id": {"$in": text_ids},
            **({"mark": {"$in": marks}} if marks is not None else {}),
            **({"model": {"$in": models}} if models is not None else {}),
            **({"body_type": {"$in": bodys}} if bodys is not None else {}),
            "other_data.text_sentiment.label": {"$exists": True, "$ne": "null"},
            "other_data.source": {"$exists": True, "$ne": "null"}
        }
        texts: List[Dict[Any]] = self._client.find(query)
        text_ids = set(text_ids)
        text_ids2 = set()
        for text in texts:
            text: Text = Text.from_dict(text)
            result[str(text.text_id)]["text"] = text
            text_ids2.add(text.text_id)
        text_id_without_text = (text_ids - text_ids2)
        for id in text_id_without_text:
            del result[str(id)]
            warning(f"No text with id {id}. Adjectives from this text skiped")
        return result
