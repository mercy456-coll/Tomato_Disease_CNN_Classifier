import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

st.set_page_config(page_title="Tomato Disease Classifier", page_icon="🍅")

@st.cache_resource
def load_model_cached():
    return load_model('tomato_disease_model.h5')

model = load_model_cached()

st.title("🍅 Tomato Disease Classifier")
st.write("Upload a tomato leaf image to detect diseases")

uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    if st.button('🔍 Predict'):
    with st.spinner('Analyzing...'):
        # Preprocess image
        img = image.convert('RGB')
        img = img.resize((256, 256))
        img_array = np.array(img, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        prediction = model.predict(img_array)
        pred_value = prediction[0][0]
        
        # Display result
        st.success('✅ Prediction Complete!')
        
        if pred_value > 0.5:
            st.error('🦠 Yellow Leaf Curl Virus Detected')
            confidence = pred_value * 100
        else:
            st.success('✅ Healthy Tomato')
            confidence = (1.0 - pred_value) * 100
        
        st.write(f'Confidence: {confidence:.2f}%')
