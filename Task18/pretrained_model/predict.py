import torch
from PIL import Image
from torchvision.models import resnet18, ResNet18_Weights

# Load pretrained model only once
weights = ResNet18_Weights.DEFAULT

model = resnet18(weights=weights)
model.eval()

# Official preprocessing
preprocess = weights.transforms()

# ImageNet class names
categories = weights.meta["categories"]


def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")

    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    probabilities = torch.softmax(output, dim=1)

    predicted_index = torch.argmax(probabilities, dim=1).item()

    confidence = probabilities[0][predicted_index].item()

    prediction = categories[predicted_index]

    return {
        "prediction": prediction,
        "confidence": confidence
    }


# Test images
images = [
    "images/dog.jpg",
    "images/car.jpg",
    "images/apple.jpg"
]

for image in images:
    result = predict_image(image)

    print("=" * 50)
    print(f"Image      : {image}")
    print(f"Prediction : {result['prediction']}")
    print(f"Confidence : {result['confidence']:.2%}")