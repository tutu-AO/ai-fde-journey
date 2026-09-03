from pydantic import BaseModel, ValidationError
from pydantic import Field
from dotenv import load_dotenv
import openai

load_dotenv()

class Product(BaseModel):
    name: str
    price: float | None = Field(default=None, gt=0)      # now the model is allowed to say "not present"
    quantity: int
    in_stock: bool
    description: str | None = None


client = openai.OpenAI()
try:
    description = input("Describe the product: ")
    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "Extract the product information from the user's text."},
            {"role": "user", "content": description},
        ],
        text_format=Product,          # ← your Pydantic model is the contract
    )
    product = response.output_parsed
    print(product)
    print(product.model_dump())   # ← a validated Product instance, not text
except ValidationError as e:
    print("Validation error:", e)
except openai.APIError as e:
    print("OpenAI API error:", e)
