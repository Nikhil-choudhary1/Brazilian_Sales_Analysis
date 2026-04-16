import joblib
import numpy as np

def predict_churn(recency, frequency, monetary):
    model = joblib.load("models/churn_model.pkl")

    data = np.array([[recency, frequency, monetary]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return prediction, probability