from tkinter import *
from tkinter import filedialog


window = Tk()
my_menu = Menu(window)
window.config(menu=my_menu)


def open():
    file_path = filedialog.askopenfilename()
    print("Selected file", file_path)


file_menu = Menu(my_menu, tearoff=0)

new = Menu(my_menu, tearoff=0)
file_menu.add_command(label="New File")

openn = Menu(my_menu, tearoff=0)
file_menu.add_command(label="Open", command=open, accelerator="Ctrl+O")
# window.bind("<Control-o>", open())

save = Menu(my_menu, tearoff=0)
file_menu.add_command(label="Save")

file_menu.add_separator()

my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

sub_menu = Menu(file_menu, tearoff=0)

sub_menu = Menu(file_menu)
sub_menu.add_command(label="Color themes")
file_menu.add_cascade(label="Preferences", menu=sub_menu)
file_menu.add_command()

mainloop()

# from tkinter import *
# window = Tk()
# window.geometry('250x250')
#
# listbox = Listbox(window)
# listbox.pack(side=LEFT, fill=BOTH)
#
# scrollbar = Scrollbar(window)
# scrollbar.pack(side=RIGHT, fill=BOTH)
#
# for values in range(100):
#     listbox.insert(END, values)
#
# listbox.config(yscrollcommand=scrollbar.set)
#
# scrollbar.config(command=listbox.yview)


# enter = Label(text="Enter your task")
# enter.place(x=100, y=0)
#
# entry = Entry()
# entry.place(x=75, y=20)
#
# btn = Button(text="Submit", bg="red", fg="black")
# btn.place(x=115, y=40)
#
# text = Text(width=30, height=6)
# text.place(x=10, y=75)
#
# btn2 = Button(text="Delete Task Number")
# btn2.place(x=75, y=175)
#
# ent = Entry()
# ent.place(x=60, y=210)


# import textwrap
# import tkinter
#
#
# from tkinter import ttk
# window = tkinter.Tk()
#
# window.geometry("300x200")
#
# name = ttk.Label(text="Enter a name:")
# name.place(x=10, y=0)
# enter_name = tkinter.Entry()
# enter_name.place(x=10, y=25)
#
# number = ttk.Label(text="Choose a number:")
# number.place(x=200, y=0)
# n = tkinter.StringVar()
# sonlar = ttk.Combobox(window, width=27, textvariable=n)
# sonlar['values'] = (1,
#                     2,
#                     3,
#                     4,
#                     5,
#                     6,
#                     7,
#                     8,
#                     9,
#                     10)
# sonlar.place(x=170, y=25)
#
# disabled = tkinter.Checkbutton(text="Disabled")
# disabled.place(x=10, y=50)
#
# unchecked = tkinter.Checkbutton(text="UnChecked")
# unchecked.place(x=100, y=50)
#
# uncheckedd = tkinter.Checkbutton(text="Enabled")
# uncheckedd.place(x=190, y=50)
#
# blue = tkinter.Radiobutton(text="Blue", value=True)
# blue.place(x=10, y=75)
#
# gold =tkinter.Radiobutton(text="Gold", value=False)
# gold.place(x=100, y=75)
#
# red = tkinter.Radiobutton(text="Red", value=False)
# red.place(x=190, y=75)
#
# entry = tkinter.Entry()
# entry.place(x=10, y=150, )
#
# text = tkinter.Label(text="A multi line ScrolledText"
#                           "widget written in Python...")
# text.place(x=10, y=130)
# mainloop()
