import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Dataset
data = {
    "experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "certifications": [0, 0, 1, 1, 2, 2, 3, 3, 4, 5],
    "salary": [25, 30, 40, 45, 55, 60, 70, 75, 85, 95]
}

df = pd.DataFrame(data)

# Features (MULTIPLE FEATURES)
X = df[["experience", "certifications"]]

# Label
y = df["salary"]

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

# Predict new employee salary
new_data = pd.DataFrame({
    "experience": [12],
    "certifications": [4]
})

salary_prediction = model.predict(new_data)

# Test predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)

# Output
print(f"Predicted Salary: ${salary_prediction[0]:.2f} thousands")
print(f"Mean Absolute Error: ${mae:.2f} thousands")