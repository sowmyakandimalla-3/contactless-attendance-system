# Contactless Attendance System

## Overview
The Contactless Attendance System is a sustainable, technology-driven solution that automates attendance marking using face recognition.  
It utilizes **Python** and **OpenCV** to detect and recognize faces in real-time and record attendance data automatically in a CSV file.  
The project promotes a contactless and paperless approach, reducing manual errors and improving efficiency in educational and organizational environments.

---

## Features
- Contactless attendance marking through face recognition.
- Real-time face detection and recognition using webcam.
- Automatic CSV-based attendance storage with timestamps.
- GUI interface built with **Tkinter** for easy interaction.
- Lightweight and can run on standard hardware without GPU.

---

## Tech Stack
| Component | Technology |
|------------|-------------|
| Programming Language | Python |
| Libraries | OpenCV, NumPy, Pandas, Tkinter |
| Storage | CSV file (data/attendance.csv) |
| Development Environment | Visual Studio Code |

---

## Project Structure
contactless-attendance-system/
│
├── capture_faces.py             # Captures and stores face images
├── train_recognizer.py          # Trains the face recognition model
├── recognize_attendance.py      # Detects and records attendance
├── gui.py                       # Tkinter-based graphical interface
├── requirements.txt             # List of dependencies
├── .gitignore                   # Ignored folders and files
│
├── known_faces/                 # Stores captured face images (auto-created)
├── models/                      # Stores trained model files (auto-created)
└── data/                        # Stores attendance CSV files    

