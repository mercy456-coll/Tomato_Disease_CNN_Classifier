# Tomato Disease CNN Classifier

A deep learning application for detecting tomato leaf diseases using a Convolutional Neural Network. This classifier distinguishes between healthy tomato leaves and leaves infected with Tomato Yellow Leaf Curl Virus.

## Live Application

**Cloud Deployment:** [https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/](https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/)

Access the live app to upload tomato leaf images and get instant disease predictions.

## Features

- **Binary Classification:** Healthy vs. Tomato Yellow Leaf Curl Virus
- **High Accuracy:** 100% test accuracy
- **Transfer Learning:** MobileNetV2 pre-trained architecture
- **Real-time Predictions:** Upload image → Get diagnosis with confidence score
- **User-Friendly Interface:** Built with Streamlit
- **Local & Cloud Deployment:** Run locally or access online

## Dataset

**Source:** PlantVillage Dataset

- **Total Samples:** 4,858 images
- **Training Set:** 3,887 images
- **Validation Set:** 873 images
- **Test Set:** 98 images
- **Classes:** 2 (Healthy Tomato, Yellow Leaf Curl Virus)
- **Image Size:** 256 × 256 pixels
- **Formats:** JPG, PNG

## Model Architecture

**Framework:** TensorFlow 2.15.0 with Keras

**Base Model:** MobileNetV2 (pre-trained on ImageNet)

**Custom Architecture:**
```
Input Layer (256, 256, 3)
    ↓
MobileNetV2 (Frozen Base Model)
    ↓
Global Average Pooling 2D
    ↓
Dense Layer (128 neurons, ReLU activation)
    ↓
Dropout (0.5)
    ↓
Output Layer (1 neuron, Sigmoid activation)
```

**Training Configuration:**
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Epochs: 5
- Batch Size: 32
- Data Augmentation: Rotation, zoom, horizontal flip

## Model Performance

| Metric | Score |
|--------|-------|
| **Training Accuracy** | 99.95% |
| **Validation Accuracy** | 100% |
| **Test Accuracy** | 100% |

**Test Set Confusion Matrix:**
- True Negatives (Healthy Correctly Identified): 49/49
- True Positives (Virus Correctly Identified): 49/49
- False Positives: 0
- False Negatives: 0

## How to Use

### Cloud Deployment (Recommended)

1. Visit: [https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/](https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/)
2. Click **"Browse files"** to upload a tomato leaf image
3. Select image format: JPG, PNG, or JPEG
4. Click **"🔍 Predict"** button
5. View prediction result:
   - 🦠 **Yellow Leaf Curl Virus Detected** (with confidence %)
   - ✅ **Healthy Tomato** (with confidence %)

### Local Deployment

**Prerequisites:**
- Python 3.10 or higher
- pip package manager
- Git

**Installation:**

```bash
# Clone the repository
git clone https://github.com/mercy456-coll/Tomato_Disease_CNN_V2.git
cd Tomato_Disease_CNN_V2

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Run the Application:**

```bash
streamlit run app.py
```

The application will launch in your default browser at `http://localhost:8501`

**Local Deployment Screenshot:**

A screenshot demonstrating successful local deployment is included in the repository documenting the working application with predictions and confidence scores.

## Project Structure

```
Tomato_Disease_CNN_V2/
├── app.py                      # Streamlit application code
├── tomato_disease_model.h5     # Trained model weights (HDF5 format)
├── Tomato_CNN_Model.ipynb      # Complete training notebook
├── requirements.txt            # Python package dependencies
├── README.md                   # This file
├── Local_Deployment_Screenshot # Evidence of working deployment
└── Tomato_Disease_Classifier_Report.docx
```

## Dependencies

```
tensorflow>=2.16.1
keras>=3.0.0
streamlit
numpy
pillow
scikit-learn
matplotlib
pandas
```

**Install all dependencies:**
```bash
pip install -r requirements.txt
```

## Development Challenges & Solutions

### Challenge 1: TensorFlow Installation on Streamlit Cloud
**Problem:** Dependency resolution failures during cloud deployment  
**Solution:** Optimized version pinning in requirements.txt and used compatible tensorflow/keras versions

### Challenge 2: Keras Model Serialization
**Problem:** Version incompatibility between .keras and .h5 formats  
**Solution:** Standardized on .h5 format (HDF5) for better cross-platform compatibility

### Challenge 3: Model Version Compatibility
**Problem:** Keras format compatibility issues across different Python/TensorFlow versions  
**Solution:** Tested and validated model loading across environments; switched to proven .h5 format

## Deployment Details

- **Local:** Streamlit on personal machine (http://localhost:8501)
- **Cloud:** Streamlit Cloud (https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/)
- **Model Format:** HDF5 (.h5)
- **Framework:** TensorFlow 2.15.0 with Keras API

## Future Enhancements

- Multi-class classification for additional tomato diseases
- Integration of Grad-CAM visualization for model interpretability
- Real-time camera feed support for field-based diagnosis
- Mobile application development
- Deployment to alternative cloud platforms (AWS, Google Cloud)
- Model optimization for edge devices
- Integration with agricultural IoT systems

## Team Members

| Name | Registration | GitHub Username | Contribution |
|------|--------------|-----------------|--------------|
| Inameti Mercy Etim | 23/EG/C0/003 | mercy456-coll | Model Development & Deployment |
| Roberts William | 23/EG/CO/023 | Willie-Roberts-2405 | Cloud Deployment |
| Ughanze Emmanuel Nzubechi | 23/EG/CO/133 | UghanzeNzubechi | Local Deployment|
| Umoh Ekemini Emmanuel | 23/EG/CO/123 | kemysmartz123 | Model Testing |
| Mbikan Gracious | 23/EG/CO/093 | donaldgracious45 | Local Deployment |
| Godwin Unimashi Pius | 22/EG/CO/1689 | Piusgodwin2 | Cloud Deployment|
| Essien Samuel Edem | 23/EG/C0/053 | SteveBruce7 | Project Report |

## Repository

**GitHub:** [https://github.com/mercy456-coll/Tomato_Disease_CNN_V2](https://github.com/mercy456-coll/Tomato_Disease_CNN_V2)

**Live App:** [https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/](https://tomatodiseasecnnv2-zakm57gv4jmpyze4app7tnw.streamlit.app/)

## Course Information

- **Course:** GET 324 (AI, ML and Convergent Technologies)
- **Institution:** University of Uyo
- **Department:** Computer Engineering
- **Group:** CO8 (Computer Engineering Group 8)

## Project Status

✅ **Model Training:** Complete (100% test accuracy)  
✅ **Local Deployment:** Tested and verified  
✅ **Cloud Deployment:** Live and operational  
✅ **Documentation:** Complete  
✅ **Version Control:** GitHub repository  


---


For questions or issues, please contact the development team through the GitHub repository.
