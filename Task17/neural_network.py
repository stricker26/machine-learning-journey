import torch
import torch.nn as nn

# Training Data
hours = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

scores = torch.tensor([
    [20.0],
    [35.0],
    [50.0],
    [65.0],
    [80.0]
])

# Model
class StudentPredictor(nn.Module):

    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(1, 3)
        self.relu = nn.ReLU() #Rectified Linear Unit
        self.output = nn.Linear(3, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)

        return x


model = StudentPredictor()

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)

# Training Loop
for epoch in range(1000):

    optimizer.zero_grad()

    prediction = model(hours)

    loss = criterion(
        prediction,
        scores
    )

    loss.backward()

    optimizer.step()

    if epoch % 100 == 0:
        print(
            f"Epoch {epoch}, Loss: {loss.item():.4f}"
        )

with torch.no_grad():
    prediction = model(
        torch.tensor([[5.0]])
    )

    print(prediction)