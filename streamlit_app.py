import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("xgb_liquidity_model.pkl")

# Streamlit app
st.set_page_config(page_title="Crypto 24h Volume Predictor", layout="centered")
st.title("📊 Crypto 24h Volume Predictor")
st.markdown("Enter the features below to predict the **24-hour trading volume** of a cryptocurrency.")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app uses an XGBoost model to predict the 24h trading volume of a crypto asset based on 5 features.
    
    🔍 Powered by **XGBoost**, **FastAPI**, and **Streamlit**.
    """)

# Input fields
price = st.number_input("💰 Price", value=40851.38)
change_1h = st.number_input("📈 1h Change", value=0.001)
change_24h = st.number_input("📊 24h Change", value=0.0)
change_7d = st.number_input("📉 7d Change", value=-0.027)
market_cap = st.number_input("🏦 Market Cap", value=776077432316.0)

# Submit button
if st.button("🔮 Predict"):
    try:
        features = np.array([price, change_1h, change_24h, change_7d, market_cap]).reshape(1, -1)
        prediction_log = model.predict(features)[0]
        prediction = np.expm1(prediction_log)  # reverse log1p
        st.success(f"💡 Predicted 24h Trading Volume: **${prediction:,.2f}**")
    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")
