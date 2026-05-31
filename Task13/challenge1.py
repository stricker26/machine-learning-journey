from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# -----------------------------
# 1. SAMPLE DATASET (Spam vs Not Spam)
# -----------------------------
emails = [
    "Win money now",
    "Claim your free prize",
    "Limited offer buy now",
    "Meeting at 3pm",
    "Please review the report",
    "Lunch tomorrow?",
    "You won a free vacation",
    "Project deadline is today",
    "Earn cash fast",
    "Can we reschedule the meeting"
]

labels = [
    1, 1, 1, 0, 0, 0, 1, 0, 1, 0
]

# 1 = spam
# 0 = not spam

# -----------------------------
# 2. TEXT → NUMBERS (IMPORTANT STEP)
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
y = labels

# -----------------------------
# 3. TRAIN / TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

# -----------------------------
# 4. TRAIN MODEL
# -----------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# 5. PREDICT
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 6. EVALUATION METRICS
# -----------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# -----------------------------
# 7. DEBUG VIEW (VERY IMPORTANT FOR ENGINEERS)
# -----------------------------
print("\nPredictions vs Actual:")
for i in range(len(y_test)):
    print(f"Pred: {y_pred[i]} | Actual: {y_test[i]}")