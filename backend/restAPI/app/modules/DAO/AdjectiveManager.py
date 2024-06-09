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
        adj_skiped_count = 0
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
            if marks is not None and text.mark not in marks:
                adj_skiped_count += 1
                continue
            if models is not None and text.model not in models:
                adj_skiped_count += 1
                continue
            if bodys is not None and text.body not in bodys:
                adj_skiped_count += 1
                continue
            result[str(text_id)] = {"adjectives": [adj], "text": text}
        info(f"Skiped {adj_skiped_count} adjective, in fact of discrepancy with input params (mark, model, body))")
        return result
