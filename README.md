# 🧠 COCO Object Detection using YOLOv5

This project demonstrates object detection using pretrained YOLOv5 on the COCO dataset. It supports both Jupyter notebook demos and an interactive Streamlit app.

## 🚀 Features

- Uses COCO-trained YOLOv5 model
- Inference on images with bounding boxes + labels
- Real-time web app via Streamlit
- Optional: Fine-tune on custom subset of COCO

## 🛠️ Tech Stack

Python, PyTorch, YOLOv5, COCO, Streamlit

## 📦 Setup

```bash
git clone https://github.com/Aditi-DS2801/COCO-ObjectDetection.git
cd COCO-ObjectDetection
pip install -r requirements.txt
```

## 🖼️ Run Inference

```bash
streamlit run app.py
```

## 📁 Folder Structure

- `notebooks/`: Jupyter demos for batch inference and training
- `app.py`: Streamlit web app
- `data/`: Sample images and COCO YAML
