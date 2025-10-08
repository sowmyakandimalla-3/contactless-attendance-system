# train_recognizer.py
import cv2, os, json
import numpy as np
from pathlib import Path

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

image_paths = list(Path("known_faces").glob("*.jpg"))
faces = []
labels = []
label_to_name = {}

for img_path in image_paths:
    filename = img_path.stem  # e.g. 1_Sowmya_0
    parts = filename.split("_")
    if len(parts) < 2:
        continue
    label = int(parts[0])
    name = parts[1]
    label_to_name[label] = name
    img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
    # images are already cropped by capture script
    faces.append(img)
    labels.append(label)

if len(faces) == 0:
    print("No training images found in known_faces/")
    exit()

recognizer.train(faces, np.array(labels))
os.makedirs("models", exist_ok=True)
recognizer.save("models/recognizer.yml")
with open("models/labels.json", "w") as f:
    json.dump({str(k):v for k,v in label_to_name.items()}, f)
print("Training complete. Model saved to models/recognizer.yml")
