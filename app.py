import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import dill


# Title for the web application
st.title('Student Performance Prediction App')

# Sidebar inputs for user data
gender = st.selectbox('Gender', ['male', 'female'])
race_ethnicity = st.selectbox('Race/Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
parental_level_of_education = st.selectbox('Parental Level of Education', [
    "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox('Lunch Type', ['standard', 'free/reduced'])
test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])
reading_score = st.number_input('Reading Score', min_value=0, max_value=100, value=50)
writing_score = st.number_input('Writing Score', min_value=0, max_value=100, value=50)

# Button to make predictions
if st.button('Predict'):
    # Collect user input into a data frame
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Create data frame for prediction
    pred_df = data.get_data_as_data_frame()
    st.write('Input Data:', pred_df)

    # Make predictions using the pipeline
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Display results
    st.success(f'The predicted score is: {results[0]}')
