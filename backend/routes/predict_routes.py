from flask import Blueprint, request, jsonify
import pandas as pd
from backend.predict import load_model

predict_bp = Blueprint('predict', __name__)
model = load_model()

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Parse and cast fields properly
        input_data = {
            "Gender": data["Gender"],
            "Age": float(data["Age"]),
            "Height": float(data["Height"]),
            "Weight": float(data["Weight"]),
            "family_history_with_overweight": data["family_history_with_overweight"],
            "FAVC": data["FAVC"],
            "FCVC": float(data["FCVC"]),
            "NCP": float(data["NCP"]),
            "CAEC": data["CAEC"],
            "SMOKE": data["SMOKE"],
            "CH2O": float(data["CH2O"]),
            "SCC": data["SCC"],
            "FAF": float(data["FAF"]),
            "TUE": float(data["TUE"]),
            "CALC": data["CALC"],
            "MTRANS": data["MTRANS"],
            "BMI": float(data["BMI"])
        }

        # 🔥 Build a DataFrame not a NumPy array
        input_df = pd.DataFrame([input_data])

        # 🔥 Predict using DataFrame
        prediction = model.predict(input_df)

        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Error predicting"}), 500
