# capture_faces.py
import cv2, os
os.makedirs("known_faces", exist_ok=True)

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

user_id = input("Enter numeric user id (e.g. 1): ").strip()
user_name = input("Enter user name (no spaces, e.g. Sowmya): ").strip()
count = 0
print("Press SPACE to capture face, ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Capture Faces", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:  # ESC
        break
    elif k%256 == 32:  # SPACE
        if len(faces) == 0:
            print("No face detected, try again")
            continue
        x,y,w,h = faces[0]
        face_img = gray[y:y+h, x:x+w]
        img_name = f"known_faces/{user_id}_{user_name}_{count}.jpg"
        cv2.imwrite(img_name, face_img)
        print(f"Saved {img_name}")
        count += 1

cam.release()
cv2.destroyAllWindows()
