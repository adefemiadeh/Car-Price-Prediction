from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {'text': 'Car Pricing Prediction Solution'}
    
@app.get('/predict')
def predict(Year: str, Kms_Driven: str, Owner: str, Fuel_Type_Diesel: str,
    Fuel_Type_Petrol: str, Seller_Type_Individual: str, Transmission_Manual:str):

    model = pickle.load(open('C:/Users/adefe/CarPricePrediction/car_price_prediction.pkl', 'rb'))
    makeprediction = model.predict([[Year, Kms_Driven, Owner, Fuel_Type_Diesel,
    Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
    output = round(makeprediction[0],2)

    return{'You Can Sell Your Car For: {}'.format(output)}

if __name__ == '__main__':
        uvicorn.run(app)
