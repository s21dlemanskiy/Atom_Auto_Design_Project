from wiki_ru_wordnet import WikiWordnet
from typing import Optional, List
from logging import info


class WordnetAPI:
    def __init__(self, wikiwordnet: Optional[WikiWordnet]=None):
        if wikiwordnet is None:
            wikiwordnet = WikiWordnet()
        self._wikiwordnet = wikiwordnet

    @classmethod
    def install_model(cls):
        info(f"Start loading models for {cls.__name__}....")
        WikiWordnet()
        info(f"Loaded models for {cls.__name__}")

    def get_synonyms(self, word_lemma: str) -> List[str]:
        result = set()
        for synset in self._wikiwordnet.get_synsets(word_lemma):
            for w in synset.get_words():
                result.add(w.lemma())
        return list(result)

if __name__ == "__main__":
    wapi = WordnetAPI()
    print(wapi.get_synonyms("машиной"))