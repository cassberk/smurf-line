from fastapi import FastAPI
import uvicorn

app: FastAPI = FastAPI(debug=True)


@app.get("/items/{item_id}")
async def get_buoy_data(item_id: int):
    return {"message": "Bye World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)