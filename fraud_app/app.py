from flask import Flask, render_template, request
import pickle
import numpy as np

# load saved model
model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # get values from form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Fraud Claim"
    else:
        result = "Legitimate Claim"

    return render_template('index.html', prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)