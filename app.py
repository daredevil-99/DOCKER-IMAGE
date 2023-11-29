from flask import Flask, request
from waitress import serve
import pickle 

app = Flask(__name__)
pickle_in = open(r"C:\Users\Admin\Documents\docker image\classifier.pickle", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def Welcome():
    return "WELCOME ALL"

@app.route('/predict')
def predict_note_authentication():
    monthly_income_of_family = request.args.get("monthly_income_of_family")
    spend = request.args.get("spend")
    balance = request.args.get("balance")

    # Check if any parameter is missing
    if None in [monthly_income_of_family, spend, balance]:
        return "Error: Missing parameter(s). Please provide values for all parameters."

    # Convert parameters to float
    try:
        monthly_income_of_family = float(monthly_income_of_family)
        spend = float(spend)
        balance = float(balance)
    except ValueError:
        return "Error: Invalid parameter value(s). Please provide numeric values."
    # Make the prediction
    prediction = classifier.predict([[monthly_income_of_family, spend, balance]])
    return "The predicted value is " + str(prediction)


mode = 'dev'

if __name__ =='__main__':
    if mode == "dev":
        app.run(host = "0.0.0.0", port=int("5000"), debug = True)
    else: 
        serve(app, host = "0.0.0.0", port = 5000, threads =1, url_prefix = "/my_app")