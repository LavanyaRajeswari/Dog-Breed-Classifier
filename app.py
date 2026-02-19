from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = "dog_breed_model.h5"
CLASS_INDEX_PATH = "class_indices.json"
IMG_SIZE = 224

# Load model
model = None

def load_model_once():
    global model
    if model is None:
        print("Loading model...")
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully!")


# Load class indices
with open(CLASS_INDEX_PATH, "r") as f:
    class_indices = json.load(f)

# Reverse dictionary (index → breed)
index_to_class = {v: k for k, v in class_indices.items()}

print("Total Breeds:", len(index_to_class))

def preprocess_image(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["POST"])
def home():
    load_model_once()

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        image = Image.open(file).convert("RGB")
        image = preprocess_image(image)

        prediction = model.predict(image)[0]

        # Top 3 predictions
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
