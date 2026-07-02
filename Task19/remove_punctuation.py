import string

text = "Hello!!! AI, world."

clean = text.translate(
    str.maketrans("", "", string.punctuation)
)

print(clean)