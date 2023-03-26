from flask import Flask, redirect, url_for, request, session
from flask import render_template
import pickle
import numpy as np


churn_prediction_model_path = 'models/RandomForest.pkl'
churn_prediction_model = pickle.load(open(churn_prediction_model_path, 'rb'))

app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"


if __name__ == '__main__':
    app.run(debug=True)



@app.route("/")
def home():
    return render_template('start.html')

@app.route("/main")
def index():
    return render_template("index.html")


@ app.route('/churn-predict', methods=['POST'])
def churn_prediction():
    title = 'Churn Prediction Systen using Synthetic Data'

    if request.method == 'POST':
        customer = int(request.form['customerage'])
        gender = int(request.form['gender'])
        dependent = int(request.form['dependent'])
        education = int(request.form['education'])
        marital = int(request.form['marital'])
        income=int(request.form['income'])
        card=int(request.form['card'])
        months=int(request.form['months'])
        relationship=int(request.form['relationship'])
        monthsin=int(request.form['monthsin'])
        contacts=int(request.form['contacts'])
        credit=int(request.form['credit'])

        
        data = np.array([[customer,gender,dependent,education,marital,income,card,months,relationship,monthsin,contacts,credit]])
        my_prediction = churn_prediction_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('churn-result.html', prediction=final_prediction, title=title)

    else:

        return render_template('try-again.html', title=title)
