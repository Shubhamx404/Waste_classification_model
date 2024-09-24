# data preprocessing splitting train or test ...
Data link : https://www.kaggle.com/datasets/mostafaabla/garbage-classification
import os
import shutil
import random

# Define source and destination directories
source_dir = '/content/garbage_classification'  # Replace with your source directory
destination_dir = 'data'
train_dir = os.path.join(destination_dir, 'train')
test_dir = os.path.join(destination_dir, 'test')

# Create train and test directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Split ratio
train_ratio = 0.85

# Iterate through each class folder
for class_folder in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_folder)

    if os.path.isdir(class_path):
        # Create corresponding train/test folders
        os.makedirs(os.path.join(train_dir, class_folder), exist_ok=True)
        os.makedirs(os.path.join(test_dir, class_folder), exist_ok=True)

        # Get all images in the class folder
        images = os.listdir(class_path)
        random.shuffle(images)  # Shuffle the images for randomness

        # Split images into train and test sets
        split_index = int(len(images) * train_ratio)
        train_images = images[:split_index]
        test_images = images[split_index:]

        # Move images to respective folders
        for image in train_images:
            shutil.move(os.path.join(class_path, image), os.path.join(train_dir, class_folder, image))

        for image in test_images:
            shutil.move(os.path.join(class_path, image), os.path.join(test_dir, class_folder, image))

print("Data has been successfully split into train and test directories.")