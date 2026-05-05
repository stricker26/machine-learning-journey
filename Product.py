class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_label(self):
        return "Expensive" if self.price > 1000 else "Affordable"
    
    def get_stock_status(self):
        return "In stock" if self.stock > 0 else "Out of stock"
    
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "label": self.get_label(),
            "stock_status": self.get_stock_status()
        }
    
product = Product("Laptop", 50000, 5)
print(product.to_dict())