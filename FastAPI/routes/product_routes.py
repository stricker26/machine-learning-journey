from fastapi import APIRouter
from models.product import Product

router = APIRouter(prefix="/products")

@router.get("/")
def get_products():
    products = [
        Product("Laptop", 50000, 5),
        Product("Mouse", 500, 0)
    ]

    return {
        "status": "success",
        "data": [p.to_dict() for p in products]
    }

@router.get("/download")
def download_products():
    return {
        "message": "Downloading products..."
    }