import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Model
model = joblib.load("Models/house_price_model.pkl")

# Header
st.title("🏠 House Price Prediction App")

st.markdown("""
    Predict house prices using Machine Learning.
    Fill in the property details and click Predict.
    """)

st.divider()

# Layout
col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        max_value=20000,
        value=2000
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )
    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=1
    )

with col2:

    mainroad = st.selectbox(
        "Main Road Access",
        ["yes", "no"]
    )

    guestroom = st.selectbox(
        "Guest Room",
        ["yes", "no"]
    )

    basement = st.selectbox(
        "Basement",
        ["yes", "no"]
    )

    hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["yes", "no"]
    )

    airconditioning = st.selectbox(
        "Air Conditioning",
        ["yes", "no"]
    )


st.divider()

# Prediction Button

if st.button("🔮 Predict House Price"):

    input_data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "mainroad":[mainroad],
        "guestroom":[guestroom],
        "basement":[basement],
        "hotwaterheating":[hotwaterheating],
        "airconditioning":[airconditioning],
        "parking":[parking],
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated House Price: ₹ {prediction:,.0f}"
    )

    st.balloons()

st.divider()

st.caption(
    "Developed using Streamlit, Scikit-Learn and XGBoost"
)