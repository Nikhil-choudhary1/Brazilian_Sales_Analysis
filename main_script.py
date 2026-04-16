from src.components.data_ingestion import load_data
from src.components.feature_engineering import create_features
from src.components.model_trainer import train_model

def run_pipeline():
    print("Starting Pipeline...")

   
    print("📥 Loading data...")
    orders, customers, payments = load_data()

  
    print("Creating features...")
    df = create_features(orders, customers, payments)

    print("Feature Data Shape:", df.shape)
    print(df.head())

   
    print("Training model...")
    model = train_model(df)

    print("Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()