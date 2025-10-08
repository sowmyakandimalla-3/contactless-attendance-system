#  Contactless Attendance System

## 🌟 Overview  
The **Contactless Attendance System** is a sustainable, technology-driven solution that automates attendance marking using **Face Recognition**.  
Built with **Python **, **OpenCV **, and **Tkinter **, this project detects and recognizes faces in real-time, automatically logging attendance in a CSV file.  

It promotes a **paperless and hygienic** approach by eliminating manual attendance and reducing physical contact — ideal for schools, colleges, and organizations.  

---

## 🚀 Features  
 **Contactless Attendance** — No manual signing or touching devices.  
 **Real-Time Face Recognition** — Uses webcam input for detection & recognition.  
 **Automatic Record Storage** — Saves attendance with timestamps in CSV format.  
 **Graphical Interface (GUI)** — User-friendly control using Tkinter.  
 **Lightweight & Fast** — Works even without GPU acceleration.  

---

## 🧰 Tech Stack  

| Component |  Technology Used |
|--------------|------------------|
| **Programming Language** | Python  |
| **Libraries** | OpenCV, NumPy, Pandas, Tkinter |
| **Storage** | CSV File (`data/attendance.csv`) |
| **Development Environment** | Visual Studio Code  |

---

## 📂 Project Structure  

contactless-attendance-system/
│
├──  capture_faces.py # Captures and stores new face images
├──  train_recognizer.py # Trains face recognition model using OpenCV
├──  recognize_attendance.py # Recognizes and marks attendance
├──  gui.py # Tkinter GUI interface
├──  requirements.txt # Python dependencies
├──  .gitignore # Ignored files and folders
│
├── 📁 known_faces/ # Stores captured face images
├── 📁 models/ # Stores trained model data
└── 📁 data/ # Stores attendance CSV files



---

##  How It Works  

1️⃣ **Capture Faces**  
   - Run `capture_faces.py`  
   - The webcam opens and captures images for each user.  

2️⃣ **Train the Model**  
   - Run `train_recognizer.py`  
   - Trains an OpenCV LBPH model on captured face data.  

3️⃣ **Recognize Attendance**  
   - Run `recognize_attendance.py`  
   - Recognizes faces in real-time and logs attendance automatically.  

4️⃣ **Control via GUI**  
   - Run `gui.py` for a single interface to control capture, training, and recognition.  

---

##  Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/contactless-attendance-system.git
cd contactless-attendance-system
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
3️⃣ Activate the environment
bash
Copy code
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate   # For Linux/Mac
4️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
5️⃣ Run the GUI
bash
Copy code
python gui.py


---

🎯 Output Examples
-> GUI Interface
User-friendly control panel to capture, train, and recognize faces.

-> Face Recognition in Action
Real-time webcam recognition marking attendance automatically.

-> Attendance Record Generated
Attendance saved with name, ID, and timestamp in CSV format.


🏆 Acknowledgements
 OpenCV — for computer vision and face recognition.

 Python — for simplicity and rapid development.

 Inspired by sustainable smart campus automation projects.
