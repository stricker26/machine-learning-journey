import torch
from PIL import Image
from torchvision.models import resnet18, ResNet18_Weights

# Load pretrained weights
weights = ResNet18_Weights.DEFAULT

# Load model
model = resnet18(weights=weights)
model.eval()

# Use the preprocessing required by these weights
preprocess = weights.transforms()

# Load image
image = Image.open("dog.jpg").convert("RGB")

# Preprocess
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)

# Inference
with torch.no_grad():
    output = model(input_batch)

# Convert logits to probabilities
probabilities = torch.softmax(output, dim=1)

# Best prediction
predicted_index = torch.argmax(probabilities, dim=1).item()

confidence = probabilities[0][predicted_index].item()

# Lookup label
categories = weights.meta["categories"]

predicted_label = categories[predicted_index]

print(f"Prediction : {predicted_label}")
print(f"Confidence : {confidence:.2%}")