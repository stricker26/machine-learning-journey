from torchvision.models import resnet18

model = resnet18(weights="DEFAULT")

print(model)