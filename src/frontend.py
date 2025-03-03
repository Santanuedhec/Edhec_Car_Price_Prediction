import streamlit as st
import requests
from pydantic import ValidationError
from src.CarFeatures import CarFeatures

st.title("Car Price Prediction")


levy = st.number_input("Levy", min_value=300, max_value=1500, value=500, step=10)
engine_volume = st.number_input("Engine Volume", min_value=1.0, max_value=4.0, value=2.0, step=0.1)
mileage = st.number_input("Mileage", min_value=0, max_value=330000, value=50000, step=1000)
cylinders = st.number_input("Cylinders", min_value=3, max_value=8, value=4)
doors = st.number_input("Doors", min_value=2, max_value=5, value=4)
airbags = st.number_input("Airbags", min_value=0, max_value=16, value=6)
age = st.number_input("Age", min_value=1, max_value=70, value=5)
leather_interior = st.number_input("Leather Interior (0 for No, 1 for Yes)", min_value=0, max_value=1, value=1)
turbo = st.number_input("Turbo (0 for No, 1 for Yes)", min_value=0, max_value=1, value=0)

wheel = st.selectbox("Wheel", options=["Left wheel", "Right-hand drive"])
drive_wheels = st.selectbox("Drive Wheels", options=["4x4", "Front", "Rear"])
gear_box_type = st.selectbox("Gear Box Type", options=["Automatic", "Manual", "Tiptronic", "Variator"])
fuel_type = st.selectbox("Fuel Type", options=["CNG", "Diesel", "Hybrid", "Hydrogen", "LPG", "Petrol", "Plug-in Hybrid"])
color = st.selectbox("Color", options=[
    "Beige", "Black", "Blue", "Brown", "Carnelian red", "Golden",
    "Green", "Grey", "Orange", "Pink", "Purple", "Red",
    "Silver", "Sky blue", "White", "Yellow"
])

if st.button("Predict Price"):
    input_data = {
        "Levy": levy,
        "Engine_volume": engine_volume,
        "Mileage": mileage,
        "Cylinders": cylinders,
        "Doors": doors,
        "Airbags": airbags,
        "Age": age,
        "Leather_interior": leather_interior,
        "Turbo": turbo,
        "Wheel": wheel,
        "Drive_wheels": drive_wheels,
        "Gear_box_type": gear_box_type,
        "Fuel_type": fuel_type,
        "Color": color
    }
    
    try:
        car_features = CarFeatures(**input_data)
    except ValidationError as e:
        st.error("Validation Error: " + str(e))
    else:
        api_url = "https://edhec-car-price-prediction.onrender.com/predict"
        try:
            response = requests.post(api_url, json=input_data)
            if response.status_code == 200:
                predicted_price = response.json().get("predicted_price", "No price returned")
                st.success(f"Predicted Price: {predicted_price}")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred while connecting to the API: {e}")