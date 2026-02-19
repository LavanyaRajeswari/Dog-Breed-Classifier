# 🐕 Dog Breed Classifier

 Live - https://dog-breed-classifier-ui.onrender.com/

A deep learning-powered web application that identifies dog breeds from images using transfer learning with MobileNetV2.

## 📋 Project Overview

This project uses TensorFlow/Keras with MobileNetV2 pre-trained model for transfer learning to classify dog breeds. The application includes:

- **Flask REST API** - Backend service for image prediction
- **React Frontend** - User-friendly web interface
- **Deep Learning Model** - MobileNetV2-based classifier trained on 120+ dog breeds

## 🏗️ Project Structure

```
Dog_Breed/
├── app.py                    # Flask API server
├── train_model.py            # Model training script
├── train_data.py             # Data preparation utilities
├── organize_data.py          # Dataset organization script
├── labels.csv                # Training data labels
├── class_indices.json        # Class mapping for the model
├── dog_breed_model.h5        # Trained model file
├── dataset/                  # Training dataset
│   └── train/               # Training images organized by breed
├── dog-breed-ui/           # React frontend application
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   └── App.css         # Styling
│   └── package.json        # Frontend dependencies
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Node.js 14+** (for frontend)
- **npm** or **yarn**

### Backend Setup

1. **Create and activate virtual environment:**
   
```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
```

2. **Install Python dependencies:**
   
```
bash
   pip install tensorflow flask flask-cors numpy pillow
   
```

3. **Run the Flask API:**
   
```
bash
   python app.py
   
```
   
   The API will start at `http://localhost:5000`

### Frontend Setup

1. **Navigate to the UI directory:**
   
```
bash
   cd dog-breed-ui
   
```

2. **Install dependencies:**
   
```
bash
   npm install
   # or
   yarn install
   
```

3. **Start the development server:**
   
```
bash
   npm start
   # or
   yarn start
   
```

   The application will open at `http://localhost:3000`

## 📡 API Endpoints

### Base URL
```
http://localhost:5000
```

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check - returns API status |
| `/predict` | POST | Upload an image to get breed prediction |

### Prediction Endpoint

**Request:**
```
bash
curl -X POST -F "image=@dog_image.jpg" http://localhost:5000/predict
```

**Response:**
```
json
{
  "predictions": [
    {
      "breed": "Golden Retriever",
      "confidence": 85.45
    },
    {
      "breed": "Labrador Retriever",
      "confidence": 10.23
    },
    {
      "breed": "Yellow Labrador",
      "confidence": 2.11
    }
  ]
}
```

## 🔧 Training the Model

If you want to retrain the model:

1. **Prepare your data:**
   - Place training images in `dataset/train/`
   - Organize images in subdirectories named after each breed (e.g., `dataset/train/golden_retriever/`)

2. **Run training:**
   
```
bash
   python train_model.py
   
```

3. **Model configuration (in train_model.py):**
   - `IMG_SIZE = 224` - Input image size
   - `BATCH_SIZE = 16` - Training batch size
   - `EPOCHS = 1` - Number of training epochs

## 🖼️ Using the Application

1. Open the React application in your browser
2. Click the upload button or drag & drop a dog image
3. Wait for the model to process the image
4. View the top 3 breed predictions with confidence scores

## 📊 Supported Breeds

The model supports classification for 120+ dog breeds including:
- Golden Retriever, Labrador, German Shepherd
- Poodle, Bulldog, Beagle
- And many more...

## 🛠️ Technology Stack

### Backend
- **TensorFlow** - Deep learning framework
- **Keras** - Neural network API
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **React** - UI framework
- **CSS** - Styling
- **Axios** - HTTP client (for API calls)

## 📝 Configuration

### Model Settings
- Input image size: 224x224 pixels
- Image preprocessing: Rescaling (1/255)
- Model format: HDF5 (.h5)

### API Settings
- Default port: 5000
- CORS enabled for local development

## ⚠️ Troubleshooting

### Common Issues

1. **Model not found error:**
   - Ensure `dog_model.keras` is in the project root
   - Run training to generate the model file

2. **CORS errors:**
   - The Flask app includes CORS support
   - If issues persist, check browser console

3. **Memory issues during training:**
   - Reduce `BATCH_SIZE` in `train_model.py`
   - Use GPU for training if available

4. **Frontend not connecting to API:**
   - Ensure Flask is running on port 5000
   - Check proxy configuration in `package.json`

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- MobileNetV2 pre-trained weights from ImageNet
- Dataset structure inspired by Stanford Dogs Dataset

🏆 Author

Lavanya Rajeswari
Full Stack & Machine Learning Enthusiast


