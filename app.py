import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np




# Page configuration
st.set_page_config(page_title="Tomato Disease Classifier", page_icon="🍅")

# Cache model so it doesn't reload
@st.cache_resource
def load_model_cached():
    # Load model from GitHub raw content
    url = "https://github.com/mercy456-coll/Tomato_Disease_CNN_Classifier/raw/main/tomato_disease_model.keras"
    urllib.request.urlretrieve(url, "tomato_disease_model.keras")
    return load_model('tomato_disease_model.keras')

# Load model
model = load_model_cached()

# Title and description
st.title("🍅 Tomato Disease Classifier")
st.write("Upload a tomato leaf image to detect if it's healthy or has Yellow Leaf Curl Virus")

# File uploader
uploaded_file = st.file_uploader("Choose an image (JPG, PNG, JPEG)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Predict button
    if st.button('🔍 Predict', type='primary'):
        with st.spinner('Analyzing image...'):
            # Preprocess image (match training: rescale to 0-1, resize to 256x256)
            img = image.convert('RGB')
            img = img.resize((256, 256))
            img_array = np.array(img, dtype=np.float32) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            # Make prediction
            prediction = model.predict(img_array)
            
            # Display result
            st.success('✅ Prediction Complete!')
            
            if prediction[0] > 0.5:
                st.error('🦠 Yellow Leaf Curl Virus Detected')
                st.write(f'Confidence: {float(prediction[0]) * 100:.2f}%')
            else:
                st.success('✅ Healthy Tomato')
                st.write(f'Confidence: {(1-prediction[0])*100:.2f}%')
