// frontend/src/pages/PredictionForm.tsx
import React, { useState } from 'react';
import axios from 'axios';

interface FormData {
  Gender: string;
  Age: string;
  Height: string;
  Weight: string;
  family_history_with_overweight: string;
  FAVC: string;
  FCVC: string;
  NCP: string;
  CAEC: string;
  SMOKE: string;
  CH2O: string;
  SCC: string;
  FAF: string;
  TUE: string;
  CALC: string;
  MTRANS: string;
  BMI: string;
}

interface PredictionResponse {
  prediction: string;
}

const initialFormData: FormData = {
  Gender: '',
  Age: '',
  Height: '',
  Weight: '',
  family_history_with_overweight: '',
  FAVC: '',
  FCVC: '',
  NCP: '',
  CAEC: '',
  SMOKE: '',
  CH2O: '',
  SCC: '',
  FAF: '',
  TUE: '',
  CALC: '',
  MTRANS: '',
  BMI: '',
};

function preparePredictionData(formData: FormData) {
  return {
    Gender: formData.Gender,
    Age: Number(formData.Age),
    Height: Number(formData.Height),
    Weight: Number(formData.Weight),
    family_history_with_overweight: formData.family_history_with_overweight,
    FAVC: formData.FAVC,
    FCVC: Number(formData.FCVC),
    NCP: Number(formData.NCP),
    CAEC: formData.CAEC,
    SMOKE: formData.SMOKE,
    CH2O: Number(formData.CH2O),
    SCC: formData.SCC,
    FAF: Number(formData.FAF),
    TUE: Number(formData.TUE),
    CALC: formData.CALC,
    MTRANS: formData.MTRANS,
    BMI: Number(formData.BMI),
  };
}

const PredictionForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [prediction, setPrediction] = useState<string>('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const preparedData = preparePredictionData(formData);
  
      const response = await axios.post<PredictionResponse>('http://127.0.0.1:5000/predict', preparedData);
  
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Prediction error:', error);
      setPrediction('Error predicting.');
    }
  };  

  return (
    <div style={{ padding: '20px' }}>
      <h2>Obesity Risk Predictor</h2>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px' }}>
        {Object.entries(formData).map(([key, value]) => (
          <div key={key} style={{ marginBottom: '10px' }}>
            <label htmlFor={key} style={{ display: 'block', marginBottom: '5px' }}>
              {key}:
            </label>
            <input
              type="text"
              id={key}
              name={key}
              value={value}
              onChange={handleChange}
              style={{ width: '100%', padding: '8px' }}
            />
          </div>
        ))}
        <button type="submit" style={{ padding: '10px', marginTop: '10px' }}>
          Predict
        </button>
      </form>

      {prediction && (
        <div style={{ marginTop: '20px' }}>
          <h3>Prediction:</h3>
          <p>{prediction}</p>
        </div>
      )}
    </div>
  );
};

export default PredictionForm;
