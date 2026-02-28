import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from streamlit_lottie import st_lottie

st.set_page_config(page_title="AI Healthcare Dashboard", layout="wide")

# ------------------- Animation -------------------

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation = load_lottie("https://assets4.lottiefiles.com/packages/lf20_5njp3vgg.json")

st_lottie(animation, height=200)

st.title("🩺 AI Healthcare Prediction Dashboard")
st.write("Multi Disease Prediction using Machine Learning")

# ------------------- Sidebar -------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    ["Heart Disease Prediction", "Liver Disease Prediction", "AI Doctor Chatbot"]
)

# ==========================================================
# HEART DISEASE PREDICTION
# ==========================================================

if page == "Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    data = pd.read_csv("dataset/heart.csv")

    X = data.drop("target", axis=1)
    y = data["target"]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train)

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 20, 80, 40)

        sex = st.selectbox("Sex", ["Male", "Female"])
        sex = 1 if sex == "Male" else 0

        cp = st.slider("Chest Pain Type", 0, 3, 1)

        trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)

        chol = st.slider("Cholesterol", 100, 400, 200)

    with col2:

        thalach = st.slider("Max Heart Rate", 60, 220, 150)

        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)

        slope = st.slider("Slope", 0, 2, 1)

        ca = st.slider("Major Vessels", 0, 3, 0)

        thal = st.slider("Thal", 0, 3, 2)

    input_data = np.array([[age, sex, cp, trestbps, chol, 0, 0, thalach, 0, oldpeak, slope, ca, thal]])

    input_data = scaler.transform(input_data)

    if st.button("Predict Heart Disease"):

        prediction = model.predict(input_data)

        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")

        st.metric("Risk Probability", f"{probability:.2f}%")
        st.progress(int(probability))

# ==========================================================
# LIVER DISEASE PREDICTION
# ==========================================================

if page == "Liver Disease Prediction":

    st.header("🧬 Liver Disease Prediction")

    data = pd.read_csv("dataset/liver.csv")

    data["Gender"] = data["Gender"].map({"Male": 1, "Female": 0})

    data = data.dropna()

    X = data.drop("Dataset", axis=1)
    y = data["Dataset"]

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=50)

    model.fit(X_train, y_train)

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider("Age", 10, 90, 40)

        gender = st.selectbox("Gender", ["Male", "Female"])
        gender = 1 if gender == "Male" else 0

        tb = st.slider("Total Bilirubin", 0.1, 10.0, 1.0)

        db = st.slider("Direct Bilirubin", 0.1, 5.0, 0.5)

        alk = st.slider("Alkaline Phosphotase", 100, 400, 200)

    with col2:

        alt = st.slider("Alamine Aminotransferase", 10, 200, 50)

        ast = st.slider("Aspartate Aminotransferase", 10, 200, 50)

        tp = st.slider("Total Proteins", 2.0, 10.0, 6.5)

        albumin = st.slider("Albumin", 1.0, 6.0, 3.0)

        agr = st.slider("Albumin Globulin Ratio", 0.5, 2.5, 1.0)

    input_data = np.array([[age, gender, tb, db, alk, alt, ast, tp, albumin, agr]])

    input_data = scaler.transform(input_data)

    if st.button("Predict Liver Disease"):

        prediction = model.predict(input_data)

        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Liver Disease")
        else:
            st.success("✅ Low Risk of Liver Disease")

        st.metric("Risk Probability", f"{probability:.2f}%")

        st.progress(int(probability))

# ==========================================================
# AI DOCTOR CHATBOT
# ==========================================================

if page == "AI Doctor Chatbot":

    st.header("🤖 AI Doctor Chatbot")

    user_input = st.text_input("Ask a health question")

    responses = {
        "fever": "Drink fluids and rest. If fever continues consult doctor.",
        "diabetes": "Maintain healthy diet and monitor blood sugar.",
        "heart": "Exercise regularly and reduce cholesterol.",
        "liver": "Avoid alcohol and fatty foods."
    }

    if user_input:

        response = "Please consult a healthcare professional."

        for key in responses:

            if key in user_input.lower():
                response = responses[key]

        st.write(response)

st.markdown("---")
st.caption("AI Driven Intelligent Disease Prediction System")