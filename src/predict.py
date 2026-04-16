import joblib
import numpy as np
import pandas as pd
import pickle
from src.config import MODEL_PATH

def predict_churn(recency, frequency, monetary):
    model = joblib.load(MODEL_PATH)

    data = pd.DataFrame([{
        "recency": recency,
        "frequency": frequency,
        "monetary": monetary
    }])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return prediction, probability