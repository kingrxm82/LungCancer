from flask import Flask,render_template,request
import numpy as np
import pickle

model = pickle.load(open('./model/model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction/result',methods=['POST'])
def predictionResult():
    data1=request.form.get('yellowfingers',type=int)
    data2=request.form.get('anxiety',type=int)
    data3=request.form.get('peerpressure',type=int)
    data4=request.form.get('chronicdisease',type=int)
    data5=request.form.get('fatigue',type=int)
    data6=request.form.get('allergy',type=int)
    data7=request.form.get('wheezing',type=int)
    data8=request.form.get('alchoholconsuming',type=int)
    data9=request.form.get('coughting',type=int)
    data10=request.form.get('swallowingdifficulty',type=int)
    data11=request.form.get('chestpain',type=int)
    data12=request.form.get('anixyelfin',type=int)
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12]])
    pred = model.predict(arr)
    return render_template('result.html',data=pred)

if __name__ == "__main__":
    app.run(debug=True)