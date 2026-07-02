from nltk.tokenize import word_tokenize
import string

sentence = "Hello!!! I LOVE Python, AI, and Laravel!!!"

# Convert to lowercase
lowercase_sentence = sentence.lower()

# Remove punctuation
clean = lowercase_sentence.translate(
    str.maketrans("", "", string.punctuation)
)

# Tokenization
tokens = word_tokenize(clean)

# Stop words
stop_words = [
    "i",
    "and"
]

print(f"Original Text: {sentence}")
print(f"Lowercase Text: {lowercase_sentence}")
print(f"Text without Punctuation: {clean}")
print(f"Final token lists: {tokens}")

# Filtered token
filtered_tokens = []

for token in tokens:
    if token not in stop_words:
        filtered_tokens.append(token)

print(f"Filtered token lists: {filtered_tokens}")

# Pythonic version
filtered_tokens_pythonic = [
    token 
    for token in tokens 
    if token not in stop_words
]

print(f"Filtered token lists (Pythonic): {filtered_tokens_pythonic}")