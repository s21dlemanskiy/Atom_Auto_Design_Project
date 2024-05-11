from ..DataModels.Text import Text
from logging import info
# from deeppavlov import configs, build_model

class DeepavlovAPI():
    @classmethod
    def install_model(cls):
        info(f"Start loading models for {cls.__name__}....")
        # build_model(configs.classifiers.rusentiment_convers_bert, download=True)
        info(f"Loaded models for {cls.__name__}")

    # transformers
    # deeppavlov == 1.6.0

    def __init__(self):
        pass
        # self._model = build_model(configs.classifiers.rusentiment_convers_bert, download=True)


    def add_sentiment(self, text: Text, replace=False) -> Text:
        """ add to text sentiment analys (examle: {'label': 'NEUTRAL', 'score': 1})
            text: text to analys
            replace: if text_sentiment alredy exists, need to replace?"""
        if "text_sentiment" in text.other_data and not replace:
            return text
        # santiment = self._model([str(text)])
        # text.other_data.update({'text_sentiment': {'label': santiment.upper(), 'score': 1}})
        text.other_data.update({'text_sentiment': {'label': "UNDEFIND", 'score': 1}})
        return text
