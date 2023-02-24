import requests

url = "http://localhost:5000/predict"
r = requests.post(
    url,
    json={
        "Pregnancies": 6,
        "Glucose": 148,
        "BloodPressure": 72,
        "SkinThickness": 35,
        "Insulin": 0,
        "BMI": 33.6,
        "DiabetesPedigree": 0.625,
        "Age": 50,
        "Outcome": 1,
    },
)
print(r.json())