from flask import render_template, current_app as app, jsonify
import numpy
from app.forms import DiagnoseForm
import joblib
import pandas as pd


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", title='Home')


@app.route("/diagnose", methods=['GET'])
def diagnose():
    form = DiagnoseForm()
    return render_template("diagnose.html",
                           form=form,
                           title='Diagnose')


@app.route('/diagnosis', methods=['POST'])
def diagnosis():
    form = DiagnoseForm()
    if form.validate_on_submit():
        rf_model = joblib.load('app/data/rf_model.pkl')
        scaler = joblib.load('app/data/scaler.pkl')
        form_dict = form.data
        form_dict.pop('csrf_token')
        form_dict.pop('submit')
        
        print("Test1: ", str(form_dict))
        
        feature_names = ['gender', 'age', 'hypertension', 'heart_disease', 
                         'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        
        input_df = pd.DataFrame([form_dict], columns=feature_names)
        input_data = input_df.to_numpy()
        # Scale only numerical features
        std_data = scaler.transform(input_data)

        print("Transformed Data:", std_data)
        print(rf_model.predict(std_data))
        prediction = 'Positive' if rf_model.predict(std_data)[0] else 'Negative' # Convert boolean result to string
        accuracy = "{:.2f}".format(round((numpy.max(rf_model.predict_proba(input_df)) / 1), 2))
        results = {'prediction': prediction,
                   'accuracy': accuracy}
        return results

    return jsonify(data=form.errors)

