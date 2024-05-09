from typing import Dict, Optional, Any, Type
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self
from copy import deepcopy
from pydantic import BaseModel

class Word(BaseModel):
    deprel: str
    word: str
    lemma: str
    start_char: int
    end_char: int

    @classmethod
    def from_dict(cls: Type[Self], data: Dict, *args, copy=False, **kwargs) -> Self:
        requred_keys = {"deprel", "word", "lemma", "start_char", "end_char"}
        if copy:
            data = deepcopy(data)
        if len(requred_keys.difference(data.keys())) > 0:
            raise ValueError(f"'{requred_keys.difference(data.keys())}'must be in input data dict")
        deprel = data.pop("deprel")
        word = data.pop("word")
        lemma = data.pop("lemma")
        start_char = int(data.pop("start_char"))
        end_char = int(data.pop("end_char"))
        return cls(deprel=deprel,
                   word=word,
                   lemma=lemma,
                   start_char=start_char,
                   end_char=end_char,
                   copy=copy
                   *args,
                   **kwargs)

    def to_dict(self):
        return {"deprel": self.deprel,
                "word": self.word,
                "lemma": self.lemma,
                "start_char": self.start_char,
                "end_char": self.end_char}

    def __str__(self) -> str:
        return self.word

    def __repr__(self) -> str:
        return str(self)

class KeyWord(Word):
    text_id: Any

    @classmethod
    def from_dict(cls: Type[Self], data: Dict, *args, copy=False, **kwargs) -> Self:
        if copy:
            data = deepcopy(data)
        if "text_id" not in data:
            raise ValueError(f"'text_id' must be in input data dict")
        text_id = data.pop("text_id")
        return super().from_dict(data, *args, text_id=text_id, **kwargs)

    def to_dict(self, id_to_string=False):
        result = super().to_dict()
        if id_to_string:
            result["text_id"] = str(self.text_id)
        else:
            result["text_id"] = self.text_id
        return result


class Adjunct(Word):
    negative: bool

    @classmethod
    def from_dict(cls: Type[Self], data: Dict, *args, copy=False, **kwargs) -> Self:
        if copy:
            data = deepcopy(data)
        if "negative" not in data:
            raise ValueError(f"'negative' must be in input data dict")
        negative = data.pop("negative")
        return super().from_dict(data, *args, negative=negative, **kwargs)

    def to_dict(self):
        result = super().to_dict()
        result["negative"] = self.negative
        return result

    def __str__(self) -> str:
        return ("не " if self.negative else "") + super().__str__()

    def __repr__(self) -> str:
        return str(self)


class Adjective(BaseModel):
    adjective_id: Optional[Any]
    key_word: KeyWord
    adjective: Adjunct

    @classmethod
    def from_dict(cls: Type[Self], data: Dict, copy=False) -> Self:
        requred_keys = {"key_word", "adjective"}
        if copy:
            data = deepcopy(data)
        if len(requred_keys.difference(data.keys())) > 0:
            raise ValueError(f"{requred_keys.difference(data.keys())} must be in input data dict")
        adjective_id = data.pop("_id", None)
        key_word = KeyWord.from_dict(data.pop("key_word"))
        adjective = Adjunct.from_dict(data.pop("adjective"))
        return cls(adjective_id=adjective_id,
                    key_word=key_word,
                    adjective=adjective)

    def to_dict(self, id_to_string=False):
        adjective_dict = {"key_word": self.key_word.to_dict(id_to_string=id_to_string),
                     "adjective": self.adjective.to_dict()}
        if self.adjective_id is not None:
            if id_to_string:
                adjective_dict["_id"] = str(self.adjective_id)
            else:
                adjective_dict["_id"] = self.adjective_id
        return adjective_dict

    def __str__(self) -> str:
        return str(self.adjective) + " " + str(self.key_word)

    def __repr__(self) -> str:
        return str(self)

    def get_adjective_id(self) -> str:
        return self.adjective_id
