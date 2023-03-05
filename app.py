import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template, make_response
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST", "GET"])
def predict():
    class MainClass(Resource):

        def options(self):
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add('Access-Control-Allow-Headers', "*")
            response.headers.add('Access-Control-Allow-Methods', "*")
            return response
        
        try: 
            values = request.json
            data = [val for val in values.values()]
            # int_features = [float(x) for x in request.form.values()]
            final_features = [np.array(data).reshape(1, -1)]
            prediction = model.predict(final_features)
            types = { 0: "Low chances of the startup being success", 1: "High chances that the startup will be successful "}

            response = jsonify({
                "statusCode": 200,
                "status": "Prediction made",
                "result": "The type of iris plant is: " + types[prediction[0]]
                })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        
        except Exception as error:
            return jsonify({
                "statusCode": 500,
                "status": "Could not make prediction",
                "error": str(error)
            })
        
    
    # if prediction==0:
    #     return render_template('index.html',
    #                            prediction_text='Low chances of the startup being success'.format(prediction),
    #                            )
    # else:
    #     return render_template('index.html',
    #                            prediction_text='High chances that the startup will be successful'.format(prediction),
    #                           )


if __name__ == "__main__":
    app.run(debug=True)
