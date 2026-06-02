import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/salaries.csv")

X = df[
    [
        "experience",
        "education_level",
        "certifications"
    ]
]

y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print(model.coef_)
print(model.intercept_)


joblib.dump(
    model,
    "trained_models/salary_model.pkl"
)