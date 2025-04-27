# predict.py

import joblib
import pandas as pd

def load_model():
    model = joblib.load('model.pkl')  # Only load model, no separate scaler anymore
    return model

def make_prediction(model, input_data):
    # input_data must be a dictionary matching the model features
    input_df = pd.DataFrame([input_data])
    
    prediction = model.predict(input_df)[0]
    return prediction
