# Import library
import streamlit as st
import pickle
import numpy as np
import sklearn

# set page title and icon
st.set_page_config(page_title="Heart Disease Detection", page_icon="🫀")

# Put title and divider below it
st.title("Heart Disease Detection")
st.divider()

# make first 3 columns
col1, col2, col3 = st.columns(3)

# sex column
with col1:
    st.subheader("Gender")
    gender = st.radio("Gender", ["Female", "Male"], label_visibility="hidden")

# age column
with col2:
    st.subheader("Age")
    st.caption("Min Age: 29  \n Max Age: 77")
    patient_age = st.number_input(
        "Patient's Age", label_visibility="hidden", min_value=29, max_value=77
    )

# cp column
with col3:
    st.subheader("Chest Pain")
    chest_pain = st.radio(
        "Chest Pain",
        ["typical angina", "atypical angina", "non-anginal pain", "asymtomatic"],
        label_visibility="hidden",
    )

st.divider()

# Make second three columns
col4, col5, col6 = st.columns(3)

# thalach column
with col4:
    st.subheader("Maximum Heart Rate when exercise")
    st.caption("Min input: 88  \n Max input: 202")
    max_heart_rate = st.number_input(
        "Maximum Heart Rate when exercise",
        label_visibility="hidden",
        min_value=88,
        max_value=202,
    )

# oldpeak column
with col5:
    st.subheader("ST depression induced by exercise compare to rest")
    st.caption("Min input: 0  \n Max input: 4")
    st_segmen = st.number_input(
        "st segmen", label_visibility="hidden", step=0.1, min_value=0.0, max_value=4.0
    )

# exang column
with col6:
    st.subheader("Did Angina occur when Exercise?")
    angina_occurence = st.radio(
        "Does Angina occur when Exercise?", [False, True], label_visibility="hidden"
    )

st.divider()

# Make the last three columns
col7, col8, col9 = st.columns(3)

# slope column
with col7:
    st.subheader("Slope of ST segment on ECG")
    slope_of_st = st.radio(
        "Slope of ST segment",
        ["Downsloping", "Flat", "Upsloping"],
        label_visibility="hidden",
    )

# thal column
with col8:
    st.subheader("Thalium Scan Result")
    thalium_result = st.radio(
        "Thalium Scan Result",
        [
            "Type 1: Normal",
            "Type 2: Fixed Defect",
            "Type 3: Reversable Defect",
        ],
        label_visibility="hidden",
    )

# ca column
with col9:
    st.subheader("Amount of blood vessel visibled when flourosopi test")
    num_of_blood_vessel = st.radio(
        "blood vessel",
        ["No blood vessel", "1 blood vessel", "2 blood vessels", "3 blood vessels"],
        label_visibility="hidden",
    )
st.divider()

# Change all columns value to numeric
sex = {"Male": 1, "Female": 0}

cp = {
    "typical angina": 0,
    "atypical angina": 1,
    "non-anginal pain": 2,
    "asymtomatic": 3,
}

thalach = max_heart_rate

oldpeak = st_segmen

exang = 1 if angina_occurence else 0

slope = {"Downsloping": 0, "Flat": 1, "Upsloping": 2}

thal = {"Type 1: Normal": 0, "Type 2: Fixed Defect": 1, "Type 3: Reversable Defect": 2}

ca = {
    "No blood vessel": 0,
    "1 blood vessel": 1,
    "2 blood vessels": 2,
    "3 blood vessels": 3,
}

# Combine all features's value in array
data = (
    np.array(
        [
            patient_age,
            sex[gender],
            cp[chest_pain],
            thalach,
            exang,
            oldpeak,
            slope[slope_of_st],
            ca[num_of_blood_vessel],
            thal[thalium_result],
        ]
    )
    .reshape(-1, 1)
    .T
)

# Get machine learning model
with open("model.pkl", "rb") as file:
    loaded_model = pickle.load(file)
    prediction = loaded_model.predict(data)

# Button to predict input value
if st.button("Predict", type="primary"):
    if prediction == 1:
        st.error("There's heart problem!")
    else:
        st.success("There isn't Heart Problem")
else:
    st.header("")
