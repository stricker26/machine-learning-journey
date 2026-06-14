import torch

# Exercise 1
print(torch.__version__)
print(torch.cuda.is_available())

# Exercise 2
users = torch.tensor([
    [25, 50000],
    [30, 60000],
    [35, 70000]
])

print(users.shape)

# Exercise 3
scores = torch.tensor([80, 90, 100, 95, 88])

print("First:", scores[0])
print("Last:", scores[-1])
print("First Three:", scores[:3])