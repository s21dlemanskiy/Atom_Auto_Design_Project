from fastapi import APIRouter
from ..DAO.TextManager import TextManager
from ..DAO.AdjectiveManager import AdjectiveManager
from ..DataModels.Text import Text
from ..MlModels.NLPTextProcessor import DepparseTextProcessor
from ..MlModels.SentimentAnalys import DeepavlovAPI
from ..DAO.MangoDB import MangoDB

router = APIRouter(prefix="/add_data", tags=["search"], responses={400: {"description": "bed params"}})


@router.post("/text")
def add_text(text: Text):
    with MangoDB() as client:
        try:
            # add text sentiment option to text data
            sentiment_model = DeepavlovAPI()
            text = sentiment_model.add_sentiment(text)

            # install text in mongoDB, and get it's ID
            text_id, *_ = TextManager(client).save_texts(text)
            text.text_id = text_id

            # parce adjectives from text
            dtp = DepparseTextProcessor()
            words_contexts = dtp.process_review(text)
            adjectives = words_contexts["adjectives"]

            # insert ajectives in mongoDB
            resultset = AdjectiveManager(client).add_adjectives(adjectives)
        except Exception as e:
            client.abort_transaction()
            raise e
