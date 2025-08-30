import numpy as np
import advancehandling as model
from fastapi import FastAPI, HTTPException # Web framework exceptions

app = FastAPI()

@app.post("/predict")
async def predict(data: dict):
    try:
        # Validate input
        if 'features' not in data:
            raise ValueError("'features' key is required in input JSON.")
        features = np.array(data['features'])
        # Make prediction
        prediction = model.predict(features.reshape(1, -1))
        return {"prediction": prediction.tolist()}
    except ValueError as e:
        # Raise an HTTP exception for the client
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Don't expose internal server errors to the client
        logger.exception("Internal error during prediction") # Logs the full traceback
        raise HTTPException(status_code=500, detail="An internal error occurred.")