from flask import Flask, request, jsonify
from flask_cors import CORS  # NEW
from predict import load_model, make_prediction

app = Flask(__name__)
CORS(app)  # NEW: allow cross-origin requests

# Load model at startup
model = load_model()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Obesity Insight Predictor API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        print("Received input data:", input_data)  # 🔥 Add this line

        if not input_data:
            return jsonify({"error": "No input data provided."}), 400

        prediction = make_prediction(model, input_data)
        return jsonify({"prediction": prediction})

    except Exception as e:
        print("Prediction error:", str(e))  # 🔥 Also add this
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
