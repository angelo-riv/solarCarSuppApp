from fastapi import FastAPI, HTTPException
#uvicorn main:app --reload

items = ["bumba"]

app = FastAPI()
@app.get("/")
def root():
    return {"Hello":"World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = items[item_id]
    return items

@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]

print("hi")

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
