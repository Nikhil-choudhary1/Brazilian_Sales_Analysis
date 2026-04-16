import pandas as pd

def create_features(orders, customers, payments):

    df = orders.merge(customers, on="customer_id") \
               .merge(payments, on="order_id")

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

   
    snapshot_date = df["order_purchase_timestamp"].max()

   
    rfm = df.groupby("customer_unique_id").agg({
        "order_purchase_timestamp": lambda x: (snapshot_date - x.max()).days,
        "order_id": "count",
        "payment_value": "sum"
    }).reset_index()

    rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

    
    rfm["churn"] = rfm["recency"].apply(lambda x: 1 if x > 180 else 0)

    return rfm