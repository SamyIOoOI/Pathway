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
number_list = {}
note_list = []
current_date = ""
current_task = ""
current_number = ""
checker = ''
variation_n = ''
## Function
def update_listbox():
    listbox.delete(0, tk.END)
    for key, value in sched_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
    for key, value in chore_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
    for key, value in community_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
    for key, value in studies_list.items():
        listbox.insert(tk.END, f"{key}: {value}")
    for key, value in number_list.items():
        listbox.insert(tk.END, f"{key}:{value}")
    for a in note_list:
        listbox.insert(tk.END, f"{a}")
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
def update_listbox_numbers():
    listbox.delete(0, tk.END)
    for key, value in number_list.items():
        listbox.insert(tk.END, f"{key}:{value}")
def insert_date():
    global current_date
    current_date = date_entry.get_date()
def insert_number():
    global current_number
    current_number = number_entry.get()
def insert_task():
    global current_task
    current_task = task_entry.get()
def confirm_entry():
    global current_date, current_task, sched_list, chore_list, community_list, studies_list, number_list, current_number
    if current_date and current_task or current_number and current_task:
        key = str(current_date)
        if current_number:
            key = str(current_number)
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
        elif variation_n == "Numbers.json":
            if key in number_list:
                counter = 1
                while f"{key}_{counter}" in number_list:
                    counter += 1
                key = f"{key}_{counter}"
            number_list[key] = current_task
            update_listbox_numbers()
        current_date = ""
        current_task = ""
        current_number = ""
        task_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
def save_task(variation_n, dump_list):
    with open(variation_n, 'w') as f:
        json.dump(dump_list, f)
    tk.messagebox.showinfo("Tasks Saved", "The tasks have been saved successfully!")
def load_task(variation_n):
    global sched_list, chore_list, community_list, studies_list, note_list, number_list
    if variation_n == "Schedule.json":
        if os.path.exists('Schedule.json'):
            with open('Schedule.json', 'r') as f:
                sched_list = json.load(f)
            update_listbox_schedule()
            tk.messagebox.showinfo("Success", "The tasks have been loaded successfully!")
        else:
            tk.messagebox.showerror("Not Found", "The save file was not found in the program's directory.")
    elif variation_n == "Chores.json":
        if os.path.exists('Chores.json'):
            with open('Chores.json', 'r') as f:
                chore_list = json.load(f)
            update_listbox_chores()
            tk.messagebox.showinfo("Success", "The tasks have been loaded successfully!")
        else:
            tk.messagebox.showerror("Not Found", "The save file was not found in the program's directory.")
    elif variation_n == "Community.json":
        if os.path.exists('Community.json'):
            with open('Community.json', 'r') as f:
                community_list = json.load(f)
            update_listbox_community()
            tk.messagebox.showinfo("Success", "The tasks have been loaded successfully!")
        else:
            tk.messagebox.showerror("Not Found", "The save file was not found in the program's directory.")
    elif variation_n == "Studies.json":
        if os.path.exists('Studies.json'):
            with open('Studies.json', 'r') as f:
                studies_list = json.load(f)
            update_listbox_studies()
            tk.messagebox.showinfo("Success", "The tasks have been loaded successfully!")
    elif variation_n == "Notes.json":
        if os.path.exists('Notes.json'):
            with open('Notes.json', 'r') as f:
                note_list = json.load(f)
            update_listbox_notes()
            tk.messagebox.showinfo("Success", "The notes have been loaded successfully!")
    elif variation_n == "Numbers.json":
        with open('Numbers.json', 'r') as f:
            number_list = json.load(f)
        update_listbox_numbers()
        tk.messagebox.showinfo("Success", "The numbers have been loaded successfully!")
    else:
        tk.messagebox.showerror("Not Found", "The save file was not found in the program's directory.")
## GUI Functions
def close_all_windows():
    global sched_list, chore_list, community_list, studies_list, number_list, note_list
    for window in gui.winfo_children():
        if isinstance(window, Toplevel):
            window.destroy()
    sched_list.clear()
    chore_list.clear()
    community_list.clear()
    studies_list.clear()
    number_list.clear()
    note_list.clear()
def sched_button():
    close_all_windows()
    global listbox, date_entry, task_entry, variation_n
    tk.messagebox.showinfo("Instructions", "Welcome to Scheduler! To register a task you select a date and then type a task, then insert both of them using the buttons, then click confirm and it will be registered. Don't forget to load & save or you'll lose all your tasks!")
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
    tk.messagebox.showinfo("Instructions", "Welcome to Chores! To register a task you select a date and then type a task, then insert both of them using the buttons, then click confirm and it will be registered. Don't forget to load & save or you'll lose all your tasks!")
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
    tk.messagebox.showinfo("Instructions", "Welcome to Community Service! To register a task you select a date and then type a task, then insert both of them using the buttons, then click confirm and it will be registered. Don't forget to load & save or you'll lose all your tasks!")
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
    tk.messagebox.showinfo("Instructions", "Welcome to Career & Studies! To register a task you select a date and then type a task, then insert both of them using the buttons, then click confirm and it will be registered. Don't forget to load & save or you'll lose all your tasks!")
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
def update_listbox_notes():
    global listbox
    listbox.delete(0, tk.END)
    for note in note_list:
        listbox.insert(tk.END, note)
def confirm_note():
    global current_task, note_list, listbox
    if current_task:
        note_list.append(current_task)
        update_listbox_notes()
        current_task = ''
        task_entry.delete(0, tk.END)

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
eggs_recipe = {
    "Ingredients": [
        "2-3 Eggs"
        "Butter"
        "Salt and Black Pepper"
    ],
    "Instructions": [
        "Melt the butter in the pan.",
        "Scramble your eggs with a spoon.",
        "Pour the eggs and stir frequently.",
        "Finish it with salt and black pepper. Enjoy."
    ]
}
fries_and_sauce_recipe = {
    "Ingredients": [
        "French fries",
        "Tomatoes",
        "Pepper",
        "Cooking oil"
    ],
    "Instructions": [
        "Prepare the french fries and put it aside, sprinkle some salt and black pepper",
        "Prepare the sauce by pouring the cooking oil in a pot, then cutting the tomatoes and pepper into small pieces and cook till it has a golden yellow tint",
        "pour the sauce on the fries. Enjoy."
    ]
}
roasted_mashed_eggplant_recipe = {
    "Ingredients": [
        "Eggplant",
        "Cooking oil",
        "Tahini Sauce"
    ],
    "Instructions": [
        "Put the eggplant on the stove and light the fire until it is completely roasted, it might smell bad and burnt but that is what we want.",
        "Peel the burnt skin of the eggplant off and mash it in a bowl.",
        "mix the mashed eggplant with oil, salt and tahini sauce. Enjoy"
    ]
}
molokhia_recipe = {
    "Ingredients": [
        "Molokhia",
        "Garlic",
        "Cooking oil",
        "Chicken Soup"
    ],
    "Instructions": [
        "First, Wash the molokhia and let it dry in a clean place. Then cut it with a molokhia cutter until it is a smooth paste.",
        "Secondly, cut some garlic and put it in a mashing bowl, add some salt and kozbara.",
        "Thirdly, mash the garlic and spices in a mashing powl until it is fully crushed",
        "Put the garlic in a pot with cooking oil and heat it until it has a strong smell."
        "Heat up the chicken soup, then pour the garlic mix and then the molokhia and stir well. Let it cook for 10 minutes until it is solid green. Enjoy."

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
    elif recipe == "Scrambled Eggs":
        ingredients = eggs_recipe["Ingredients"]
        instructions = eggs_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
    elif recipe == "Fries and Sauce":
        ingredients = fries_and_sauce_recipe["Ingredients"]
        instructions = fries_and_sauce_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
    elif recipe == "Roasted & Mashed Eggplant":
        ingredients = roasted_mashed_eggplant_recipe["Ingredients"]
        instructions = roasted_mashed_eggplant_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
    elif recipe == "Molokhia":
        ingredients = molokhia_recipe["Ingredients"]
        instructions = molokhia_recipe["Instructions"]
        tk.messagebox.showinfo("Ingredients", f"{ingredients}")
        tk.messagebox.showinfo("Instructions", f"{instructions}")
def recipes():
    global opt
    close_all_windows()
    tk.messagebox.showinfo("Instructions", "Welcome to Recipe Manager! To view a recipe's ingredients and instructions, select an option from the drop down menu, then click on the confirm button!")
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("400x350")
    top.resizable(False, False)
    top.title("Recipe Manager")
    msg_label = tk.Label(top, image=recipe_image, borderwidth='3', relief='solid')
    msg_label.place(x='45', y='10')
    recipe_names = ["Fool bi Ota (Tomato Beans)", "Fool bi Basal(Onion Beans)", "Scrambled Eggs", "Fries and Sauce", "Roasted & Mashed Eggplant", "Molokhia"]
    opt = StringVar(value="Fool bi Ota (Tomato Beans)")
    recipe_drop = tk.OptionMenu(top, opt, *recipe_names)
    recipe_get_btn = tk.Button(top, text="Confirm", command=get_recipe, bg='pink', relief='solid')
    recipe_drop.config(bg='pink', relief='solid', width=20, height=1)
    recipe_drop.place(x='90', y='190')
    recipe_get_btn.place(x='150', y='230')
def overview_btn():
    close_all_windows()
    global listbox, sched_list, chore_list, community_list, studies_list, number_list, note_list
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("350x250")
    top.resizable(False, False)
    top.title("Overview")
    listbox = tk.Listbox(top)
    listbox.config(height=11, width=40, bg='pink')
    listbox.place(x='11', y='12')
    if os.path.exists('Schedule.json'):
        with open('Schedule.json', 'r') as s:
            sched_list = json.load(s)
    if os.path.exists('Chores.json'):
        with open('Chores.json', 'r') as a:
            chore_list = json.load(a)
    if os.path.exists('Community.json'):
        with open('Community.json', 'r') as m:
            community_list = json.load(m)
    if os.path.exists('Studies.json'):
        with open('Studies.json', 'r') as y:
            studies_list = json.load(y)
    if os.path.exists('Numbers.json'):
        with open('Numbers.json', 'r') as m:
            number_list = json.load(m)
    if os.path.exists('Notes.json'):
        with open('Notes.json', 'r') as o:
            note_list = json.load(o)
    update_listbox()
    tk.messagebox.showinfo("Instructions", "Here you can see all your scheduled tasks in one place, if the save files are present.")
def notes_btn():
    global current_task, task_entry, variation_n, listbox
    close_all_windows()
    variation_n = "Notes.json"
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("350x250")
    top.resizable(False, False)
    top.title("Notes")
    task_entry = tk.Entry(top, width=40, bg='light pink')
    task_entry.place(x='11', y='48')
    task_btn = tk.Button(top, text='Insert', command=insert_task, width=3, height=1, bg='pink')
    confirm_btn = tk.Button(top, text='Submit', command=confirm_note, width=3, height=1, bg='pink')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=note_list), width=3, height=1, bg='pink')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=3, height=1, bg='pink')
    save_btn.place(x='125', y='8')
    load_btn.place(x='180', y='8')
    task_btn.place(x='15', y='8')
    confirm_btn.place(x='70', y='8')
    listbox = tk.Listbox(top)
    listbox.config(height=8, width=40)
    listbox.place(x='11', y='78')
    tk.messagebox.showinfo("Instructions", "Write your note in the entry box, then click insert and submit to add it to the listbox. Click save to save it for later, and load for loading save files.")
def numbers_btn():
    global current_task, task_entry, variation_n, listbox, number_list, number_entry, listbox
    close_all_windows()
    variation_n = "Numbers.json"
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("350x250")
    top.resizable(False, False)
    top.title("Numbers")
    number_entry = tk.Entry(top, width=20, bg='light pink')
    number_entry.insert(0, "Type Number Here")
    number_entry.place(x='4', y='48')
    task_entry = tk.Entry(top, width=20, bg='light pink')
    task_entry.insert(0, "Type Note Here")
    task_entry.place(x='180', y='48')
    task_btn = tk.Button(top, text='Add Number', command=insert_number, width=8, height=1, bg='pink')
    note_num_btn = tk.Button(top, text='Add Note', command=insert_task, width=5, height=1, bg='pink')
    confirm_btn = tk.Button(top, text='Confirm', command=confirm_entry, width=4, height=1, bg='pink')
    save_btn = tk.Button(top, text='Save', command=lambda: save_task(variation_n=variation_n, dump_list=number_list), width=2, height=1, bg='pink')
    load_btn = tk.Button(top, text='Load', command=lambda: load_task(variation_n=variation_n), width=2, height=1, bg='pink')
    note_num_btn.place(x='102', y='8')
    save_btn.place(x='249', y='8')
    load_btn.place(x='296', y='8')
    task_btn.place(x='6', y='8')
    confirm_btn.place(x='185', y='8')
    listbox = tk.Listbox(top)
    listbox.config(height=8, width=40)
    listbox.place(x='11', y='78')
    tk.messagebox.showinfo("Instructions", "Write your number and note in the entry boxes, then click add number, add note and confirm to add it to the listbox. Click save to save it for later, and load for loading save files.")
def qod_btn():
    close_all_windows()
    variation_n = "Numbers.json"
    top = Toplevel(gui, bg="PeachPuff")
    top.geometry("350x250")
    top.resizable(False, False)
    top.title("Credits")
    msg_label = tk.Label(top, image=credits_image, borderwidth='3', relief='solid')
    msg_label.place(x='1', y='1')
## Basic GUI
gui = TkinterDnD.Tk()
gui.title("Pathway")
gui.geometry("500x300")
gui.config(bg="PeachPuff")
gui.resizable(False, False)
recipe_image = PhotoImage(file='recipe.png')
credits_image = PhotoImage(file='credits.png')
image = PhotoImage(file='Pathway.png')
msg_label = tk.Label(gui, image=image, borderwidth='3', relief='solid')
msg_label.place(x='50', y='10')
scheduler = tk.Button(text='Scheduler', command=sched_button, bg='pink')
chores = tk.Button(text="Chores", command=chores_button, bg='pink')
community = tk.Button(text="Community Service", command=community_button, bg='pink')
studies = tk.Button(text="Career & Studies", command=studies_button, bg="pink")
recipes = tk.Button(text="Recipe Manager", command=recipes, bg='pink')
overview = tk.Button(text="Overview", command=overview_btn, bg='maroon',fg='pink', height=1, width=5)
notes = tk.Button(text="Notes", command=notes_btn, bg='maroon', fg='pink', height=1, width=2)
number_saved = tk.Button(text="Calls", command=numbers_btn, bg='maroon', fg='pink', height=1, width=1)
qod = tk.Button(text="☺", command=qod_btn, bg='maroon', fg='pink', height=1, width=1)
scheduler.config(height=1, width=6)
chores.config(height=1, width=6)
community.config(height=1, width=14)
recipes.config(height=1, width=18)
studies.config(height=1, width=18)
scheduler.place(x='105', y='180')
studies.place(x='165', y='215')
recipes.place(x='165', y='145')
community.place(x='180', y='180')
chores.place(x='320', y='180')
overview.place(x='5', y='265')
notes.place(x='75', y='265')
number_saved.place(x='122', y='265')
qod.place(x='458', y='265')
tk.messagebox.showinfo("Pathway", "Welcome to pathway! My personal organizer!")
gui.mainloop()