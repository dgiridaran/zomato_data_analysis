import streamlit as st
import json
import os
from scripts.data_preprocessing import location_preprocess, restorent_type_preprocessing, cuisines_preprcessing
import pickle
import numpy as np


# Title of the app
st.title("Zomato price prediction for 2 person in Bangalore")

# Dropdown selection
#location dropdown options
with open('artifacts/locations.json', 'r') as json_file:
    locations = json.load(json_file)
location_options = locations['locations']

#restorent types dropdown options
with open('artifacts/restorent_types.json', 'r') as json_file:
    restorent_type_options = json.load(json_file)

#cuisine types dropdown options
with open('artifacts/cuisine_types.json', 'r') as json_file:
    cuisine_type_options = json.load(json_file)



# Inputs
location = st.selectbox("Select an location", location_options)
rating = st.slider('Rating', min_value=0.0, max_value=5.0, value=2.5, step=0.2)
restorent_types = st.multiselect('Choose restaurants types', restorent_type_options)
cuisine_types = st.multiselect('Choose cuisines', cuisine_type_options)
book_table = st.selectbox("book table", ['Yes', 'No'])
book_table_l = [1 if book_table == 'Yes' else 0]

predict = st.button('Predict approximate cost')


if predict and location and rating and (len(restorent_types) > 0) and (len(cuisine_types) > 0) and book_table:
    # write logic
    encoded_location = location_preprocess(location)[0]
    encode_restorent_types = restorent_type_preprocessing(restorent_types)
    encoded_cuisines = cuisines_preprcessing(cuisine_types)
    
    model_file_path = os.path.join('models', 'final_model_pridict_cost.pkl')
    with open(model_file_path, 'rb') as file:
        loaded_model = pickle.load(file)

    inputs_values = np.array([rating] + [encoded_location[0]] + encode_restorent_types + encoded_cuisines + book_table_l)
    # print(inputs_values)
    predicted_cost = loaded_model.predict([inputs_values])[0]
    st.write("predicted cost", predicted_cost)







