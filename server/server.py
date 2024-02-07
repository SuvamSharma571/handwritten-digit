from flask import Flask, request, jsonify, render_template
import util
import tensorflow as tf
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')


@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def predict_digit():
    image_file = request.files['image']
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = cv2.imread(img_path , 0)
    img = cv2.resize(img , (28 , 28))
    image_array = 255 - img
    image_array = image_array / 255
    image_array = tf.reshape(image_array, (1, 28, 28))

    response = jsonify(str(int(util.get_prediction(image_array))))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Handwritten Digit Prediction...")
    util.load_saved_artifacts()
    app.run(debug = True)