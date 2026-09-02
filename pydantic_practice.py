from pydantic import BaseModel, ValidationError
from pydantic import Field

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int
    in_stock: bool
    description: str | None = None

def describe(product: Product) -> str:
    return (
        f"Product Name: {product.name}\n"
        f"Price: ${product.price}\n"
        f"Quantity: {product.quantity}\n"
        f"In Stock: {'Yes' if product.in_stock else 'No'}\n"
        f"Description: {product.description or 'No description available.'}"
    )

if __name__ == "__main__":
    try:
        product = Product(
            name="Sample Product",
            price=19.99,
            quantity=10,
            in_stock=True,
            description="This is a sample product."
        )
        print(describe(product))
    except ValidationError as e:
        print("Validation error:", e)