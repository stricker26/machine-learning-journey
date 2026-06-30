import torch
from PIL import Image
from torchvision.models import resnet18, ResNet18_Weights

# ----------------------------
# Load pretrained model
# ----------------------------
weights = ResNet18_Weights.DEFAULT

model = resnet18(weights=weights)
model.eval()

# Official preprocessing
preprocess = weights.transforms()

# ImageNet labels
categories = weights.meta["categories"]


def predict_image(image_path):
    # Load image
    image = Image.open(image_path).convert("RGB")

    # Preprocess
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    # Inference
    with torch.no_grad():
        output = model(input_batch)

    # Convert logits to probabilities
    probabilities = torch.softmax(output, dim=1)[0]

    # Top 5 predictions
    top5_probabilities, top5_indices = torch.topk(probabilities, 5)

    predictions = []

    for index, probability in zip(top5_indices, top5_probabilities):
        predictions.append({
            "class_index": index.item(),
            "label": categories[index.item()],
            "confidence": probability.item()
        })

    return predictions


# --------------------------------
# Test Images
# --------------------------------
images = [
    "images/dog.jpg",
    "images/car.jpg",
    "images/apple.jpg"
]

for image_path in images:

    print("=" * 60)
    print(f"Image: {image_path}")
    print("=" * 60)

    predictions = predict_image(image_path)

    for rank, prediction in enumerate(predictions, start=1):

        print(
            f"{rank}. "
            f"{prediction['label']:<30}"
            f"{prediction['confidence']:.2%}"
        )

    print()