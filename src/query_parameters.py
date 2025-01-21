# Import FastAPI
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define API route
## Query parameters with default values
@app.get("/default_items/")
async def read_items_default(start: int = 0, end: int = 10):
    return {"start": start, "end": end}

## Query parameters with optional values
@app.get("/optional_items/")
async def read_items_optional(start: int = 0, end: int = 10, q: str | None = None):
    if q:
        return {"start": start, "end": end, "q": q}
    return {"start": start, "end": end}

