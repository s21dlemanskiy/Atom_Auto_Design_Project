from wiki_ru_wordnet import WikiWordnet
from typing import Optional, List
from nltk.tokenize import word_tokenize, sent_tokenize


class WordnetAPI:
    def __init__(self, wikiwordnet: Optional[WikiWordnet]=None):
        if wikiwordnet is None:
            wikiwordnet = WikiWordnet()
        self._wikiwordnet = wikiwordnet

    @staticmethod
    def install_model():
        WikiWordnet()

    def get_synonyms(self, word_lemma: str) -> List[str]:
        result = set()
        for synset in self._wikiwordnet.get_synsets(word_lemma):
            for w in synset.get_words():
                result.add(w.lemma())
        return list(result)

if __name__ == "__main__":
    wapi = WordnetAPI()
    print(wapi.get_synonyms("машиной"))