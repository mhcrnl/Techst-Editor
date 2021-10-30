#! /usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
import webbrowser


def techst_api(color, btn_color, font_color):

    #create main window
    root = tkinter.Tk()

    screen_width = int(root.winfo_screenwidth())
    screen_height = int(root.winfo_screenheight())

    root.title('Techst Editor')

    root.geometry("1597x831")
    root.maxsize(screen_width, screen_height)
    root.minsize(screen_width, screen_height)
    root.config(bg = "#2596be")

    #make text input box

    text = Text(root)
    text.place(height=screen_height-175, width=screen_width-5, y=80)

    #copy paste cut function

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

    #save button and function

    def save():
        files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Txt Files', '*.txt')]
        file = fd.asksaveasfile(filetypes = files, defaultextension = files)
        filetext = str(text.get(1.0, END))
        file.write(filetext)
        file.close()

    save_btn = Button(root, text = 'Save', bg="white", command = lambda : [save()])
    save_btn.place(x=10, y=20, height=50, width=100)

    #open button and function

    def open_file(text):
        file = fd.askopenfile(mode ='r', filetypes =[('All Files', '*.*'), ('Python Files', '*.py'), ('Txt Files', '*.txt')])
        content = file.read()
        text.insert(END, content)

    open_btn = Button(root, text ='Open', bg="white", command = lambda : open_file(text))
    open_btn.place(x=115, y=20, height=50, width=100)

    #zoom in and out function and button

    size = 15
    text.config(font=("Courier", size))
    def normal_size(size):
        text.config(font=("Courier", size))

    def zoom_in():
        text.config(font=("Courier", 20))

    def zoom_out():
        text.config(font=("Courier", 10))

    zoom_in_btn = Button(root, text = "+", bg="white", command = lambda : [zoom_in()])
    zoom_out_btn = Button(root, text = "-", bg="white", command = lambda : [zoom_out()])
    normal_size_btn = Button(root, text = "normal", bg="white", command = lambda : [normal_size(size)])

    zoom_in_btn.place(x=screen_width-30, y=screen_height-90, height=20, width=20)
    zoom_out_btn.place(x=screen_width-110, y=screen_height-90, height=20, width=20)
    normal_size_btn.place(x=screen_width-90, y=screen_height-90, height=20, width=60)

    #credits function and button

    def credits():
        root = tkinter.Tk()
        root.title('Techst Editor Credits')
        root.geometry("350x150+500+300")
        root.config(bg="white")
        l1 = Label(root, text = "Techst Editor", font=("Default", 15), bg="white")
        l2 = Label(root, text = "Developer: BeetJuice101", font=("Default", 15), bg="white")
        l3 = Label(root, text = "Programming Language: Python", font=("Default", 15), bg="white")
        l4 = Label(root, text = "Git Hub: ", font=("Default", 15), bg="white")
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))
        lweb = Label(root, text=r"https://github.com/BeetJuice101/Techst-Editor", fg="blue", cursor="hand2", bg="white", font=("Default", 10))
        lweb.pack()
        lweb.bind("<Button-1>", callback)

    credits_btn = Button(root, text = "credits", bg="white", font=("Default", 7), command = lambda : [credits()])
    credits_btn.place(x=0, y=screen_height-90, height=20, width=40)

    #word search function and button

    def word_search():
        root = tkinter.Tk()
        root.title('Techst Editor Word Search')
        root.geometry("350x150+500+300")
        root.config(bg="white")
        search = Label(root, text = "Online Speelcheck", font=("Default", 15), bg="white")
        search.pack()
        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))
        lweb = Label(root, text=r"https://www.reverso.net/spell-checker/english-spelling-grammar/", fg="blue", cursor="hand2", bg="white", font=("Default", 10))
        lweb.pack()
        lweb.bind("<Button-1>", callback)
        notice = Label(root, text = "Built in word search coming soon.", font=("Default", 15), bg="white")
        notice.pack()

    word_search_btn = Button(root, text = "Word Search", bg="white", font=("Default", 15), command = lambda : [word_search()])
    word_search_btn.config(font=("Default", 10))
    word_search_btn.place(x=screen_width-121, y=20, height=50, width=100)

    if color == "Z":
        pass
    if color == "green":
        root.config(bg="green")
    if color == "blue":
        root.config(bg="blue")
    if color == "black":
        root.config(bg="black")
    if color == "white":
        root.config(bg="white")
    if color == "pink":
        root.config(bg="pink")
    if color == "red":
        root.config(bg="red")
    if color == "yellow":
        root.config(bg="yellow")
    if color == "purple":
        root.config(bg="purple")
    if color == "orange":
        root.config(bg="orange")
    if color == "brown":
        root.config(bg="brown")
    if color == "grey":
        root.config(bg="grey")
    if btn_color == "Z":
        pass
    if btn_color == "green":
        save_btn.configure(bg="green", foreground="white")
        open_btn.configure(bg="green", foreground="white")
        zoom_in_btn.configure(bg="green", foreground="white")
        zoom_out_btn.configure(bg="green", foreground="white")
        normal_size_btn.configure(bg="green", foreground="white")
        credits_btn.configure(bg="green", foreground="white")
        word_search_btn.configure(bg="green", foreground="white")
    if btn_color == "blue":
        save_btn.configure(bg="blue", foreground="white")
        open_btn.configure(bg="blue", foreground="white")
        zoom_in_btn.configure(bg="blue", foreground="white")
        zoom_out_btn.configure(bg="blue", foreground="white")
        normal_size_btn.configure(bg="blue", foreground="white")
        credits_btn.configure(bg="blue", foreground="white")
        word_search_btn.configure(bg="blue", foreground="white")
    if btn_color == "black":
        save_btn.configure(bg="black", foreground="white")
        open_btn.configure(bg="black", foreground="white")
        zoom_in_btn.configure(bg="black", foreground="white")
        zoom_out_btn.configure(bg="black", foreground="white")
        normal_size_btn.configure(bg="black", foreground="white")
        credits_btn.configure(bg="black", foreground="white")
        word_search_btn.configure(bg="black", foreground="white")
    if btn_color == "white":
        save_btn.configure(bg="white", foreground="black")
        open_btn.configure(bg="white", foreground="black")
        zoom_in_btn.configure(bg="white", foreground="black")
        zoom_out_btn.configure(bg="white", foreground="black")
        normal_size_btn.configure(bg="white", foreground="black")
        credits_btn.configure(bg="white", foreground="black")
        word_search_btn.configure(bg="white", foreground="black")
    if btn_color == "pink":
        save_btn.configure(bg="pink", foreground="white")
        open_btn.configure(bg="pink", foreground="white")
        zoom_in_btn.configure(bg="pink", foreground="white")
        zoom_out_btn.configure(bg="pink", foreground="white")
        normal_size_btn.configure(bg="pink", foreground="white")
        credits_btn.configure(bg="pink", foreground="white")
        word_search_btn.configure(bg="pink", foreground="white")
    if btn_color == "red":
        save_btn.configure(bg="red", foreground="white")
        open_btn.configure(bg="red", foreground="white")
        zoom_in_btn.configure(bg="red", foreground="white")
        zoom_out_btn.configure(bg="red", foreground="white")
        normal_size_btn.configure(bg="red", foreground="white")
        credits_btn.configure(bg="red", foreground="white")
        word_search_btn.configure(bg="red", foreground="white")
    if btn_color == "yellow":
        save_btn.configure(bg="yellow", foreground="black")
        open_btn.configure(bg="yellow", foreground="black")
        zoom_in_btn.configure(bg="yellow", foreground="black")
        zoom_out_btn.configure(bg="yellow", foreground="black")
        normal_size_btn.configure(bg="yellow", foreground="black")
        credits_btn.configure(bg="yellow", foreground="black")
        word_search_btn.configure(bg="yellow", foreground="black")
    if btn_color == "purple":
        save_btn.configure(bg="purple", foreground="white")
        open_btn.configure(bg="purple", foreground="white")
        zoom_in_btn.configure(bg="purple", foreground="white")
        zoom_out_btn.configure(bg="purple", foreground="white")
        normal_size_btn.configure(bg="purple", foreground="white")
        credits_btn.configure(bg="purple", foreground="white")
        word_search_btn.configure(bg="purple", foreground="white")
    if btn_color == "orange":
        save_btn.configure(bg="orange", foreground="black")
        open_btn.configure(bg="orange", foreground="black")
        zoom_in_btn.configure(bg="orange", foreground="black")
        zoom_out_btn.configure(bg="orange", foreground="black")
        normal_size_btn.configure(bg="orange", foreground="black")
        credits_btn.configure(bg="orange", foreground="black")
        word_search_btn.configure(bg="orange", foreground="black")
    if btn_color == "brown":
        save_btn.configure(bg="brown", foreground="white")
        open_btn.configure(bg="brown", foreground="white")
        zoom_in_btn.configure(bg="brown", foreground="white")
        zoom_out_btn.configure(bg="brown", foreground="white")
        normal_size_btn.configure(bg="brown", foreground="white")
        credits_btn.configure(bg="brown", foreground="white")
        word_search_btn.configure(bg="brown", foreground="white")
    if btn_color == "grey":
        save_btn.configure(bg="grey", foreground="black")
        open_btn.configure(bg="grey", foreground="black")
        zoom_in_btn.configure(bg="grey", foreground="black")
        zoom_out_btn.configure(bg="grey", foreground="black")
        normal_size_btn.configure(bg="grey", foreground="black")
        credits_btn.configure(bg="grey", foreground="black")
        word_search_btn.configure(bg="grey", foreground="black")
    if font_color == "Z":
        pass
    if font_color == "green":
        text.config(fg="green")
    if font_color == "blue":
        text.config(fg="blue")
    if font_color == "black":
        text.config(fg="black")
    if font_color == "white":
        text.config(fg="white")
    if font_color == "pink":
        text.config(fg="pink")
    if font_color == "red":
        text.config(fg="red")
    if font_color == "yellow":
        text.config(fg="yellow")
    if font_color == "purple":
        text.config(fg="purple")
    if font_color == "orange":
        text.config(fg="orange")
    if font_color == "brown":
        text.config(fg="brown")
    if font_color == "grey":
        text.config(fg="grey")

    root.mainloop()