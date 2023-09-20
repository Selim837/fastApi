from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "King Selimbey"}

@app.get("/items/{item_id}")
async def get_item(item_id):
    return{"item_id": item_id}