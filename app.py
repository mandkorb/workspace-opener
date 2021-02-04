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
    
    if filename not in apps and len(filename) > 6:
        apps.append(filename)
    else:
        pass

    for app in apps:
        app_path_label = tk.Label(apps_frame, text=app).pack(pady=5)
    
def run_apps():
    for app in apps:
        os.startfile(app)

def open_from_txt():
    apps_in_file = filedialog.askopenfilename(initialdir="/", title="Select FIle",
                    filetypes=(("text", "*.txt"), ("*all files", ".")))
                    
    with open(apps_in_file, "r") as f:
        for path in f:
            temp_apps = [elt.strip() for elt in path.split(',')]
            
    for item in temp_apps:
        apps.append(item)
    
    for app in apps:
        app_path_label = tk.Label(apps_frame, text=app).pack(pady=5)     

def save_to_file():
    if len(apps) != 0:
        with open("template.txt", "w") as f:
            for app in apps:
                f.write(app + ",")
            
canvas = tk.Canvas(root, width=500, height=300, bg="#2E3348").pack()

apps_frame = tk.Frame(root, bg="#fafafa")
apps_frame.place(relwidth=0.8, relheight=0.92, relx=0.175, rely=0.04)

buttons_frame = tk.Frame(root, bg="#2E3348")
buttons_frame.place(relwidth=0.17, relheight=0.95, relx=0.01, rely=0.04)

open_file = tk.Button(buttons_frame, text="Open File", padx=5, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=add_app).pack()

run_apps = tk.Button(buttons_frame, text="Run Apps", padx=4, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=run_apps).pack(pady=10)

open_saved = tk.Button(buttons_frame, text="Open .txt", padx=5.5, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=open_from_txt).pack()

save = tk.Button(buttons_frame, text="Save", padx=18, pady=5,
            fg="#2E3348", bg="#fafafa", font="helvetica 10", command=save_to_file).pack(pady=10)


root.mainloop()
