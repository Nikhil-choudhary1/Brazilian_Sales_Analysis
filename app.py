import streamlit as st
import time
import matplotlib.pyplot as plt
from src.predict import predict_churn

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("Customer Churn Prediction")
st.markdown("Enter Customer Details")

recency = st.number_input("Recency (days)", min_value=0, step=1)
frequency = st.number_input("Frequency (orders)", min_value=0, step=1)
monetary = st.number_input("Monetary (total spend)", min_value=0.0, step=10.0)

if st.button("Predict"):

    st.subheader("Processing...")

    progress_bar = st.progress(0)
    status_text = st.empty()

    
    for i in range(100):
        time.sleep(0.03)  
        progress_bar.progress(i + 1)
        status_text.text(f"Analyzing customer... {i+1}%")
    
    prediction, probability = predict_churn(recency, frequency, monetary)
    progress_bar.empty()
    status_text.empty()


    st.success("Prediction Completed!")

    if prediction == 1:
        st.error(f"Customer will CHURN ({probability*100:.2f}%) ")
    else:
        st.success(f"Customer will RETAIN ({(1-probability)*100:.2f}%) ")

    st.subheader("Churn Risk Score")

    fig, ax = plt.subplots()

    ax.barh(["Risk"], [probability * 100])
    ax.set_xlim(0, 100)

    if probability > 0.7:
        color = "red"
    elif probability > 0.4:
        color = "orange"
    else:
        color = "green"

    ax.barh(["Risk"], [probability * 100], color=color)

    ax.set_xlabel("Probability (%)")
    ax.set_title("Churn Probability")

    st.pyplot(fig)