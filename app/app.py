import argparse

import flask
from flask import Flask, jsonify, request
import requests

from utils import load_model, load_tokenizer, encode_text, predict
from transformers import AutoTokenizer

app = Flask(__name__)

Model, config_file = load_model("../src/Baseline_model/state_dict.pt", "../src/Baseline_model/config_model.json") # argparse
tokenizer = load_tokenizer()

@app.route('/predict', methods = ['POST'])
def api_sentiment():
    data = request.get_json(force = True)

    encoded = encode_text(data['text'], tokenizer, config_file)

    prediction = predict(Model, encoded)

    request_responses = {
        "Negative Score" : str(prediction[0][0]),
        "Positive Score" : str(prediction[0][1])
    }

    return jsonify(request_responses)

if __name__ == "__main__":
    app.run(debug=True)
    