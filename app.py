import flask
from flask import Flask, request, render_template
import pickle
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.layers.experimental import preprocessing

#load the model
model = load_model('model/MH_GRU_model.h5')

#load the TextVectorization layer configuration
with open('model/vectorizer_config.pkl', 'rb') as f:
    config = pickle.load(f)

#recreate the TextVectorization layer from the config
vectorizer = preprocessing.TextVectorization.from_config(config)

#load the TextVectorization layer weights
with open('model/vectorizer_weights.pkl', 'rb') as f:
    weights = pickle.load(f)
    vectorizer.set_weights(weights)
    
app = flask.Flask(__name__, template_folder='templates')

#homepage
@app.route('/')
def home():
    return render_template('home.html')

#form page
@app.route('/form', methods=['GET'])
def form():
    
    return render_template('index.html')

#prediction page
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        #get message from the request by the html element name tag
        message = request.form['message']

        #create Ragged Tensor
        input_ragged = tf.ragged.constant([message])

        #adapt Vectorizer to Input Data
        vectorizer.adapt(input_ragged)

        #vectorization
        vect = vectorizer(input_ragged)

        #perform prediction
        my_prediction = (model.predict(vect) > 0.5).astype("int32")
    
        return render_template('predict.html', prediction=my_prediction)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
