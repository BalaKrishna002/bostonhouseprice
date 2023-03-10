# import pickle
import joblib
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=joblib.load(open('model.pkl','rb'))
scaler = joblib.load(open('scaling.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        print(data)
    except ValueError:
        return render_template('home.html',status=-1)

    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=round(regmodel.predict(final_input)[0],3)
    return render_template('success.html',title="House price:",text=output)

if __name__=="__main__":
    app.run(debug=True)
