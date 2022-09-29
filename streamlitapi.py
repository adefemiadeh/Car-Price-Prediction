import pickle
import streamlit as st

model = pickle.load(open('C:/Users/adefe/CarPricePrediction/car_price_prediction.pkl', 'rb'))

def main():
    st.title('Car Pricing Prediction Solution')
    
    #Input Variables
    Year = st.text_input('Year')
    Kms_Driven = st.text_input('Kms_Driven')
    Owner = st.text_input('Owner')
    Fuel_Type_Diesel = st.text_input('Fuel_Type_Diesel')
    Fuel_Type_Petrol = st.text_input('Fuel_Type_Petrol')
    Seller_Type_Individual = st.text_input('Seller_Type_Individual')
    Transmission_Manual = st.text_input('Transmission_Manual')

    #Prediction Code
    if st.button('Predict'):
        makeprediction = model.predict([[Year, Kms_Driven, Owner, Fuel_Type_Diesel,
    Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(makeprediction[0],2)
        st.success('You Can Sell Your Car for: {}'. format(output))

if __name__ == '__main__':
        main()
