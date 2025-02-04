from flask import Flask, jsonify, request, render_template
from src.MLScript import predict_Popularity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def getHome():
    print("hola")
    return render_template('index.html')

@app.route('/spotify-ia', methods=['POST'])
def testSongData():
    form_data = request.get_json()
    popularity = predict_Popularity(form_data)
    return jsonify(popularity)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)