from typing import Dict, Optional, Any, Set, Type
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self
from copy import deepcopy
from pydantic import BaseModel



class Text(BaseModel):
    text: str
    mark: str
    model: str
    link: str
    body_type: str
    other_data: Dict[str, Any]
    text_id: Optional[Any] = None

    def __init__(self, text: str, mark: str, model: str, link: str, body_type: Optional[str] = None,
                 other_data: Optional[Dict[str, Any]] = None, text_id: Optional[str] = None):
        if other_data is None:
            other_data = {}
        if body_type is None:
            body_type = "UNDEFIND"
        super().__init__(text_id=text_id,
                         text=text,
                         mark=mark,
                         model=model,
                         link=link,
                         body_type=body_type,
                         other_data=other_data)

    @classmethod
    def from_dict(cls: Type[Self], data: Dict, copy=False) -> Self:
        requred_keys = {"text", "mark", "model", "body_type", "link"}
        if copy:
            data = deepcopy(data)
        if len(requred_keys.difference(data.keys())) > 0:
            raise ValueError(f"{requred_keys.difference(data.keys())} must be in input data dict")
        text_id = data.pop("_id", None)
        text = data.pop("text")
        link = data.pop("link")
        mark = data.pop("mark")
        model = data.pop("model")
        body_type = data.pop("body_type")
        other_data = data.pop("other_data", {})
        other_data.update(data)
        return cls(text_id=text_id,
                    text=text,
                    mark=mark,
                    model=model,
                    link=link,
                    body_type=body_type,
                    other_data=other_data)

    def to_dict(self, ignore_id=True):
        text_dict = {"text": self.text,
                     "mark": self.mark,
                     "model": self.model,
                     "link": self.link,
                     "body_type": self.body_type,
                     "other_data": self.other_data}
        if self.text_id is not None and not ignore_id:
            text_dict["_id"] = self.text_id
        return text_dict

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return str(self)

    def get_text_id(self) -> str:
        return self.text_id
