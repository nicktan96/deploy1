from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np


app = Flask(__name__)

model=pickle.load(open('genModel.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("heart_prediction.html")

@app.route('/predict',methods=['POST'])
def predict():
    # For age
    data1 = request.form['age']
    if data1 == "":
        data1 = 40
    else:
        data1 = request.form['age']
    # For gender
    data2 = request.form['gender']
    if data2 =="m" or data2 == "M":
        data2 = 0
    else:
        data2 = 1
        print(data2)
    # For chest pain
    data3 = request.form['chestpain']
    if data3 == "":
        data3 = 0
    else:
        data3 = request.form['chestpain']

    # For Resting Blood pressure
    data4 = request.form['bps']
    if data4 == "":
        data4 = 100
    else:
        data4 = request.form['bps']

    # For Cholesterol
    data5 = request.form['chol']
    if data5 == "":
        data5 = 200
    else:
        data5 = request.form['chol']

    # For Fasting Blood pressure
    data6 = request.form['fbp']
    if data6 == "":
        data6 = 0
    else:
        data6 = request.form['fbp']

    # For Resting ECG
    data7 = request.form['ecg']
    if data7 == "":
        data7 = 0
    else:
        data7 = request.form['ecg']

    # For Maximum heart rate
    data8 = request.form['max']
    if data8 == "":
        data8 = 170
    else:
        data8 = request.form['max']

    # For exercise induced angina
    data9 = request.form['ang']
    if data9 == "":
        data9 = 0
    else:
        data9 = request.form['ang']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9]])
    prediction = model.predict(arr)

    output = prediction

    if output == 1:
        return render_template('heart_prediction.html', pred='High Risk of Heart Disease'.format(output))

    else:
        return render_template('heart_prediction.html', pred='Low Risk of Heart Disease '.format(output))


if __name__ == '__main__':
    app.run(debug=True)