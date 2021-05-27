import numpy as np
import covid as covid
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
"""model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')"""

@app.route('/')
def predict():

    pickle.dump(None, open('model.pkl','wb'))
    model = pickle.load(open('model.pkl','rb'))
   # int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    prediction = covid.model_predictions
    

    #output = round(prediction[0], 2)

   # return render_template('index.html', prediction_text='Sales should be $ {}'.format(prediction))
    return render_template('index.html', prediction_text = prediction)


if __name__ == "__main__":
    app.run(debug=True)