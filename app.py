import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("flowpure_brain.h5")

st.title("FlowPure AI - Water Quality Monitoring")

# Inputs
ph = st.slider("pH", 0.0, 14.0, 7.0)
bod = st.slider("BOD", 0, 500, 50)
cod = st.slider("COD", 0, 1000, 150)
tss = st.slider("TSS", 0, 500, 100)
turbidity = st.slider("Turbidity", 0, 200, 20)
ammonia = st.slider("Ammonia", 0, 50, 5)
flow = st.slider("Flow Rate", 0, 200, 120)
temp = st.slider("Temperature", 0, 50, 30)

# Prediction
if st.button("Predict"):
    prediction = model.predict([[ph, bod, cod, tss, turbidity, ammonia, flow, temp]])
    result = np.argmax(prediction)

    if result == 0:
        st.success("Normal Water ✅")
    elif result == 1:
        st.warning("Moderate Pollution ⚠️")
    else:
        st.error("Industrial Pollution 🚨")