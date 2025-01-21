# Import FastAPI and BaseModel
from fastapi import FastAPI
from pydantic import BaseModel


# Create a data model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# Create an instance of FastAPI
app = FastAPI()


# Define API route
## Declaring the model as parameter
@app.post("/model_parameter_items/")
async def create_item(
    item: Item,
):  # The request body is declared as an instance of the Item class
    return {"item": item}


## Using the model
@app.post("/model_usage_items/")
async def model_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


## Request body with path and query parameter
@app.put("/combined_items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
