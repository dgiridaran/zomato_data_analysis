import pickle
import os
from pathlib import Path
import json
import numpy as np



def location_preprocess(location):
    location_encoder_path = os.path.join('.', 'models', 'location_encoder.pkl')
    print(location_encoder_path)
    with open(location_encoder_path, 'rb') as file:
        loaded_model = pickle.load(file)
    encoding = loaded_model.transform([[location]])
    return encoding


def restorent_type_preprocessing(restorent_types):
    restorents_path = os.path.join('.', 'artifacts', 'restorent_types.json')
    with open(restorents_path, 'r') as json_file:
        restorent_type_options = json.load(json_file)
    output = np.zeros(len(restorent_type_options), dtype='int64')
    indices = [np.where(np.array(restorent_type_options) == val)[0][0] for val in restorent_types]
    # print(indices)
    for ind in indices:
        output[ind] = 1
    return output.tolist()


def cuisines_preprcessing(cusines):
    cuisines_path = os.path.join('.', 'artifacts', 'cuisine_types.json')
    with open(cuisines_path, 'r') as json_file:
        cuisines_options = json.load(json_file)
    output = np.zeros(len(cuisines_options), dtype='int64')
    indices = [np.where(np.array(cuisines_options) == val)[0][0] for val in cusines]
    # print(indices)
    for ind in indices:
        output[ind] = 1
    return output.tolist()
