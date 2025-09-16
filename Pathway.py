import tkinter as tk
from dis import Instruction
from logging import exception
from tkinter import filedialog as fd, image_types, ttk, Toplevel, StringVar
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
checker = ''
variation_n = ''
## Function
def update_listbox_schedule():
    listbox.delete(0, tk.END)
    for key, value in sched_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
def update_listbox_chores():
    listbox.delete(0, tk.END)
    for key, value in chore_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
def update_listbox_community():
    listbox.delete(0, tk.END)
    for key, value in community_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
def update_listbox_studies():
    listbox.delete(0, tk.END)
    for key, value in studies_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
def insert_date():
    global current_date
    current_date = date_entry.get_date()
def insert_task():
    global current_task
    current_task = task_entry.get()
def confirm_entry():
    global current_date, current_task, sched_list, chore_list, community_list, studies_list
    if current_date and current_task:
        key = str(current_date)
        if variation_n == "Schedule.json":
            if key in sched_list:
                counter = 1
                while f"{key}_{counter}" in sched_list:
                    counter += 1
                key = f"{key}_{counter}"
            sched_list[key] = current_task
            update_listbox_schedule()
        elif variation_n == "Chores.json":
            if key in chore_list:
                counter = 1
                while f"{key}_{counter}" in chore_list:
                    counter += 1
                key = f"{key}_{counter}"
            chore_list[key] = current_task
            update_listbox_chores()
        elif variation_n == "Community.json":
            if key in community_list:
                counter = 1
                while f"{key}_{counter}" in community_list:
                    counter += 1
                key = f"{key}_{counter}"
            community_list[key] = current_task
            update_listbox_community()
        elif variation_n == "Studies.json":
            if key in studies_list:
                counter = 1
                while f"{key}_{counter}" in studies_list:
                    counter += 1
                key = f"{key}_{counter}"
            studies_list[key] = current_task
            update_listbox_studies()
        current_date = ""
        current_task = ""
        task_entry.delete(0, tk.END)
def save_task(variation_n, dump_list):
    with open(variation_n, 'w') as f:
        json.dump(dump_list, f)
    tk.messagebox.showinfo("Tasks Saved", "The tasks have been saved successfully!")
def load_task(variation_n):
    global sched_list, chore_list, community_list, studies_list
    if variation_n == "Schedule.json":
        if os.path.exists('Schedule.json'):
            with open('Schedule.json', 'r') as f:
                sched_list = json.load(f)
        update_listbox_schedule()
    elif variation_n == "Chores.json":
        if os.path.exists('Chores.json'):
            with open('Chores.json', 'r') as f:
                chore_list = json.load(f)
        update_listbox_chores()
    elif variation_n == "Community.json":
        if os.path.exists('Community.json'):
            with open('Community.json', 'r') as f:
                community_list = json.load(f)
            update_listbox_community()
    elif variation_n == "Studies.json":
        if os.path.exists('Studies.json'):
            with open('Studies.json', 'r') as f:
                studies_list = json.load(f)
            update_listbox_studies()
## GUI Functions
def close_all_windows():
    for window in gui.winfo_children():
        if isinstance(window, Toplevel):
            window.destroy()
def sched_button():
    close_all_windows()
    global listbox, date_entry, task_entry, variation_n
    variation_n = "Schedule.json"
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("400x350")
    top.title("Scheduler")
    top.resizable(False, False)
    date_entry = DateEntry(top)
    date_entry.place(x='11', y='22')
    task_entry = tk.Entry(top, width=20, bg='light pink')
    task_entry.place(x='11', y='50')
    date_btn = tk.Button(top, text='Insert Date', command=insert_date, width=6, height=1, bg='pink')
    date_btn.place(x='180', y='11')
    task_btn = tk.Button(top, text='Insert Task', command=insert_task, width=6, height=1, bg='pink')
    task_btn.place(x='180', y='49')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry, width=6, height=1, bg='pink')
    confirm_btn.place(x='260', y='11')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=sched_list), width=4, height=1, bg='pink')
    save_btn.place(x='260', y='49')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=4, height=1, bg='pink')
    load_btn.place(x='325', y='49')
    listbox = tk.Listbox(top)
    listbox.config(height=10, width=40)
    listbox.place(x='11', y='82')
    update_listbox_schedule()
def chores_button():
    close_all_windows()
    global listbox, date_entry, task_entry, variation_n
    variation_n = "Chores.json"
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("400x350")
    top.title("Household Chores")
    top.resizable(False, False)
    date_entry = DateEntry(top)
    date_entry.place(x='11', y='22')
    task_entry = tk.Entry(top, width=20, bg='light pink')
    task_entry.place(x='11', y='50')
    date_btn = tk.Button(top, text='Insert Date', command=insert_date, width=6, height=1, bg='pink')
    date_btn.place(x='180', y='11')
    task_btn = tk.Button(top, text='Insert Task', command=insert_task, width=6, height=1, bg='pink')
    task_btn.place(x='180', y='49')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry, width=6, height=1, bg='pink')
    confirm_btn.place(x='260', y='11')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=chore_list), width=4, height=1, bg='pink')
    save_btn.place(x='260', y='49')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=4, height=1, bg='pink')
    load_btn.place(x='325', y='49')
    listbox = tk.Listbox(top)
    listbox.config(height=10, width=40)
    listbox.place(x='11', y='82')
    update_listbox_chores()
def community_button():
    close_all_windows()
    global listbox, date_entry, task_entry, variation_n
    variation_n = "Community.json"
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("400x350")
    top.title("Community Service")
    top.resizable(False, False)
    date_entry = DateEntry(top)
    date_entry.place(x='11', y='22')
    task_entry = tk.Entry(top, width=20, bg='light pink')
    task_entry.place(x='11', y='50')
    date_btn = tk.Button(top, text='Insert Date', command=insert_date, width=6, height=1, bg='pink')
    date_btn.place(x='180', y='11')
    task_btn = tk.Button(top, text='Insert Task', command=insert_task, width=6, height=1, bg='pink')
    task_btn.place(x='180', y='49')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry, width=6, height=1, bg='pink')
    confirm_btn.place(x='260', y='11')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=community_list), width=4, height=1, bg='pink')
    save_btn.place(x='260', y='49')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=4, height=1, bg='pink')
    load_btn.place(x='325', y='49')
    listbox = tk.Listbox(top)
    listbox.config(height=10, width=40)
    listbox.place(x='11', y='82')
    update_listbox_community()
def studies_button():
    close_all_windows()
    global listbox, date_entry, task_entry, variation_n
    variation_n = "Studies.json"
    top = Toplevel(gui, bg='PeachPuff')
    top.geometry("400x350")
    top.title("Career & Studies")
    top.resizable(False, False)
    date_entry = DateEntry(top)
    date_entry.place(x='11', y='22')
    task_entry = tk.Entry(top, width=20, bg='light pink')
    task_entry.place(x='11', y='50')
    date_btn = tk.Button(top, text='Insert Date', command=insert_date, width=6, height=1, bg='pink')
    date_btn.place(x='180', y='11')
    task_btn = tk.Button(top, text='Insert Task', command=insert_task, width=6, height=1, bg='pink')
    task_btn.place(x='180', y='49')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry, width=6, height=1, bg='pink')
    confirm_btn.place(x='260', y='11')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=studies_list), width=4, height=1, bg='pink')
    save_btn.place(x='260', y='49')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=4, height=1, bg='pink')
    load_btn.place(x='325', y='49')
    listbox = tk.Listbox(top)
    listbox.config(height=10, width=40)
    listbox.place(x='11', y='82')
    update_listbox_studies()
## Detailed Recipes Start Here ##
tomato_beans_recipe = {
    "Ingredients": [
        "2 fresh medium-sized tomatoes",
        "2-3 hot pepper (can be mixed with sweet pepper)",
        "Cooking oil",
        "One can of fava beans"
    ],
    "Instructions": [
        "1- Cut the tomatoes and pepper into small pieces with a kitchen knife, please use it safely." ,
        "2- Pour cooking oil in any kind of steel or aluminum pot or dish and turn up the heat",
        "3- Put the tomato and pepper in the pot and stir them frequently",
        "4- When the ingredients start to have a golden or yellowish color, sprinkle some salt on it, other spices can also be used.",
        "5- After sprinkling the salt, stir the mixture for a bit then put the fava beans in the put and stir well.",
        "6- Leave it on low heat for 5 minutes. Enjoy."
    ]
}
onion_beans_recipe = {
    "Ingredients": [
        "2 fresh medium-sized tomatoes",
        "2-3 hot pepper (can be mixed with sweet pepper)",
        "2 Medium-Sized Onions",
        "Cooking oil",
        "One can of fava beans"
    ],
    "Instructions": [
        "1- Cut the tomatoes, Onion and pepper into small pieces with a kitchen knife, please use it safely." ,
        "2- Pour cooking oil in any kind of steel or aluminum pot or dish and turn up the heat",
        "3- Put the onion and stir it frequently until it is of golden color",
        "After the onion is golden yellow, put the tomatoes and pepper you cutted before",
        "4- When the ingredients start to have a golden or yellowish color, sprinkle some salt on it, other spices can also be used.",
        "5- After sprinkling the salt, stir the mixture for a bit then put the fava beans in the put and stir well.",
        "6- Leave it on low heat for 5 minutes. Enjoy."
    ]
}
## Detailed Recipes End Here ##
def get_recipe():
    recipe = opt.get()
    if recipe == "Fool bi Ota (Tomato Beans)":
        ingredients = tomato_beans_recipe["Ingredients"]
        instructions = tomato_beans_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
    elif recipe == "Fool bi Basal(Onion Beans)":
        ingredients = onion_beans_recipe["Ingredients"]
        instructions = onion_beans_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
def recipes():
    global opt
    close_all_windows()
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("400x350")
    top.resizable(False, False)
    top.title("Recipe Manager")
    msg_label = tk.Label(top, image=recipe_image, borderwidth='3', relief='solid')
    msg_label.place(x='45', y='10')
    recipe_names = ["Fool bi Ota (Tomato Beans)", "Fool bi Basal(Onion Beans)"]
    opt = StringVar(value="Fool bi Ota (Tomato Beans)")
    recipe_drop = tk.OptionMenu(top, opt, *recipe_names)
    recipe_get_btn = tk.Button(top, text="Confirm", command=get_recipe, bg='pink', relief='solid')
    recipe_drop.config(bg='pink', relief='solid', width=20, height=1)
    recipe_drop.place(x='90', y='190')
    recipe_get_btn.place(x='150', y='230')
## Basic GUI
gui = TkinterDnD.Tk()
gui.title("Pathway")
gui.geometry("500x300")
gui.config(bg="PeachPuff")
gui.resizable(False, False)
recipe_image = PhotoImage(file='recipe.png')
image = PhotoImage(file='Pathway.png')
msg_label = tk.Label(gui, image=image, borderwidth='3', relief='solid')
msg_label.place(x='50', y='10')
scheduler = tk.Button(text='Scheduler', command=sched_button, bg='pink')
chores = tk.Button(text="Chores", command=chores_button, bg='pink')
community = tk.Button(text="Community Service", command=community_button, bg='pink')
studies = tk.Button(text="Career & Studies", command=studies_button, bg="pink")
recipes = tk.Button(text="Recipe Manager", command=recipes, bg='pink')
scheduler.config(height=1, width=6)
chores.config(height=1, width=6)
community.config(height=1, width=14)
recipes.config(height=1, width=18)
studies.config(height=1, width=18)
scheduler.place(x='60', y='180')
studies.place(x='165', y='225')
recipes.place(x='165', y='135')
community.place(x='180', y='180')
chores.place(x='360', y='180')
tk.messagebox.showinfo("Pathway", "Welcome to pathway! My personal organizer!")
gui.mainloop()