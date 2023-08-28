# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st


# loading the saved models

vitiligo_model = pickle.load(open('D:/Programming/Project_Vitiligo_SVM_ML/trained_model.sav', 'rb'))

st.title('Predicting if the Observed Patch is Vitiligo using ML')

#getting the input data from the user
#columns for input fields

col1, col2, col3 = st.columns(3)

with col1:
    Glucose = st.text_input('Enter the Glucose levels')
    
with col2:
    BloodPressure = st.text_input('Enter the Blood Pressure')
    
with col3:
    SkinThickness = st.text_input('Enter the Skin Thickness')
    
with col1:
    BMI = st.text_input('Enter the BMI value')
    
with col2:
    HemoglobinLevels = st.text_input('Enter the Hemoglobin Levels')
    
with col3:
    StressLevels = st.text_input('Enter the Stress Levels')
    
with col1:
    Age = st.text_input('Enter the Age')


#code for prediction
vitiligo_diagnosis= ''

#creating a button for prediction

# Creating a button for prediction
if st.button('Vitiligo Test Result'):
    # Check if any of the inputs are empty
    if not Glucose or not BloodPressure or not SkinThickness or not BMI or not HemoglobinLevels or not StressLevels or not Age:
        st.warning("Please fill in all input fields.")
    else:
        vitiligo_prediction = vitiligo_model.predict([[Glucose, BloodPressure, SkinThickness, BMI, HemoglobinLevels, StressLevels, Age]])

        if vitiligo_prediction[0] == 1:
            vitiligo_diagnosis = "This person's Observed Patch is Vitiligo"
        else:
            vitiligo_diagnosis = "This person's Observed Patch is Not Vitiligo"
        
st.success(vitiligo_diagnosis)
        


