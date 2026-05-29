import pandas as pd

# ==========================================
# STEP 1: CREATE DATASET
# ==========================================

data = [
    ("Win a free iPhone now", "spam"),
    ("Limited offer buy now", "spam"),
    ("Congratulations you won a prize", "spam"),
    ("Click here to claim reward", "spam"),
    ("Earn money fast from home", "spam"),
    ("Exclusive promo just for you", "spam"),

    ("Hey are we still meeting today", "not spam"),
    ("Can you send me the file", "not spam"),
    ("Let's have lunch tomorrow", "not spam"),
    ("Are you available for call", "not spam"),
    ("Please review the document", "not spam"),
    ("I will arrive at 5pm", "not spam"),
]

# Create DataFrame
df = pd.DataFrame(data, columns=["text", "label"])

print("=== DATASET ===")
print(df)

# ==========================================
# STEP 2: SPLIT FEATURES AND LABELS
# ==========================================

# X = input data
# y = target/answer

X = df["text"]
y = df["label"]

# ==========================================
# STEP 3: TRAIN / TEST SPLIT
# ==========================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\n=== TRAIN DATA ===")
print(X_train)

print("\n=== TEST DATA ===")
print(X_test)

# ==========================================
# STEP 4: CONVERT TEXT TO NUMBERS
# ==========================================

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

# Learn words from training data
X_train_vec = vectorizer.fit_transform(X_train)

# Convert test data using learned words
X_test_vec = vectorizer.transform(X_test)

print("\n=== TF-IDF SHAPE ===")
print(X_train_vec.shape)

# ==========================================
# STEP 5: TRAIN CLASSIFICATION MODEL
# ==========================================

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

# Train model
model.fit(X_train_vec, y_train)

# ==========================================
# STEP 6: MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test_vec)

print("\n=== PREDICTIONS ===")
print(y_pred)

print("\n=== ACTUAL LABELS ===")
print(y_test.values)

# ==========================================
# STEP 7: CHECK ACCURACY
# ==========================================

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("\n=== ACCURACY ===")
print(accuracy)

# ==========================================
# STEP 8: TEST CUSTOM MESSAGES
# ==========================================

test_messages = [
    "Win money now",
    "Are we still on for tomorrow?",
    "Claim your free reward",
    "Please review the document",
    "Congratulations you won cash",
    "Can we schedule a meeting"
]

# Convert messages into vectors
test_vectors = vectorizer.transform(test_messages)

# Predict
predictions = model.predict(test_vectors)

print("\n=== CUSTOM MESSAGE PREDICTIONS ===")

for message, prediction in zip(test_messages, predictions):
    print(f"Message: {message}")
    print(f"Prediction: {prediction}")
    print("-----------------------------")