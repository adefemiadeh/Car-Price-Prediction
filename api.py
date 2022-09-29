from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('car_price_prediction.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to Car Pricing Solution API'

@app.route('/predict', methods = ["GET"])
def predict():
    Year = request.args.get('Year')
    Kms_Driven = request.args.get('Kms_Driven')
    Owner = request.args.get('Owner')
    Fuel_Type_Diesel = request.args.get('Fuel_Type_Diesel')
    Fuel_Type_Petrol = request.args.get('Fuel_Type_Petrol')
    Seller_Type_Individual = request.args.get('Seller_Type_Individual')
    Transmission_Manual = request.args.get('Transmission_Manual')

    makeprediction = model.predict([[Year, Kms_Driven, Owner, Fuel_Type_Diesel,
    Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
    output = round(makeprediction[0],2)

    return jsonify({'You can sell your car for': output})

if __name__ == '__main__':
    app.run(debug=True)  
