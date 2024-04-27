from enum import Enum
from typing import Optional
from fastapi.responses import JSONResponse
import pydantic
from fastapi import FastAPI, Query, HTTPException
import uvicorn
import pandas as pd

app: FastAPI = FastAPI(debug=True)

class WaveProperties(str, Enum):
    mean_wave_direction = "MWD"
    average_period = "APD"
    significant_height = "WVHT"
    dominant_period = "DPD"
    water_temperature = "WTMP"


class BuoyDataOut(pydantic.BaseModel):
    buoy_id: int
    mean_wave_direction: Optional[float] = None
    average_period: Optional[float] = None
    significant_height: Optional[float] = None
    dominant_period: Optional[float] = None
    water_temperature: Optional[float] = None


@app.get("/realtime/{buoy_id}")
async def get_buoy_data(
    buoy_id: int,
    ):
    """Retrieve the current data from the realtime2 data set."""

    url = f"https://www.ndbc.noaa.gov/data/realtime2/{buoy_id}.txt"
    try:
        df_buoy = pd.read_csv(url, delim_whitespace=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    data = {"buoy_id": buoy_id }
    for prop in WaveProperties:
        try:
            data[prop.name] = df_buoy.loc[1][prop.value]
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

    return BuoyDataOut(**data)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)