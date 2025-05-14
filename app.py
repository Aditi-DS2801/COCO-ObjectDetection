import streamlit as st
import torch
from PIL import Image
import os

st.title("COCO Object Detection - YOLOv5")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    results = model(image)
    results.save(save_dir='results')

    result_path = os.path.join('results', 'image0.jpg')
    if os.path.exists(result_path):
        st.image(result_path, caption="Detection Result")
