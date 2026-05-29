import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "salary": [25, 30, 35, 40, 50, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]

# Label
y = df["salary"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
new_data = pd.DataFrame({
    "experience": [12]
})

prediction = model.predict(new_data)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print(f"Predicted Salary: ${prediction[0]:.2f} thousands")
print(f"Mean Absolute Error: ${mae:.2f} thousands")