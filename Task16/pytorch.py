import torch

a = torch.tensor([1, 2, 3])

print(a * 2)

# 2D Tensor
tensor2D = torch.tensor([
    [1, 2],
    [3, 4]
])

print(tensor2D)

arr = [
 [1,2],
 [3,4],
 [5,6]
]

tensor = torch.tensor(arr)

print(tensor.shape)