from flask import Flask, request, jsonify
from botnoi import cv
import requests
import joblib
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/prediction')
def classifier():
    img_url = request.values['p_image_url']
    a = cv.image(img_url)
    feat = a.getmobilenet()
    modFile = 'CDmodel.mod'
    model = pickle.load(open(modFile,'rb'))
    
    #Predict classes with LinearSVC
    prediction = model.predict([feat])
    print(feat.shape)
    result = {'img_url': img_url, 'prediction': prediction[0]}
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
