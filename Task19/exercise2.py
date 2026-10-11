from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

orig_sentence = """
Python is one of the most popular programming languages in the world,
and it is widely used for AI, web development, and automation.
"""

# convert to lowercase
sentence = orig_sentence.lower()

# remove punctuation
sentence = sentence.translate(
    str.maketrans('', '', string.punctuation)
)

# Tokenize
tokens = word_tokenize(sentence)

# Remove the stop words using NLTK
stop_words = set(stopwords.words("english"))

filtered = [
    word
    for word in tokens
    if word not in stop_words
    and word.isalpha()
]

print(f"Original sentence: {orig_sentence}")
print(f"Tokens: {tokens}")
print(f"Final filtered words: {filtered}")

# Exercise 2: Print the total number of English stop words.
print(f"Total number of English stop words: {len(stop_words)}")

# Exercise 3: Find whether these words are stop words:
words = [
    "the",
    "python",
    "is",
    "love",
    "we",
    "computer"
]

for word in words:
    print(f"{word} -> {word in stop_words}")