import tkinter as tk
from logging import exception
from tkinter import filedialog as fd, image_types, ttk, Toplevel
from tkinter import Radiobutton, Button, messagebox, PhotoImage
from tkinter.ttk import Progressbar
from tkinterdnd2 import DND_FILES, TkinterDnD
import json
import os
## Global Variables
sched_list = {}
chore_list = {}
community_list = {}
studies_list = {}
## Function
def schedule():
    print("hey")
def test():
    global sched_list
    sched_list["test"] = "test"
    update_listbox()
def update_listbox():
    listbox_sched.delete(0, tk.END)
    for key, value in sched_list.items():
        listbox_sched.insert(tk.END, f"{key}: {value}")
## GUI Functions
def sched_button():
    global listbox_sched
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("300x250")
    top.title("Scheduler")
    top.resizable(False, False)
    listbox_sched = tk.Listbox(top)
    listbox_sched.config(height=10, width=20)
    listbox_sched.place(x='11', y='22')
    update_listbox()
    test_btn = tk.Button(top, text='test', command=test)
    test_btn.pack()
def chores_button():
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("300x250")
    top.title("Household Chores")
    top.resizable(False, False)
def community_button():
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("300x250")
    top.title("Community Service")
    top.resizable(False, False)
def studies_button():
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("300x250")
    top.title("Career & Studies")
    top.resizable(False, False)
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