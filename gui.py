# gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import subprocess
import sys
import os

# Helper to run a command (uses current Python interpreter)
def run_command(cmd, output_widget, on_done=None):
    def task():
        try:
            output_widget.configure(state="normal")
            output_widget.insert(tk.END, f"> Running: {' '.join(cmd)}\n")
            output_widget.see(tk.END)
            output_widget.update()
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            # stream output
            for line in proc.stdout:
                output_widget.insert(tk.END, line)
                output_widget.see(tk.END)
            proc.wait()
            if proc.returncode == 0:
                output_widget.insert(tk.END, f"> Finished: {' '.join(cmd)}\n\n")
            else:
                output_widget.insert(tk.END, f"> Command exited with code {proc.returncode}\n\n")
        except Exception as e:
            output_widget.insert(tk.END, f"> Error: {e}\n\n")
        finally:
            output_widget.configure(state="disabled")
            if on_done:
                on_done()
    thread = threading.Thread(target=task, daemon=True)
    thread.start()
    return thread

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        root.title("Contactless Attendance — Control Panel")
        root.geometry("720x420")

        frame = tk.Frame(root)
        frame.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(frame)
        btn_frame.pack(anchor="nw", pady=(0,8))

        self.capture_btn = tk.Button(btn_frame, text="Capture Faces", width=18, command=self.capture)
        self.capture_btn.grid(row=0, column=0, padx=6)

        self.train_btn = tk.Button(btn_frame, text="Train Recognizer", width=18, command=self.train)
        self.train_btn.grid(row=0, column=1, padx=6)

        self.recognize_btn = tk.Button(btn_frame, text="Start Attendance", width=18, command=self.recognize)
        self.recognize_btn.grid(row=0, column=2, padx=6)

        self.clear_btn = tk.Button(btn_frame, text="Clear Log", width=12, command=self.clear_log)
        self.clear_btn.grid(row=0, column=3, padx=6)

        # status / logfile area
        self.log = scrolledtext.ScrolledText(frame, state="disabled", wrap=tk.WORD)
        self.log.pack(fill=tk.BOTH, expand=True)

        # small note
        note = tk.Label(root, text="Note: Webcam windows (OpenCV) will open separately. Close them to return to GUI.")
        note.pack(side="bottom", pady=6)

    def clear_log(self):
        self.log.configure(state="normal")
        self.log.delete(1.0, tk.END)
        self.log.configure(state="disabled")

    def disable_buttons(self):
        self.capture_btn.configure(state="disabled")
        self.train_btn.configure(state="disabled")
        self.recognize_btn.configure(state="disabled")

    def enable_buttons(self):
        self.capture_btn.configure(state="normal")
        self.train_btn.configure(state="normal")
        self.recognize_btn.configure(state="normal")

    def capture(self):
        # runs capture_faces.py (opens OpenCV window)
        if not os.path.exists("capture_faces.py"):
            messagebox.showerror("File not found", "capture_faces.py not found in project folder.")
            return
        self.disable_buttons()
        cmd = [sys.executable, "capture_faces.py"]
        run_command(cmd, self.log, on_done=self.enable_buttons)

    def train(self):
        # runs train_recognizer.py
        if not os.path.exists("train_recognizer.py"):
            messagebox.showerror("File not found", "train_recognizer.py not found in project folder.")
            return
        self.disable_buttons()
        cmd = [sys.executable, "train_recognizer.py"]
        run_command(cmd, self.log, on_done=self.enable_buttons)

    def recognize(self):
        # runs recognize_attendance.py (opens OpenCV window)
        if not os.path.exists("recognize_attendance.py"):
            messagebox.showerror("File not found", "recognize_attendance.py not found in project folder.")
            return
        self.disable_buttons()
        cmd = [sys.executable, "recognize_attendance.py"]
        run_command(cmd, self.log, on_done=self.enable_buttons)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceGUI(root)
    root.mainloop()
