# face_recognition.py
import os
import cv2
from deepface import DeepFace

def match_faces(image):
    reference_images_directory = "path_to_your_reference_images_directory"
    reference_images, reference_image_names = load_reference_images(reference_images_directory)
    
    frame = cv2.imdecode(image.read(), cv2.IMREAD_COLOR)
    matched_names = []
    
    if frame is not None:
        for reference_img, reference_name in zip(reference_images, reference_image_names):
            if DeepFace.verify(frame, reference_img.copy(), model_name='Facenet', enforce_detection=False)['verified']:
                matched_names.append(reference_name)
        return matched_names
    else:
        return []

def load_reference_images(directory):
    reference_images = []
    reference_image_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".webp") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            img_path = os.path.join(directory, filename)
            reference_images.append(cv2.imread(img_path))
            reference_image_names.append(os.path.splitext(filename)[0])  # Store the name without extension
    return reference_images, reference_image_names
