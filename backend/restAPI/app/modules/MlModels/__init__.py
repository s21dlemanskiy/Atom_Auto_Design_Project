
from .SentimentAnalys import DeepavlovAPI
from logging import info
info("Start loading models")
DeepavlovAPI.install_model()

from .NLPTextProcessor import DepparseTextProcessor
DepparseTextProcessor.install_model()

from .Synonyms import WordnetAPI
WordnetAPI.install_model()

info("End models loading")