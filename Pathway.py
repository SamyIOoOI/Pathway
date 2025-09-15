import tkinter as tk
from logging import exception
from tkinter import filedialog as fd, image_types, ttk, Toplevel
from tkinter import Radiobutton, Button, messagebox, PhotoImage
from tkcalendar import Calendar, DateEntry
from tkinter.ttk import Progressbar
from tkinterdnd2 import DND_FILES, TkinterDnD
import json
import os
## Global Variables
sched_list = {}
chore_list = {}
community_list = {}
studies_list = {}
current_date = ""
current_task = ""
## Function
def schedule():
    print("hey")
def update_listbox():
    listbox_sched.delete(0, tk.END)
    for key, value in sched_list.items():
        listbox_sched.insert(tk.END, f"{key}: {value}")
def insert_date():
    global current_date
    current_date = date_entry.get_date()
def insert_task():
    global current_task
    current_task = task_entry.get()
def confirm_entry():
    global current_date, current_task, sched_list
    if current_date and current_task:
        key = str(current_date)
        if key in sched_list:
            counter = 1
            while f"{key}_{counter}" in sched_list:
                counter += 1
            key = f"{key}_{counter}"
        sched_list[key] = current_task
        update_listbox()
        current_date = ""
        current_task = ""
        task_entry.delete(0, tk.END)
def save_schedule():
    with open('schedule.json', 'w') as f:
        json.dump(sched_list, f)
## GUI Functions
def sched_button():
    global listbox_sched, date_entry, task_entry
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("400x350")
    top.title("Scheduler")
    top.resizable(False, False)
    date_entry = DateEntry(top)
    date_entry.place(x='11', y='22')
    task_entry = tk.Entry(top, width=20)
    task_entry.place(x='11', y='52')
    date_btn = tk.Button(top, text='Insert Date', command=insert_date)
    date_btn.place(x='180', y='22')
    task_btn = tk.Button(top, text='Insert Task', command=insert_task)
    task_btn.place(x='180', y='52')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry)
    confirm_btn.place(x='260', y='22')
    save_btn = tk.Button(top, text='Save', command=save_schedule)
    save_btn.place(x='260', y='52')
    listbox_sched = tk.Listbox(top)
    listbox_sched.config(height=10, width=40)
    listbox_sched.place(x='11', y='82')
    update_listbox()
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
gui.resizable(False, False)
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
scheduler.place(x='60', y='180')
studies.place(x='165', y='225')
community.place(x='180', y='180')
chores.place(x='360', y='180')
tk.messagebox.showinfo("Pathway", "Welcome to pathway! Your personal project organizer!")
gui.mainloop()