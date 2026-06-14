import torch

users = torch.tensor([
    [25, 50000],
    [30, 60000],
    [35, 70000]
])

print(users)
print(users.shape)

# Tensors Operations
a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])

print(a + b)
print(a * b)

c = torch.tensor([10,20,30])

# Indexing
print(c[0])

# Slicing
print(c[0:2])