from fastapi import APIRouter, FastAPI
import uvicorn
from .api.waves.endpoints import wave_router

app: FastAPI = FastAPI(debug=True)

version_router: APIRouter = APIRouter()

# ----- Versioned Routers Start ----- #

version_router.include_router(
    wave_router, prefix="/waves", tags=["waves"]
)

app.include_router(version_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
