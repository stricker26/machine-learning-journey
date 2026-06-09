import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

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

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print(model.coef_)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

print(mae)

r2 = r2_score(
    y_test,
    predictions
)

print(r2)