from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

sentence = "I LOVE Python, AI, and Laravel!!!"

# lowercase
sentence = sentence.lower()

# remove punctuation
sentence = sentence.translate(
    str.maketrans('', '', string.punctuation)
)

# tokenize
tokens = word_tokenize(sentence)

# stop words
stop_words = stopwords.words("english")

filtered = [
    word
    for word in tokens
    if word not in stop_words
]

print(filtered)