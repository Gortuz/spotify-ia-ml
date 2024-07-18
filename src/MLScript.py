import numpy as np
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model

def predict_Popularity(form_data):

    song_data = get_song_data(form_data)

    model, scaler = get_algorithm_model(int(form_data['algorithm']))

    song_data = np.array(song_data).reshape(1, -1)
    song_data = scaler.transform(song_data)
    
    popularity = model.predict(song_data)

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
        form_data['duration_ms'],
        form_data['explicit'],
        form_data['danceability'],
        form_data['energy'],
        form_data['key'],
        form_data['loudness'],
        form_data['mode'],
        form_data['speechiness'],
        form_data['acousticness'],
        form_data['instrumentalness'],
        form_data['liveness'],
        form_data['valence'],
        form_data['tempo'],
        form_data['time_signature'],
        form_data['track_genre'],
        album_name_lowercase_count,
        album_name_uppercase_count,
        album_name_space_count,
        track_name_lowercase_count,
        track_name_uppercase_count,
        track_name_space_count
    ]
    return song_data

def get_algorithm_model(number):
    path = '/var/www/spotify-ia-ml/src/algorithms/'
    scaler = 'scaler.joblib'
    if number == 0: #lineal
        path += 'gradient_boosting/'
        file = 'gradient_boosting.joblib'

    elif number == 1:
        path += 'neural_network/'
        file = 'neural_network.h5'
        return load_model(path+file), joblib.load(path+scaler)
    
    elif number == 2:
        path += 'linear_regression_fl/'
        file = 'linear_regression_fl.joblib'

    return joblib.load(path+file), joblib.load(path+scaler)

def count_strings_charactersc(texto):
    lowercase_count = sum(1 for c in texto if c.islower())
    uppercase_count = sum(1 for c in texto if c.isupper())
    space_count = sum(1 for c in texto if c.isspace())

    print(lowercase_count, uppercase_count, space_count)
    return lowercase_count, uppercase_count, space_count