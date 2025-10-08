# Contactless Attendance System

## 🌟 Overview  
The **Contactless Attendance System** is a sustainable, technology-driven solution that automates attendance marking using **Face Recognition**.  
It utilizes **Python ** and **OpenCV ** to detect and recognize faces in real-time, recording attendance data automatically in a CSV file.  
This project promotes a **contactless and paperless** approach, reducing manual errors and improving operational efficiency in educational and organizational environments.  



## 🚀 Features  
 **Contactless Attendance** — No physical interaction needed; uses face recognition.  
 **Real-Time Detection** — Captures and recognizes faces instantly using webcam.  
 **Automatic Storage** — Saves attendance with timestamps in CSV format.  
 **Easy-to-Use GUI** — Built with Tkinter for simple user control and tracking.  
 **Lightweight System** — Runs efficiently on standard laptops (no GPU required).  



## 🧰 Tech Stack  

|  Component |  Technology |
|--------------|--------------|
| **Programming Language** | Python  |
| **Libraries** | OpenCV, NumPy, Pandas, Tkinter |
| **Storage** | CSV File (`data/attendance.csv`) 📄 |
| **IDE / Environment** | Visual Studio Code |



## 📂 Project Structure  

contactless-attendance-system/
│
├──  capture_faces.py # Captures and stores face images
├──  train_recognizer.py # Trains the face recognition model
├──  recognize_attendance.py # Detects and records attendance
├──  gui.py # Tkinter-based graphical interface
├──  requirements.txt # List of dependencies
├──  .gitignore # Ignored folders and files
│
├── 📁 known_faces/ # Stores captured face images (auto-created)
├── 📁 models/ # Stores trained model files (auto-created)
└── 📁 data/ # Stores attendance CSV files



##  How It Works  

1️⃣ **Capture Faces** — Use webcam to register new faces for recognition.  
2️⃣ **Train Model** — The system trains a recognizer based on captured data.  
3️⃣ **Recognize Faces** — During attendance, the camera identifies and marks recognized faces.  
4️⃣ **View Records** — Attendance is saved automatically in `data/attendance.csv` with timestamps.  



##  Installation & Setup  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/contactless-attendance-system.git
   cd contactless-attendance-system
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
venv\Scripts\activate   # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the GUI:

bash
Copy code
python gui.py



🎯 Output Example
When the program runs:

👤 The user’s face is detected and recognized.
✅ Attendance is marked automatically.
🕒 The timestamp is stored in a CSV file for record keeping.



🏆 Acknowledgements
 OpenCV for image processing
 Python for implementation
 Inspiration from sustainable smart-campus automation
