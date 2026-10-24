from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your saved model
model = joblib.load('iris_model.pkl')

app = FastAPI(title="Iris Flower Species Prediction API")

# Define the expected input schema from users
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Welcome to the Iris ML Capstone API! Go to /docs to test predictions."}

@app.post("/predict")
def predict_species(data: IrisInput):
    # Format features into a 2D array for scikit-learn
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])
    
    # Predict using the loaded model
    prediction = model.predict(features)
    
    # Map numeric prediction to species name
    species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    predicted_species = species_map.get(int(prediction[0]), "Unknown")
    
    return {
        "prediction_code": int(prediction[0]),
        "predicted_species": predicted_species
    }
