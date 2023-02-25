import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import jsonencoder
import json

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    x = request.get_json(force=True)
    data = json.dumps(x, cls=jsonencoder.NpEncoder)
    prediction = model.predict([np.array(list(data.values()))])
    output = json.dumps(prediction[0].__dict__)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
