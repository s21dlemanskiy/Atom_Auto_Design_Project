from typing import Union, List, Dict, Any, Optional
from logging import error, info

from .MangoDB import MangoDB
from ..DataModels.Text import Text


class TextManager:
    def __init__(self, client: MangoDB):
        self._client = client

    def save_texts(self, texts: Union[List[Text], Text]) -> List[Any]:
        self._client.get_collection("texts")
        if isinstance(texts, list):
            texts = list(map(lambda text: text.to_dict(ignore_id=True), texts))
            result = self._client.insert_many(texts)
            info(f"Insert texts with ids: {result.inserted_ids}")
            return result.inserted_ids
        if isinstance(texts, Text):
            text = texts.to_dict(ignore_id=True)
            result = self._client.insert_one(text)
            info(f"Insert text with id: {result.inserted_id}")
            return [result.inserted_id]
        error(f"Strange object type: {type(texts)}")
        raise ValueError()

    def get_all_texts(self) -> List[Dict[str, Any]]:
        self._client.get_collection("texts")
        return list(self._client.find())

    def set_sentiment(self, text_id, sentiment: str):
        self._client.get_collection("texts")
        newvalues = {"$set": {"other_data.text_sentiment": sentiment}}
        self._client.update_one({"_id": text_id}, newvalues)


