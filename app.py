import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load(
    "dry_bean_classifier.pkl"
)


# Page configuration
st.set_page_config(
    page_title="Dry Bean Classifier",
    page_icon="🌱",
    layout="wide"
)


st.title("🌱 Dry Bean Type Classification")

st.write(
    "Enter the physical characteristics of a dry bean "
    "to predict its type."
)


st.sidebar.header("Bean Measurements")


area = st.sidebar.number_input(
    "Area",
    min_value=0.0
)

perimeter = st.sidebar.number_input(
    "Perimeter",
    min_value=0.0
)

major_axis = st.sidebar.number_input(
    "Major Axis Length",
    min_value=0.0
)

minor_axis = st.sidebar.number_input(
    "Minor Axis Length",
    min_value=0.0
)

aspect_ratio = st.sidebar.number_input(
    "Aspect Ratio",
    min_value=0.0
)

eccentricity = st.sidebar.number_input(
    "Eccentricity",
    min_value=0.0
)

convex_area = st.sidebar.number_input(
    "Convex Area",
    min_value=0.0
)

equiv_diameter = st.sidebar.number_input(
    "Equivalent Diameter",
    min_value=0.0
)

extent = st.sidebar.number_input(
    "Extent",
    min_value=0.0
)

solidity = st.sidebar.number_input(
    "Solidity",
    min_value=0.0
)

roundness = st.sidebar.number_input(
    "Roundness",
    min_value=0.0
)

compactness = st.sidebar.number_input(
    "Compactness",
    min_value=0.0
)

shape_factor1 = st.sidebar.number_input(
    "Shape Factor 1",
    min_value=0.0
)

shape_factor2 = st.sidebar.number_input(
    "Shape Factor 2",
    min_value=0.0
)

shape_factor3 = st.sidebar.number_input(
    "Shape Factor 3",
    min_value=0.0
)

shape_factor4 = st.sidebar.number_input(
    "Shape Factor 4",
    min_value=0.0
)
input_data = pd.DataFrame({
    "Area": [area],
    "Perimeter": [perimeter],
    "MajorAxisLength": [major_axis],
    "MinorAxisLength": [minor_axis],
    "AspectRation": [aspect_ratio],
    "Eccentricity": [eccentricity],
    "ConvexArea": [convex_area],
    "EquivDiameter": [equiv_diameter],
    "Extent": [extent],
    "Solidity": [solidity],
    "roundness": [roundness],
    "Compactness": [compactness],
    "ShapeFactor1": [shape_factor1],
    "ShapeFactor2": [shape_factor2],
    "ShapeFactor3": [shape_factor3],
    "ShapeFactor4": [shape_factor4]
})
if st.button("Predict Bean Type"):

    prediction = model.predict(
        input_data
    )

    st.success(f"Predicted Bean Type: {prediction[0]}"
    )