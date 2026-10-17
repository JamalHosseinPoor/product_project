import json
from pydantic import BaseModel


# 1. Define a model for one product
class ProductModel(BaseModel):
    p_code: int
    title: str
    price: float
    qty: int


# 2. Define a model for the list of products
class ProductManyModel(BaseModel):
    products: list[ProductModel]


# 3. Read the JSON file
with open("products.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# 4. Validate the data using Pydantic
validated_data = ProductManyModel(**data)

# 5. Print the existing products
print("Current products:")

for product in validated_data.products:
    print(
        f"Name: {product.title}, "
        f"Price: {product.price}, "
        f"Quantity: {product.qty}"
    )


# 6. Create a new product
new_product = ProductModel(
    p_code=104,
    title="Headphone",
    price=1200,
    qty=8
)

# 7. Add the new product if it does not already exist
# if not any(
#     product.p_code == new_product.p_code
#     for product in validated_data.products
# ):
for product in validated_data.products:
    if product.p_code != new_product.p_code:
        validated_data.products.append(new_product)

# 8. Save the updated data to the JSON file
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(
        validated_data.model_dump(),
        file,
        indent=4,
        ensure_ascii=False
    )

print("\nUpdated products saved successfully.")
