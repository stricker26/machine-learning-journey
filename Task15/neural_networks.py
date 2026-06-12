import numpy as np

# Inputs (experience, education)
X = np.array([
    [2, 1],
    [3, 2],
    [5, 3]
])

# Output (salary)
y = np.array([[3000], [5000], [8000]])

# Initialize weights
W = np.random.randn(2, 1)
b = np.random.randn(1) # Bias term (A value added to the result to shift the output up or down.)

learning_rate = 0.01

for epoch in range(1000):
    # Forward pass
    z = np.dot(X, W) + b
    pred = z  # no activation for simplicity

    # Loss (MSE)
    loss = np.mean((y - pred) ** 2)

    # Gradient
    dW = -2 * np.dot(X.T, (y - pred)) / len(X)
    db = -2 * np.mean(y - pred)

    # Update
    W -= learning_rate * dW
    b -= learning_rate * db

    if epoch % 100 == 0:
        print(f"Loss: {loss}")

print("Final prediction:", pred)