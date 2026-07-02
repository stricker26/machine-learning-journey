from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

sentence = "Hello!!! I LOVE Python, AI, and Laravel!!!"

# Convert to lowercase
lowercase_sentence = sentence.lower()

# Remove punctuation
clean_text = lowercase_sentence.translate(
    str.maketrans("", "", string.punctuation)
)

# Tokenization
tokens = word_tokenize(clean_text)

print(f"Original Text: {sentence}")
print(f"Lowercase Text: {lowercase_sentence}")
print(f"Text without Punctuation: {clean_text}")
print(f"Final token lists: {tokens}")

stop_words = set(stopwords.words("english"))

filtered_tokens = [
    token
    for token in tokens
    if token not in stop_words
]

print(f"Filtered token lists: {filtered_tokens}")