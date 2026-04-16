import streamlit as st
import time
from src.predict import predict_churn

st.title("Customer Churn Prediction")

recency = st.number_input("Recency (days)", min_value=0, step=1)
frequency = st.number_input("Frequency (orders)", min_value=0, step=1)
monetary = st.number_input("Monetary (total spend)", min_value=0.0, step=10.0)

if st.button("Predict"):

    st.subheader("Processing...")

    progress_bar = st.progress(0)

    
    for i in range(100):
        time.sleep(0.01)  
        progress_bar.progress(i + 1)

    result = predict_churn(recency, frequency, monetary)

    st.success("Prediction Completed!")

    if result == 1:
        st.error("Customer will CHURN ")
    else:
        st.success("Customer will RETAIN ")