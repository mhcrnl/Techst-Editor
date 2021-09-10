#! /usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
root = tkinter.Tk()
root.title('Techst Editor')
root.geometry("1597x831")
root.config(bg = "white")


text = Text(root)
text.place(height=750, width=1596, y=80)


def make_menu(w):
    global the_menu
    the_menu = tkinter.Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

make_menu(root)

text.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)

def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py')]
    file = fd.asksaveasfile(filetypes = files, defaultextension = files)
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


save_btn = Button(root, text = 'Save', command = lambda : [save()])
save_btn.place(x=10, y=20, height=50, width=100)


def open_file(text):
    file = fd.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
    content = file.read()
    text.insert(END, content)


open_btn = Button(root, text ='Open', command = lambda : open_file(text))
open_btn.place(x=115, y=20, height=50, width=100)

def dark_mode():
    light_mode_btn = Button(root, text = "Light Mode", command = lambda : [light_mode_btn.place_forget(), dark_mode_btn.place(x=1475, y=20, height=50, width=90), run_light()])
    light_mode_btn.place(x=1475, y=20, height=50, width=90)

def run_dark():
    root.config(bg="black")
    text.config(bg="black", foreground="white")

def run_light():
    root.config(bg="white")
    text.config(bg="white", foreground="black")

dark_mode_btn = Button(root, text = "Dark Mode", command = lambda : [dark_mode_btn.place_forget(), dark_mode(), run_dark()])
dark_mode_btn.place(x=1475, y=20, height=50, width=90)

root.mainloop()