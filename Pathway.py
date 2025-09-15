import tkinter as tk
from logging import exception
from tkinter import filedialog as fd, image_types
from tkinter import Radiobutton, Button, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import json
import os
## Functions
def sched_button():
    print("Hello world")
## Below is the basic GUI
gui = TkinterDnD.Tk()
gui.title("Pathway")
gui.geometry("500x300")
tk.messagebox.showinfo("Pathway", "Welcome to pathway! Your personal project organizer!")
scheduler = tk.Button(text='Scheduler', command=sched_button)
scheduler.config(height=1, width=6)
scheduler.place(x='40',y='180')
gui.mainloop()