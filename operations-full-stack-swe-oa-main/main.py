from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class NumbersRequest(BaseModel):
    numbers: List[int]

@app.post("/sorted-numbers")
def sorted_numbers(req: NumbersRequest): #Validates with number request model
    numbers = req.numbers
    if not numbers:
        raise HTTPException(status_code=400, detail="List of numbers cannot be empty")
    return {
        "original_numbers": numbers,
        "sorted_numbers": sorted(numbers)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
