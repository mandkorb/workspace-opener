import os
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
root.title("Workspace Opener")
root.geometry("500x300")
root.resizable(width=False, height=False)

apps = []

def add_app():
    for app in apps_frame.winfo_children():
        app.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select App",
                    filetypes=(("apps", "*.exe"), ("*all files", ".")))   
    apps.append(filename)

    for app in apps:
        app_path_label = tk.Label(apps_frame, text=app).pack(pady=5)
    
def run_apps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, width=500, height=300, bg="#2E3348").pack()

apps_frame = tk.Frame(root, bg="#fafafa")
apps_frame.place(relwidth=0.8, relheight=0.92, relx=0.175, rely=0.04)

buttons_frame = tk.Frame(root, bg="#2E3348")
buttons_frame.place(relwidth=0.17, relheight=0.95, relx=0.01, rely=0.04)

open_file = tk.Button(buttons_frame, text="Open File", padx=5, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=add_app).pack()

run_apps = tk.Button(buttons_frame, text="Run Apps", padx=4, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=run_apps).pack(pady=10)

root.mainloop()
