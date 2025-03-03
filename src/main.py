from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.CarFeatures import CarFeatures
import pandas as pd
import numpy as np
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to my Car Price Prediction API!"}

with open("src/car_price_prediction.pickle", "rb") as f:
    rf_clf = pickle.load(f)

def predict_price_auto(user_input: dict) -> float:
    
    feature_names = rf_clf.feature_names_in_
    features = []
    
    for col in feature_names:
        if "_" not in col:
            
            features.append(user_input.get(col, 0))
        else:
            
            category, dummy_val = col.split("_", 1)
            if category in user_input:
                if user_input[category].strip().lower() == dummy_val.strip().lower():
                    features.append(1)
                else:
                    features.append(0)
            else:
                features.append(0)
    
    
    features_df = pd.DataFrame([features], columns=feature_names)
    return rf_clf.predict(features_df)[0]

@app.post("/predict")
def predict_price_api(features: CarFeatures):
    
    
    user_input = {
        "Levy": features.Levy,
        "Leather interior": features.Leather_interior,
        "Engine volume": features.Engine_volume,
        "Mileage": features.Mileage,
        "Cylinders": features.Cylinders,
        "Doors": features.Doors,
        "Airbags": features.Airbags,
        "Age": features.Age,
        "Turbo": features.Turbo,
        "Wheel": features.Wheel,
        "Drive wheels": features.Drive_wheels,
        "Gear box type": features.Gear_box_type,
        "Fuel type": features.Fuel_type,
        "Color": features.Color
    }
    
    predicted_price = predict_price_auto(user_input)
    return {"predicted_price": predicted_price}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
