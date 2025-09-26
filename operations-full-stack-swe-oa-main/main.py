from fastapi import FastAPI, HTTPException
#uvicorn main:app --reload

app = FastAPI()
@app.get("/sorted-numbers")
def sorted_numbers(numbers: list):
    sorted_numbers = sorted(numbers)
    return {"original_numbers":numbers,
            "sorted_numbers":sorted_numbers}



if __name__ == "__main__":
    sorted_numbers([3,1,2])
    uvicorn.run(app, port=8000, host="0.0.0.0")
