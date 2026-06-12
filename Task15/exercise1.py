import numpy as np

# -----------------------
# Data
# -----------------------
X = np.array([
    [1, 50],
    [2, 60],
    [3, 70],
    [4, 80],
    [5, 90]
])

y = np.array([[0], [0], [0], [1], [1]])

# -----------------------
# Activation function
# -----------------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# derivative (needed for learning)
def sigmoid_derivative(z):
    return z * (1 - z)

# -----------------------
# Initialize parameters
# -----------------------
np.random.seed(42)

W = np.random.randn(2, 1)
b = np.random.randn(1)

learning_rate = 0.01

# -----------------------
# Training loop
# -----------------------
for epoch in range(2000):

    # Forward propagation
    z = np.dot(X, W) + b
    pred = sigmoid(z)

    # Loss (MSE for simplicity)
    loss = np.mean((y - pred) ** 2)

    # Backpropagation
    error = y - pred
    d_pred = error * sigmoid_derivative(pred)

    dW = np.dot(X.T, d_pred)
    db = np.sum(d_pred)

    # Update weights
    W += learning_rate * dW
    b += learning_rate * db

    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# -----------------------
# Final predictions
# -----------------------
print("\nFinal Predictions:")
print(pred)

# Convert to 0 or 1
binary_output = (pred > 0.5).astype(int)
print("\nBinary Output:")
print(binary_output)