from flask import Flask, jsonify, request, render_template
from config import config
from src.models.MLScript import Predict_Popularity
configuration = config['development']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getHome():
    print("hola")
    return render_template('index.html')

@app.route('/spotify-ia', methods=['POST'])
def testSongData():
    
    form_data = request.form
    popularity = Predict_Popularity(form_data)
    return jsonify(popularity)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({})

if __name__ == '__main__':
    app.run()