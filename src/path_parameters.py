# Import FastAPI and Enum
from enum import Enum
from fastapi import FastAPI


# Define enumeration class
class ModelName(str, Enum):  # Inherit from str and Enum
    model_1 = "first_try"
    model_2 = "second_try"
    model_3 = "third_try"


# Create an instance of FastAPI
app = FastAPI()


# Define API routes
## Path parameters with types
@app.get(
    "/get_items/{item_id}"
)  # The path parameter 'item_id' will be passed to the function
async def get_item(
    item_id: int,
):  # The path parameter 'item_id' is declared as an integer
    return {"item_id": item_id}


## Path parameters with predefined values
@app.get(
    "/get_models/{model_name}"
)  # The path parameter 'model_name' will be passed to the function
async def get_model(model_name: ModelName):
    if model_name is ModelName.model_1:
        return {"model_name": model_name, "message": "Worked on the first model!"}

    if model_name is ModelName.model_2:
        return {"model_name": model_name, "message": "Worked on the second model!"}

    return {"model_name": model_name, "message": "Threee times a charm!"}


## Path parameters containing paths
@app.get(
    "/get_files/{file_path:path}"
)  # :path is a special type that will match any path
async def read_file(file_path: str):
    return {"file_path": file_path}
