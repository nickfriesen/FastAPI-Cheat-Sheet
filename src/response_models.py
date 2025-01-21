# Import FastAPI and BaseModel
from fastapi import FastAPI
from pydantic import BaseModel


# Define BaseModel and ReponseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class ItemResponse(BaseModel):
    name: str
    price: float
    discounted_price: float


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
}

# Create an instance of FastAPI
app = FastAPI()


# Define API route
## Using type annotations
@app.post("/items/")
async def create_item(
    item: Item,
) -> Item:  # The response body is annotated with the Item class
    return item


## Using reponse_model parameter
@app.post(
    "/items/", response_model=ItemResponse
)  # The response body is declared as an instance of the ItemResponse class
def create_item_response_model(item: Item):
    discounted = item.price * 0.9
    return {"name": item.name, "price": item.price, "discounted_price": discounted}


## Using the response_model_exclude_unset parameter
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def read_item(item_id: str):
    return items[item_id]
