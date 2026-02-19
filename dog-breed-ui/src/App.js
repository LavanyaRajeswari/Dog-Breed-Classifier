import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handlePredict = async () => {
    if (!image) {
      alert("Please upload an image first!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
      });

      const data = await response.json();   // 🔥 IMPORTANT

      console.log("API Response:", data);

      // Take top prediction
      setResult(data.predictions[0]);

      setLoading(false);

    } catch (error) {
      console.error(error);
      alert("Prediction failed!");
      setLoading(false);
    }
  };


  return (
    <div className="container">
      <div className="card">
        <h1>🐶 Dog Breed Identifier</h1>
        <input type="file" onChange={handleUpload} />

        {preview && (
          <img src={preview} alt="Preview" className="preview-image" />
        )}

        <button onClick={handlePredict}>
          {loading ? "Predicting..." : "Predict Breed"}
        </button>

        {result && (
          <div className="result">
            🐾 Predicted Breed:
            <span>{result.breed}</span>
            <br />
            Confidence: {result.confidence}%
          </div>
        )}

      </div>
    </div>
  );
}

export default App;
