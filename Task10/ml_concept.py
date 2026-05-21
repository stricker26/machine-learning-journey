import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Sample dataset
data = {
    "size": [50, 60, 80, 100, 120],
    "price": [3, 4, 5, 7, 8]
}

df = pd.DataFrame(data)

# Features
X = df[["size"]]

# Label
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
new_data = pd.DataFrame({
    "size": [50]
})

prediction = model.predict(new_data)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print(f"Predicted price: {prediction[0]:.2f} million")
print(f"Mean Absolute Error: {mae:.2f} million")