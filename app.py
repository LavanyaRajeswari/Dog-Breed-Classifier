from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "dog_model.keras")
CLASS_INDEX_PATH = os.path.join(BASE_DIR, "class_indices.json")

IMG_SIZE = 224

model = None

def load_model_once():
    global model
    if model is None:
        model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_INDEX_PATH, "r") as f:
    class_indices = json.load(f)

index_to_class = {v: k for k, v in class_indices.items()}

def preprocess_image(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Dog Breed Classifier API is Running",
        "endpoint": "/predict (POST)"
    })

@app.route("/predict", methods=["POST"])
def predict():
    load_model_once()

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        image = Image.open(file).convert("RGB")
        image = preprocess_image(image)

        prediction = model.predict(image)[0]
        top_3_indices = prediction.argsort()[-3:][::-1]

        results = []
        for idx in top_3_indices:
            breed_name = index_to_class[idx].replace("_", " ").title()
            confidence = float(round(prediction[idx] * 100, 2))
            results.append({
                "breed": breed_name,
                "confidence": confidence
            })

        return jsonify({"predictions": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
