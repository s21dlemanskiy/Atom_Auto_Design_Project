from fastapi import APIRouter
from ..DAO.TextManager import TextManager
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DAO.MangoDB import MangoDB
from ..MlModels.Synonyms import WordnetAPI
from ..MlModels.NLPTextProcessor import DepparseTextProcessor
from typing import List

router = APIRouter(prefix="/search", tags=["search"], responses={400: {"description": "bed params"}})

@router.get("/")
def search_by_words(words: List[str]):
    result = {}
    with MangoDB() as client:
        adjective_mg = AdjectiveManager(client)
        adjectives = adjective_mg.get_adjectives_by_nouns(words)
        for adj in adjectives:
            if adj["text"]["_id"] not in result:
                result[adj["text"]["_id"]] = []
            result[adj["text"]["_id"]].append(adj)
    return result

@router.get("/synonims")
def get_synonyms(word: str) -> List[str]:
    word_lemma = DepparseTextProcessor.get_lemma(word)
    wiki_wordnet = WordnetAPI()
    synonyms = wiki_wordnet.get_synonyms(word_lemma)
    return synonyms