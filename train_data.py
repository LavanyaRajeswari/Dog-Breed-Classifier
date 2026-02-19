from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing import image_dataset_from_directory

app = Flask(__name__)

# 1. FIRST load dataset to get class names
print("Loading dataset for class names...")
train_data = image_dataset_from_directory(
    'dataset/train',
    image_size=(224, 224),
    batch_size=32
)
class_names = list(train_data.class_indices.keys())  # Now this works!
print(f"Classes: {class_names}")

# 2. Load your trained model
model = tf.keras.models.load_model('models/dog_breed_model.h5')  # Your trained model

@app.route('/')
def hello():
    return "Dog Breed Classifier API Ready!"

# ... rest of your routes
