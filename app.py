import os
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
root.title("Workspace Opener")
root.iconbitmap("chief.png")
root.geometry("450x300")
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=300, width=450, bg="#fafafa")
canvas.pack()

frame = tk.Frame(root, bg="#2E3348")
frame.place(relwidth=0.2, relheight=1)


root.mainloop()