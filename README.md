# Crypto 24h Volume Predictor

A machine learning-powered web application to forecast the **24-hour cryptocurrency trading volume** using real-time market indicators.

This Streamlit app leverages a trained **XGBoost regression model** to make accurate predictions based on features like price, market cap, volume trends, and percentage change over time.

---

## Tech Stack
-  Python
-  XGBoost (ML model)
-  FastAPI (Backend)
-  Streamlit (Frontend)

---

## Features
- Predicts 24h crypto trading volume from real-time market features  
- Simple and clean UI using Streamlit  
- Fast and lightweight REST API via FastAPI  
- Deployed on Hugging Face Spaces for live access

---

## Model Details
- Algorithm: XGBoost Regressor  
- Features used: `price`, `volume`, `price_ma3`, `volatility3`, `price_pct_change`, `VPT`  
- Evaluation metrics: R², RMSE, MAE

---

## How to Use
1. Launch the app .
2. Input feature values.
3. Click **Predict**.
4. View the predicted 24h trading volume instantly.

---

## Deployment
Deployed on Hugging Face Spaces → [https://huggingface.co/spaces/AditiL/crypto-liquidity-prediction]

---

## Author
Made by **Aditi Lidbe**  
 [GitHub](https://github.com/AditiLidbe)  [LinkedIn](https://www.linkedin.com/in/aditi-lidbe-288256257/)

---
