import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from src.logger import logging
from src.config import MODEL_PATH
from sklearn.model_selection import GridSearchCV


def train_model(df):

    X = df[["recency", "frequency", "monetary"]]
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [5, 10, None],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=3,
        n_jobs=-1,
        verbose=2
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    logging.info(f"Best Parameters: {grid_search.best_params_}")

    y_pred = best_model.predict(X_test)

     
    logging.info("Model training completed")
    print(classification_report(y_test, y_pred))

    

    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    
    logging.info("Model saved successfully")

    return best_model