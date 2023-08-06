from flask import Flask, render_template, redirect, request

import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def salary():
    if request.method == 'POST':
        experience = float(request.form['experience'])

        salary = str(model.predict([[experience]])[0, 0])
    
    return render_template('index.html', your_salary = salary)

if __name__ == '__main__':
    app.run(debug = True)