from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import requests

wind_router = APIRouter()


class WindOut(BaseModel):
    speed: float
    direction: int


def _meters_per_second_to_knots(mps: float) -> float:
    return round(mps * 1.94384,1)


@wind_router.get("/realtime/{location}")
async def get_wind_data(location: str) -> WindOut:
    """Retrieve the current data from the realtime2 data set."""
    lat, lon = location.split(",")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=e73aa31e7b34ba28ca327af468e3df8e"
    resp = requests.get(url)
    if resp.status_code == 200:
        meters_per_second = resp.json()["wind"]["speed"]
        degrees = resp.json()["wind"]["deg"]
        return WindOut(
            speed=_meters_per_second_to_knots(meters_per_second), direction=degrees
        )
    else:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
