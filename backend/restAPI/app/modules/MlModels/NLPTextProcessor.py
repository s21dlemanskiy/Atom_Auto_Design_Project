from ..DataModels.Text import Text
import stanza
from nltk.tokenize import sent_tokenize
from nltk import download as nltk_download
from typing import Set, List, Dict, Optional, Any
from stanza.models.common.doc import Word, Sentence
from logging import error, info



class DepparseTextProcessor():
    def __init__(self, nlp=None):
        if nlp is None:
            nlp = stanza.Pipeline(lang='ru', processors='tokenize,pos,lemma,ner,depparse')
        self.nlp = nlp

    @staticmethod
    def get_lemma(word: str) -> str:
        nlp = stanza.Pipeline(lang='ru', processors='tokenize,lemma')
        result = nlp(word).to_dict()
        if len(result) < 1 or len(result[0]) < 1:
            error(f"{word} returns empty result while lemmatization: {result}")
            raise ValueError()
        return result[0][0]["lemma"]

    @classmethod
    def install_model(cls):
        info(f"Start loading models for {cls.__name__}....")
        stanza.Pipeline(lang='ru', processors='tokenize,pos,lemma,ner,depparse')
        nltk_download('punkt')
        info(f"Loaded models for {cls.__name__}")

    @classmethod
    def my_to_dict(cls, word_entity, length: int, text: Optional[Text] = None):
        result = {"deprel": word_entity.deprel,
                  "word": word_entity.text,
                  "lemma": word_entity.lemma,
                  'start_char': length + word_entity.start_char,
                  'end_char': length + word_entity.end_char}
        if text is not None:
            result["text_id"] = text.get_text_id()
        return result

    @classmethod
    def parce_feats(cls, x: str) -> Dict[str, str]:
        a = [tuple(i.split("=")) for i in x.split("|")]
        result = dict()
        for i in a:
            if len(i) == 2:
                result[i[0]] = i[1]
            else:
                print(f"Exception: parce_feats(x) {i}")
        return result

    @classmethod
    def add_adjective(cls, children: List[List[Word]], adjective: Word, used_ids: Set[int], text: Text,
                      key_word: Word, length: int) -> List[Dict[str, Any]]:
        result = []
        adjective_data = {"adjective": cls.my_to_dict(adjective, length),
                          "key_word": cls.my_to_dict(key_word, length, text)}
        if adjective.id in used_ids:
            return result
        used_ids.add(adjective.id)
        # проверям на наличие частички не
        # и на наличие прилогательных соединеных через частичку и например
        adjective_data["adjective"]["negative"] = False
        word_relation_children: List[Word] = children[adjective.id - 1]
        for relation_child in word_relation_children:
            if relation_child.lemma == "не":
                adjective_data["adjective"]["negative"] = True
                continue
            if relation_child.upos == "ADJ" and \
                    relation_child.deprel == "conj" and \
                    relation_child.id not in used_ids:
                # conj: соединительная конструкция. Метка conj обозначает слова или фразы,
                # соединенные союзами или соединительными элементами.
                result += cls.add_adjective(children, relation_child, used_ids, text, key_word, length)

        # добавляем прилогательное
        result.append(adjective_data)
        return result

    @classmethod
    def add_verb_with_dependences(cls, children: List[List[Word]], verb: Word, key_word: Word, text: Text,
                                  length: int) -> Dict[str, Any]:
        result = {}
        result["verb"] = cls.my_to_dict(verb, length, text)
        result["key_word"] = cls.my_to_dict(key_word, length)
        result["additinal"] = []
        result["negative"] = False
        word_relation_children: List[Word] = children[verb.id - 1]
        for relation_child in word_relation_children:
            if relation_child.id == key_word.id:
                continue
            if relation_child.lemma == "не":
                result["negative"] = True
                result["additinal"].append(cls.my_to_dict(relation_child, length, text))
                continue
            if relation_child.deprel == "xcomp":
                # xcomp: расширенное зависимое дополнение. Метка xcomp обозначает зависимое дополнение,
                # которое является частью основного глагола, но не управляется им.
                result["additinal"].append(cls.my_to_dict(relation_child, length, text))
                continue
            if relation_child.deprel == "obj":
                # obj: прямое дополнение. Метка obj обозначает прямое дополнение глагола, т.е. существительное
                # или фразу, которая является объектом действия глагола.
                if "additinal" not in result:
                    result["additinal"] = []
                result["additinal"].append(cls.my_to_dict(relation_child, length, text))
                continue
            if relation_child.deprel == "obl":
                # obl: обязательный аргумент или обстоятельство. Метка obl обычно относится к фразам, которые указывают
                # на обязательные аргументы или обстоятельства глагола.
                result["additinal"].append(cls.my_to_dict(relation_child, length, text))
                continue
        result["phrase"] = " ".join(list(map(lambda x: x["word"],
                                             sorted(result["additinal"] + [result["verb"], result["key_word"]],
                                                    key=lambda x: x["start_char"])
                                             )))
        return result

    def parce_adjectives_noun(self, sent: Sentence, text: Text, additional_length: int):
        adjectives_noun = []
        used_ids = set()
        # generate tuple of links to dependency child to make access faster
        childs = [list() for i in range(len(sent.words))]
        for entity in sent.words:
            if entity.head > 0:
                childs[entity.head - 1].append(entity)
        # for all noun find context
        for key_word in sent.words:
            word_context = {}
            if key_word.upos == "NOUN":
                noun = key_word
                # если сущ. это nsubj (подлежащее) то ищем сказуемое представленое прил. и добавляем в список
                if noun.deprel == "nsubj" and noun.head != 0 and sent.words[noun.head - 1].upos == "ADJ":
                    adjective = sent.words[noun.head - 1]
                    if adjective.id in used_ids:
                        continue
                    results = self.add_adjective(childs, adjective, used_ids, text, noun, additional_length)
                    adjectives_noun += results
            if key_word.upos == "ADJ":
                adjective = key_word
                if adjective.id in used_ids:
                    continue
                # если прил. это amod (определение) то ищем сущ которое оно определяет и добавляем в список
                if adjective.deprel == "amod" and adjective.head != 0 and sent.words[
                    adjective.head - 1].upos == "NOUN":
                    noun = sent.words[adjective.head - 1]
                    results = self.add_adjective(childs, adjective, used_ids, text, noun, additional_length)
                    adjectives_noun += results
        return adjectives_noun

    def process_review(self, text: Text):
        length = 0
        word_contexts = {"adjectives": [], "verb": []}
        for sentence in sent_tokenize(str(text), language="russian"):
            # if len(sentence) < 15:
            #     length += len(sentence) + 1
            #     continue
            doc = self.nlp(sentence)
            for sent in doc.sentences:
                word_contexts["adjectives"] += self.parce_adjectives_noun(sent, text, length)
            length += len(sentence) + 1

        return word_contexts


if __name__ == "__main__":
    nlp1 = stanza.Pipeline(lang='ru', processors='tokenize,pos,lemma,ner,depparse')
    text_example = "'Отличный автомобиль. С  двигателем 2,5 хорошая динамика. Просторный салон. Такой фишки,\
     как управление пассажирским сидением со стороны водителя, нет даже у немцев. Вывод картинки с камеры в зеркале на\
      приборку при включении поворотника просто огонь! Черный потолок! Светодиодная оптика офигенная. Вентиляция \
      сидений летом очень в тему. Диски колесные супер. Шумка отличная. Никакого звона камешков при езде. \
      Камера заднего вида с хорошим разрешением. Климат-контроль работает отлично. На руле есть все нужные кнопки.'"
    tp = DepparseTextProcessor(nlp1)
    word_context = tp.process_review(
        Text(text_id="id1id", text=text_example, mark="mark1", model="model1", link="lnk1"))
    for i in word_context["adjectives"]:
        print("не" if i["adjective"]["negative"] else "", i["adjective"]["word"], i["key_word"]["word"])
    # result:
    """  Отличный автомобиль
         хорошая динамика
         Просторный салон
         пассажирским сидением
         Черный потолок
         Светодиодная оптика
         офигенная оптика
         колесные супер
         отличная Шумка
         заднего вида
         хорошим разрешением
         нужные кнопки
         """
    print(word_context["adjectives"])
    # result:
    """[{
          "adjective": {
            "deprel": "amod",
            "word": "'Отличный",
            "lemma": "'отличный",
            "start_char": 0,
            "end_char": 9,
            "text_id": "id1id",
            "negative": false
          },
          "key_word": {
            "deprel": "root",
            "word": "автомобиль",
            "lemma": "автомобиль",
            "start_char": 10,
            "end_char": 20
          }
        },
        ......
    ]"""