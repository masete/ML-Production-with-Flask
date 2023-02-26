import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import jsonencoder
import json

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST", "GET"])
def predict():
    # data = request.get_json(force=True)
    # data = json.dumps(x, cls=jsonencoder.NpEncoder)
    # prediction = model.predict([np.array(list(data.values()))])
    # output = prediction[0]
    # return jsonify(output)

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

if __name__ == "__main__":
    app.run(debug=True)
