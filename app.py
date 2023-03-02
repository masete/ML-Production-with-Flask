import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST", "GET"])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    
    if prediction==0:
        return render_template('index.html',
                               prediction_text='Low chances of the startup being success'.format(prediction),
                               )
    else:
        return render_template('index.html',
                               prediction_text='High chances that the startup will be successful'.format(prediction),
                              )


if __name__ == "__main__":
    app.run(debug=True)
