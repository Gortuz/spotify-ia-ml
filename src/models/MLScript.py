
def Predict_Popularity(form_data):
    print("Received form data:")
    for key, value in form_data.items():
        print(f"{key}: {value}")
    
    popularity = 0.5


    print("******************\nPredicted popularity:", popularity)
    return {'popularity': popularity}

def count_uppercase_letters(s):
    return sum(1 for c in s if c.isupper())

def count_lowercase_letters(s):
    return sum(1 for c in s if c.islower())

def count_spaces(s):
    return sum(1 for c in s if c.isspace())