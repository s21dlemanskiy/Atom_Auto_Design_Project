from fastapi import APIRouter
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DAO.MangoDB import MangoDB
from ..MlModels.Synonyms import WordnetAPI
from ..MlModels.NLPTextProcessor import DepparseTextProcessor
from typing import List

router = APIRouter(prefix="/search", tags=["search"], responses={400: {"description": "bed params"}})

@router.post("/")
def search_by_words(words: List[str]):
    result = {}
    with MangoDB() as client:
        adjective_mg = AdjectiveManager(client)
        map_texts_adjectives = adjective_mg.get_adjectives_by_nouns(words)
        for text_id in map_texts_adjectives.keys():
            result[text_id] = {}
            result[text_id]["adjectives"] = list(map(lambda x: x.to_dict(id_to_string=True),
                                                                   map_texts_adjectives[text_id]["adjectives"]))
            result[text_id]["text"] = map_texts_adjectives[text_id]["text"].to_dict(ignore_id=True)
    return result


@router.get("/synonims")
def get_synonyms(word: str) -> List[str]:
    word_lemma = DepparseTextProcessor.get_lemma(word)
    wiki_wordnet = WordnetAPI()
    synonyms = wiki_wordnet.get_synonyms(word_lemma)
    if (word.lower() not in synonyms):
        synonyms.append(word.lower())
    return synonyms