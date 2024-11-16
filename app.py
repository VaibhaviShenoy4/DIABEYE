from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from keras.preprocessing import image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your model once when the app starts
import tensorflow as tf
from tensorflow.keras.layers import Conv2D

custom_objects = {"Conv2D": Conv2D}
loaded_model = tf.keras.models.load_model(r"C:\Users\HP\Downloads\DiabEye\modelmobile\DenseModel.h5", custom_objects=custom_objects)

# loaded_model = tf.keras.models.load_model(r"C:\Users\HP\Downloads\DiabEye\modelmobile\DenseModel.h5")

# Define image parameters
img_width, img_height = 224, 224
batch_size = 32

# Create test data generator
test_datagen = ImageDataGenerator(rescale=1./255)

# Directory for test images
test_dir = r'C:\Users\HP\Downloads\DiabEye\ddata\test'

# Get class labels from the generator
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='sparse',  # Use 'sparse' for integer-encoded labels
    shuffle=False
)
class_labels = list(test_generator.class_indices.keys())

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Load and preprocess the image
    img_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)  # Ensure the uploads directory exists
    file.save(img_path)

    img = image.load_img(img_path, target_size=(img_width, img_height))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to create a batch with a single image
    img_array /= 255.  # Normalize the pixel values

    # Make prediction
    prediction = loaded_model.predict(img_array)

    # Get the predicted class
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_labels[predicted_class_index]
    confidence_level = prediction[0][predicted_class_index]

    # Return the results
    return jsonify({
        'confidence': float(confidence_level),
        'predicted_class_index': int(predicted_class_index),  # Convert to standard Python int
        'predicted_class_name': predicted_class_name
    })
    
if __name__ == '__main__':
    app.run(debug=True)
