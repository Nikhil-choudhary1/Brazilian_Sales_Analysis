import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from src.logger import logging
from src.config import MODEL_PATH

def train_model(df):

    X = df[["recency", "frequency", "monetary"]]
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
     
    logging.info("Model training completed")
    print(classification_report(y_test, y_pred))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    
    logging.info("Model saved successfully")

    return model