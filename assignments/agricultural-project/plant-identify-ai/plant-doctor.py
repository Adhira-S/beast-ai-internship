# Plant Doctor AI - Python version using Teachable Machine exported model

import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model you exported from Teachable Machine
model = tf.keras.models.load_model('model.h5')
class_names = ['Healthy Plant', 'Unhealthy Plant']

def predict_plant(image_path):
    img = Image.open(image_path).resize((224, 224))  # Resize the image to match the input size of the model
    img_array = np.array(img) / 255.0                # Scale pixel values to 0-1
    img_array = np.expand_dims(img_array, axis=0)    # Add batch dimension
    predictions = model.predict(img_array)           # Run the AI
    index = np.argmax(predictions)                   # Pick the top answer
    confidence = predictions[0][index] * 100
    print(f'Prediction: {class_names[index]} with {confidence:.2f}% confidence.')

predict_plant('___.jpg') # Replace '___' with the actual image file name