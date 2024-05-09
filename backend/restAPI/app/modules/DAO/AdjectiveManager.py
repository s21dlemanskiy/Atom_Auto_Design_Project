from .MangoDB import MangoDB
from ..DataModels.Text import Text
from typing import Dict, List, Any, Optional
from logging import error, info, warning


class AdjectiveManager:
    def __init__(self, client: MangoDB):
        self._client = client

    def add_adjectives(self, adjectives: List[Dict[str, Any]]):
        self._client.get_collection("adjectives")
        result = self._client.insert_many(adjectives)
        info(f"Insert adjectives count:{len(result.inserted_ids)}")
        return result.inserted_ids

    def get_adjectives_by_noun(self, noun_lemma: str) -> List[Dict[str, Any]]:
        result = []
        self._client.get_collection("adjectives")
        result_set = self._client.find({"key_word.lemma": noun_lemma.lower()})
        self._client.get_collection("texts")
        for adj in result_set:
            if "key_word" not in adj or "text_id" not in adj["key_word"]:
                warning(f"Strange adjective with no 'key_word.text_id': {adj}")
                continue
            text_id = adj["key_word"]["text_id"]
            text: Optional[Dict[Any]] = self._client.find_one({"_id": text_id})
            if text is None:
                info(f"No text with id {text_id}. Adjectives from this text skiped")
                continue
            del adj["key_word"]["text_id"]
            adj["text"] = text
            result.append(adj)
        return result

    def get_adjectives_by_nouns(self, noun_lemmas: List[str]) -> List[Dict[str, Any]]:
        result = []
        self._client.get_collection("adjectives")
        noun_lemmas = list(map(lambda x: x.lower(), noun_lemmas))
        result_set = self._client.find({"key_word.lemma": {"$in": noun_lemmas}})
        self._client.get_collection("texts")
        for adj in result_set:
            if "key_word" not in adj or "text_id" not in adj["key_word"]:
                warning(f"Strange adjective with no 'key_word.text_id': {adj}")
                continue
            text_id = adj["key_word"]["text_id"]
            text: Optional[Dict[Any]] = self._client.find_one({"_id": text_id})
            if text is None:
                info(f"No text with id {text_id}. Adjectives from this text skiped")
                continue
            del adj["key_word"]["text_id"]
            adj["text"] = text
            result.append(adj)
        return result
