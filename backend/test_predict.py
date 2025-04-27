from predict import load_model, make_prediction

# Load the model
model = load_model()

# Sample input (must match training feature names and types)
sample_input = {
    'Gender': 'Male',
    'Age': 22,
    'Height': 1.75,
    'Weight': 75,
    'family_history_with_overweight': 'yes',
    'FAVC': 'no',
    'FCVC': 3,
    'NCP': 3,
    'CAEC': 'Sometimes',
    'SMOKE': 'no',
    'CH2O': 2,
    'SCC': 'no',
    'FAF': 1,
    'TUE': 0.5,
    'CALC': 'Frequently',
    'MTRANS': 'Public_Transportation',
    'BMI': 24.5
}

# Make a prediction
prediction = make_prediction(model, sample_input)

print(f"Predicted Obesity Category: {prediction}")