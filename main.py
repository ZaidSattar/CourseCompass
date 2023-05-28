import tkinter as tk
from tkinter import filedialog
from analyzePDF import analyze_pdf  # Import the analyze_pdf function from analyzePDF.py

def upload_action(event=None):
    filename = filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')])
    if filename:
        file_label.config(text=filename)
        analyze_pdf(filename)  # Call the analyze_pdf function with the filename argument


root = tk.Tk()
root.title("PDF Uploader")

# Configure root window
root.configure(bg="#282c34")  # Set background color
root.geometry("600x400")  # Set window size
root.resizable(False, False)  # Disable window resizing

# Create and configure title label
title_label = tk.Label(root, text="Course Compass", font=("Helvetica", 48, "bold"), bg="#282c34", fg="#ffffff")
title_label.pack(pady=20)

# Create and configure upload button
upload_button = tk.Button(root, text="Upload a PDF", command=upload_action, bg="#61dafb", fg="#282c34",
                          font=("Helvetica", 16), relief="solid", bd=4, width=20)
upload_button.pack(pady=30)

# Create and configure file label
file_label = tk.Label(root, text="", bg="#282c34", fg="#ffffff", font=("Helvetica", 12), wraplength=500, justify="center")
file_label.pack(pady=10)

# Create and configure separator line
separator = tk.Frame(root, height=2, width=500, bg="#61dafb")
separator.pack(pady=20)

# Create and configure progress bar
progress_bar = tk.Canvas(root, width=400, height=10, bg="#282c34", highlightthickness=0)
progress_bar.create_rectangle(0, 0, 0, 10, fill="#61dafb", width=0)
progress_bar.pack(pady=10)

# Create and configure progress label
progress_label = tk.Label(root, text="0%", font=("Helvetica", 12), bg="#282c34", fg="#ffffff")
progress_label.pack(pady=5)

# Create and configure footer label

# Set hover effect for the upload button
upload_button.bind("<Enter>", lambda e: upload_button.config(bg="#0184cd", fg="#ffffff"))
upload_button.bind("<Leave>", lambda e: upload_button.config(bg="#61dafb", fg="#282c34"))

root.mainloop()
