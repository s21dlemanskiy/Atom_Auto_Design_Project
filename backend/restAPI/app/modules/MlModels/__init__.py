
from .SentimentAnalys import DeepavlovAPI
DeepavlovAPI.install_model()

from .NLPTextProcessor import DepparseTextProcessor
DepparseTextProcessor.install_model()

from .Synonyms import WordnetAPI
WordnetAPI.install_model()