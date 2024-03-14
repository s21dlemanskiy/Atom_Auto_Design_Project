

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import json

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
with open("1.txt", 'r', encoding="utf-8") as f:
    text = f.readline()
sentence_length = 0
sentences = []
index = 0
for i in range(len(text)):
    sentence_length += 1
    if text[i] == ".":
        sentence_length = 0
        sentences += [text[index:i]]
        index = i

word_to_find = "заряд"
results = model.predict(sentences, k=1)
for sentence, sentiment in zip(sentences, results):
    if word_to_find in sentence:
        # if "positive" in sentiment or "negative" in sentiment:
        print(sentence, '->', sentiment)