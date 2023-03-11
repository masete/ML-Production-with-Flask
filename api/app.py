# from lib2to3.pytree import convert
from flask import Flask, request, jsonify, render_template, make_response
import pickle
import numpy as np
import json
import os

ACL_ORIGIN = 'Access-Control-Allow-Origin'

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def convert(o):
    if isinstance(o, np.generic):
        return o.item()
    raise TypeError

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route("/predict_series_A", methods=["GET", "POST"])
def predictSeriesA():

    try:
        if request.method == "POST":
            form_values = request.json
            column_names = ["Last_funding_round_raised_amount", 
                            "age_of_company",
                            "Amount_of_the_last_funding_type",
                            "Companies_Information_Level_of_Completeness",
                            "Stage_DA_Classified_Early",
                            "number_of_founders",
                            "number_of_bussiness_categories",
                            "number_of_market_countires",
                            "Female_Co_Founder",
                            "Average_time_of_rounds",
                            "number_of_investors",
                            "Sector_Information_Technology",
                            "Business_model_B2C"]

            for key in form_values:
                form_values[key] = form_values[key].strip()
            input_data = np.asarray([float(form_values[i]) for i in column_names]).reshape(1, -1)
            prediction = model.predict(input_data)

            types = { 0:"According to our data and the metrics provided, there are Low chances of the startup being success", 1:"According to our data and the metrics provided, there are High chances that the startup will be successful"}
            response = jsonify({
                "statusCode": 200,
                "status": "Prediction made",
                "result": "The are : " + types[prediction[0]]
            })
           
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        
    except:
        return json.dumps({"error":"Please Enter Valid Data"})
  

if __name__ == "__main__":
    app.run(debug=True)
