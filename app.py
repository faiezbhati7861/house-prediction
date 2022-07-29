import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(_name_)
model = pickle.load(open('linearregression1.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp = float(request.args.get('exp'))
    
    prediction = model.predict([[exp]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given square feet is : {}'.format(prediction))


if _name_ == "_main_":
    app.run(debug=True)
