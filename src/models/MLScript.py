import numpy as np
import pickle
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model

def predict_Popularity(form_data):

    song_data = get_song_data(form_data)
    
    print(song_data)

    model = get_algorithm_model(int(form_data['algorithm']))

    popularity = model.predict(np.array([song_data]))

    
    print("******************\nPredicted popularity:", popularity)
    if int(form_data['algorithm']) == 1:
        return {'popularity': popularity.tolist()[0][0]}
    else:
        return {'popularity': popularity.tolist()[0]}

def get_song_data(form_data):
    album_name_lowercase_count, album_name_uppercase_count, album_name_space_count = count_strings_charactersc(form_data['album_name'])
    track_name_lowercase_count, track_name_uppercase_count, track_name_space_count = count_strings_charactersc(form_data['track_name'])

    song_data = [
    #    '6,6,230666,0,0.676,0.461,1,-6.746,0,0.143,0.0322,1.01e-06,0.358,0.715,87.917,4,1,5,1,0,5,1,0'
        len(form_data['album_name']),
        len(form_data['track_name']),
        int(form_data['duration_ms']),
        int(form_data['explicit']),
        float(form_data['danceability']),
        float(form_data['energy']),
        int(form_data['key']),
        float(form_data['loudness']),
        int(form_data['mode']),
        float(form_data['speechiness']),
        float(form_data['acousticness']),
        float(form_data['instrumentalness']),
        float(form_data['liveness']),
        float(form_data['valence']),
        float(form_data['tempo']),
        int(form_data['time_signature']),
        int(form_data['track_genre']),
        album_name_lowercase_count,
        album_name_uppercase_count,
        album_name_space_count,
        track_name_lowercase_count,
        track_name_uppercase_count,
        track_name_space_count
    ]
    array_song_data = np.array(song_data) 

    return array_song_data

def get_algorithm_model(number):
    path = ''
    if number == 0: #lineal
        path = 'src/models/algorithms/lineal_regression.joblib'
    elif number == 1:
        path = 'src/models/algorithms/neural_network.h5'
        return load_model(path)
    elif number == 2:
        path = 'src/models/algorithms/lineal_regression.joblib'
    elif number == 3:
        path = 'src/models/algorithms/logistic_regresion.joblib'
    elif number == 4:
        path = 'src/models/algorithms/gradient_boosting.pkl'
        with open(path, 'rb') as file:
            return pickle.load(file)

    return joblib.load(path)

def count_strings_charactersc(texto):
    lowercase_count = sum(1 for c in texto if c.islower())
    uppercase_count = sum(1 for c in texto if c.isupper())
    space_count = sum(1 for c in texto if c.isspace())

    # print(lowercase_count, uppercase_count, space_count)
    return lowercase_count, uppercase_count, space_count