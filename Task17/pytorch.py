import torch
import torch.nn as nn

class StudentPredictor(nn.Module):

    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(1, 3)
        self.output = nn.Linear(3, 1)

    def forward(self, x):

        x = self.hidden(x)
        x = self.output(x)

        return x
    
model = StudentPredictor()

print(model)