# recognize_attendance.py
import cv2, os, csv, json
from datetime import datetime
from pathlib import Path

os.makedirs("data", exist_ok=True)
attendance_file = "data/attendance.csv"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if not Path("models/recognizer.yml").exists():
    print("Model not found. Run train_recognizer.py first.")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/recognizer.yml")
with open("models/labels.json") as f:
    labels = json.load(f)
labels = {int(k):v for k,v in labels.items()}

# create CSV header if missing
if not Path(attendance_file).exists():
    with open(attendance_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name","timestamp"])

cam = cv2.VideoCapture(0)
recognized_today = set()
print("Press 'q' to quit")
while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        try:
            label, confidence = recognizer.predict(roi)
        except Exception:
            continue
        name = labels.get(label, "Unknown")
        text = f"{name} ({confidence:.1f})"
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2)
        if name != "Unknown":
            today = datetime.now().strftime("%Y-%m-%d")
            key = f"{name}_{today}"
            if key not in recognized_today:
                recognized_today.add(key)
                with open(attendance_file, "a", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, datetime.now().isoformat()])
                print(f"Attendance recorded for {name}")
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
