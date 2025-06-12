from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("xgb_liquidity_model.pkl")

app = FastAPI()

# Define request schema
class InputData(BaseModel):
    features: list  # must be in the same order as training

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.features).reshape(1, -1)
    prediction_log = model.predict(input_array)[0]
    prediction = np.expm1(prediction_log)  # reverse log1p
    return {"predicted_24h_volume": prediction}
