import pandas as pd
from pymongo import MongoClient

def load_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ecommerce"]

    orders = pd.DataFrame(list(db["orders"].find()))
    customers = pd.DataFrame(list(db["customers"].find()))
    payments = pd.DataFrame(list(db["payments"].find()))

 
    for df in [orders, customers, payments]:
        if "_id" in df.columns:
            df.drop(columns=["_id"], inplace=True)

    return orders, customers, payments