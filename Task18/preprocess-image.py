from PIL import Image
from torchvision import transforms

image = Image.open("dog.jpg")

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)

print(input_tensor.shape)
print(input_batch.shape)