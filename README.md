# Waste_classification_model
# Waste Classification and Segregation using Deep Learning

This project implements an automated waste classification and detection system using deep learning and computer vision techniques. The objective is to classify and detect different categories of waste from images and videos to support efficient waste segregation and sustainable waste management systems.

The project explores both image classification and object detection approaches. A ResNet50-based convolutional neural network is used for waste image classification through transfer learning, while a YOLO (You Only Look Once) model is used for real-time waste detection and localization in images and videos.

The workflow includes dataset preprocessing, image normalization, train–validation splitting, model training, evaluation, and real-time inference. The preprocessing pipeline ensures consistent input formatting, while the classification model focuses on accuracy and generalization. The YOLO-based detection model enables bounding-box level identification of waste objects, making the system suitable for real-world deployment scenarios.

The repository contains Jupyter notebooks for model training and experimentation, a Python script for data preprocessing and splitting, project documentation in PDF format, and a demonstration video showcasing YOLO-based waste detection.

Key technologies used in this project include Python, TensorFlow/Keras, PyTorch-based YOLO implementation, OpenCV, NumPy, Pandas, and Matplotlib. The models leverage transfer learning to improve performance while reducing training time and computational cost.

Applications of this system include smart waste management, recycling automation, environmental monitoring, smart city infrastructure, and industrial waste segregation. Future improvements include expanding the dataset, deploying the model as a web or mobile application, integrating real-time camera input, optimizing for edge devices, and experimenting with newer detection and vision transformer models.

To run the project, clone the repository, install the required dependencies, and execute the Jupyter notebooks for either classification or detection. The ResNet50 notebook focuses on image classification, while the YOLO notebook demonstrates real-time object detection.

Repository: https://github.com/Shubhamx404/Waste_classification_model  
Author: Shubham Kumar Sharma  
License: MIT
