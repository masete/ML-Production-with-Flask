import requests

# url = "http://localhost:5000/predict"
# r = requests.post(
#     url,
#     json={
#         "Pregnancies": 6,
#         "Glucose": 148,
#         "BloodPressure": 72,
#         "SkinThickness": 35,
#         "Insulin": 0,
#         "BMI": 33.6,
#         "DiabetesPedigree": 0.625,
#         "Age": 50,
#         "Outcome": 1,
#     },
# )
# print(r.json())



url = "http://localhost:5000/predict"

r = requests.post(
    url,
    json={
        "16_Last funding round raised amount": 45000, 
        "age_of_company": 8,
        "Amount of the last funding type": 7600,
        "Companies Information, Level of Completeness": 8,
        "Stage, DA Classified_Early": 8,
        "number of founders":9,
        "number of bussiness categories":9,
        "number of market countires":56,
        "Female_Co-Founder":78,
        "Average time of rounds(days)":98,
        "Sector_Financial Services":45,
        "number of investors": 56,
        "Sector_Information Technology": 7,
        "Stage, DA Classified_Growth":90,
        "Business_model_B2C":45,
        "number of other offices":23,
        "Status_Acquired":3,
        "3_Status_Active":4,
        "Male_Co-Founder":2,
        "3_Status_Dead":5,
        "Business_model_B2B":2,
        "10_Total_Venture_Funding (Disclosed)":2,
        "Sector_Commercial & Professional Services":8,
        "2. Seed": 5,
        "Total Number of Funding Rounds": 6,
        "Total Funding todate (disclosed)":8,
        "Total Number of Venture Funding Rounds":1,
        "Total Venture funding todate (disclosed)":7,
        "Acquired":5,
        "1. Grant":1,
        "3. Early Venture":7,
        "Sector_E-Commerce & Retail":5,
        "4. Late Venture":8,
        "5. Debt Financing":9,
        "6.Private Equity":12,
        "7. Offerings":78,
        "8. Exits": 12,
        "10.2_Number of Venture Funding rounds (#)":3,
        "Stage, DA Classified_Mature":7,
       },
)
print(r.json())


