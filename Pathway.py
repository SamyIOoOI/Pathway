import tkinter as tk
from logging import exception
from tkinter import filedialog as fd, image_types
from tkinter import Radiobutton, Button, messagebox, PhotoImage
from tkinterdnd2 import DND_FILES, TkinterDnD
import json
import os
## Functions
def sched_button():
    print("Hello World!")
def chores_button():
    print("Hello World!")
def community_button():
    print("Hello World!")
def studies_button():
    print("Hello World!")
## Below is the basic GUI
gui = TkinterDnD.Tk()
gui.title("Pathway")
gui.geometry("500x300")
gui.config(bg="PeachPuff")
gui.resizable(False,False)
image = PhotoImage(file='Pathway.png')
msg_label = tk.Label(gui, image=image, borderwidth='3', relief='solid')
msg_label.place(x='50', y='10')
scheduler = tk.Button(text='Scheduler', command=sched_button, bg='pink')
chores = tk.Button(text="Chores", command=chores_button, bg='pink')
community = tk.Button(text="Community Service", command=community_button, bg='pink')
studies = tk.Button(text="Career & Studies", command=studies_button, bg="pink")
scheduler.config(height=1, width=6)
chores.config(height=1, width=6)
community.config(height=1, width=14)
studies.config(height=1, width=18)
scheduler.place(x='60',y='180')
studies.place(x='165', y='225')
community.place(x='180', y='180')
chores.place(x='360', y='180')
tk.messagebox.showinfo("Pathway", "Welcome to pathway! Your personal project organizer!")
gui.mainloop()