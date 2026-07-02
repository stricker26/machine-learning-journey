from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sentence = "I love learning AI because it is very interesting."

tokens = word_tokenize(sentence.lower())

stop_words = stopwords.words("english")

filtered = []

for word in tokens:
    if word not in stop_words:
        filtered.append(word)

print(filtered)