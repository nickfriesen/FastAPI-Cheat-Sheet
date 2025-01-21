# Import FastAPI and BaseModel
from fastapi import FastAPI
from pydantic import BaseModel



# Define BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Create an instance of FastAPI
app = FastAPI()


# Define API routes
## GET operator: used to retrieve data (read-only)
@app.get("/get_items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


## POST operator: used to create new resources
@app.post("/post_items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


## PUT operator: used to update existing resources
@app.put("/put_items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


## DELETE operator: used to delete resources
@app.delete("/delete_items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted successfully!"}


## PATCH operator: used to partially update existing resources
@app.patch("/patch_items/{item_id}")
async def patch_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


## HEAD operator: used to retrieve only the metadata of a response
@app.head("/head_items/{item_id}")
async def head_item(item_id: int):
    return {"item_id": item_id, "message": "Item metadata retrieved successfully!"}


## OPTIONS operator: used to retrieve the supported HTTP methods
@app.options("/options_items/")
async def options_item():
    return {"message": "Supported HTTP methods retrieved successfully!"}


## TRACE operator: used debug and trace requests
@app.trace("/trace_items/")
async def trace_item():
    return {"message": "Request traced successfully!"}
