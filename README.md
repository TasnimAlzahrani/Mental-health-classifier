# Mental-health-classifier
a mental health classifier that can analyze user-generated text and determine the likelihood of mental health concerns. By leveraging sentiment analysis techniques and incorporating deep neural networks, we seek to create a robust and accurate classifier that can provide valuable insights and support for individuals in need.

# Features
* **Home**: The home page home.html provides an introduction to the mental health issues classifier Flask web application and its features.

* **Index**: The index page index.html allows users to input text and submit it for the model.

* **Prediction**: The prediction page predict.html displays the results of the selected NLP task. It shows the mental health classifier prediction.

# Prerequisites
Before running the NLP Flask web application, ensure that you have the following prerequisites installed:

* Python 3
* Flask (Install using pip install flask)
* Keras (Install using pip install keras==2.12.0)
* Tensorflow (Install using pip install tensorflow==2.12.0)

# Getting Started
1. Clone this repository or download the source code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the Flask web server:
```
flask run
```
Once the server is running, open a web browser and visit http://127.0.0.1:5000 to access the Flask web application.

# Project Structure
The project directory consists of the following files:

* app.py: This is the main Flask application file. It handles routing and request handling for different web pages.

* templates/home.html: The HTML template for the home page. It provides an introduction to the Flask web application and a start button.

* templates/index.html: The HTML template for the form page. It contains the user interface for inputting text and a submit button.

* templates/predict.html: The HTML template for the prediction page. It displays the prediction of the NLP model.

