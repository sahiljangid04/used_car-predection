# importing flask
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

# creating an object of flask
app = Flask(__name__)

model_path = '/Users/sahil_jangid/codes/python/projects/used car /RandomForestModel.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
file_path = '/Users/sahil_jangid/codes/python/projects/used car /Cleaned Car Dataset.csv'
car = pd.read_csv(file_path)

# creating a route/entry point for our application
@app.route('/')
def index():  # ye tabhi call hoga jb koi hmare route pr hit krega
    company = sorted(car['Make'].unique())
    car_model = car[['Make', 'Model']].drop_duplicates().sort_values(by=['Make', 'Model']).to_dict(orient='records')
    year = sorted(car['Make_Year'].unique())
    fuel_type = sorted(car['Fuel_Type'].unique())
    return render_template('index.html', company=company, car_model=car_model, year=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    # For getting the values which are opted by user
    print(company, car_model, year, fuel_type, kms_driven)

    prediction = model.predict(pd.DataFrame([[company, car_model, year, fuel_type, kms_driven]], columns=['Make', 'Model', 'Make_Year', 'Fuel_Type', 'Mileage_Run']))

    # return str(np.round(prediction[0]),2)
    return str(round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)
