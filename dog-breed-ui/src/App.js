import React, { useState } from "react";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => {
    if (!e.target.files || e.target.files.length === 0) return;

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

      const response = await fetch("https://dog-breed-classifier-31cr.onrender.com/predict", {
        method: "POST",
        body: formData
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Server Error:", errorText);
        alert("Server error occurred.");
        setLoading(false);
        return;
      }

      const data = await response.json();
      console.log("API Response:", data);

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
