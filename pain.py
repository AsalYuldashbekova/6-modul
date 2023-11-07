# from tkinter import *
# from tkinter.colorchooser import askcolor
#
#
# class Paint(object):
#
#     DEFAULT_PEN_SIZE = 5.0
#     DEFAULT_COLOR = 'black'
#
#     def __init__(self):
#         self.root = Tk()
#
#         self.pen_button = Button(self.root, text='pen', command=self.use_pen)
#         self.pen_button.grid(row=0, column=0)
#
#         self.brush_button = Button(self.root, text='brush', command=self.use_brush)
#         self.brush_button.grid(row=0, column=1)
#
#         self.color_button = Button(self.root, text='color', command=self.choose_color)
#         self.color_button.grid(row=0, column=2)
#
#         self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
#         self.eraser_button.grid(row=0, column=3)
#
#         self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
#         self.choose_size_button.grid(row=0, column=4)
#
#         self.c = Canvas(self.root, bg='white', width=600, height=600)
#         self.c.grid(row=1, columnspan=5)
#
#         self.setup()
#         self.root.mainloop()
#
#     def setup(self):
#         self.old_x = None
#         self.old_y = None
#         self.line_width = self.choose_size_button.get()
#         self.color = self.DEFAULT_COLOR
#         self.eraser_on = False
#         self.active_button = self.pen_button
#         self.c.bind('<B1-Motion>', self.paint)
#         self.c.bind('<ButtonRelease-1>', self.reset)
#
#     def use_pen(self):
#         self.activate_button(self.pen_button)
#
#     def use_brush(self):
#         self.activate_button(self.brush_button)
#
#     def choose_color(self):
#         self.eraser_on = False
#         self.color = askcolor(color=self.color)[1]
#
#     def use_eraser(self):
#         self.activate_button(self.eraser_button, eraser_mode=True)
#
#     def activate_button(self, some_button, eraser_mode=False):
#         self.active_button.config(relief=RAISED)
#         some_button.config(relief=SUNKEN)
#         self.active_button = some_button
#         self.eraser_on = eraser_mode
#
#     def paint(self, event):
#         self.line_width = self.choose_size_button.get()
#         paint_color = 'white' if self.eraser_on else self.color
#         if self.old_x and self.old_y:
#             self.c.create_line(self.old_x, self.old_y, event.x, event.y,
#                                width=self.line_width, fill=paint_color,
#                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
#         self.old_x = event.x
#         self.old_y = event.y
#
#     def reset(self, event):
#         self.old_x, self.old_y = None, None
#
#
# if __name__ == '__main__':
#     Paint()

#################################################################################################################

# import tkinter as tk
# from tkinter import ttk
#
# class PaintApp:
#     def __init__(self, root):
#         self.root = root
#         self.canvas_width = 800
#         self.canvas_height = 600
#         self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white", bd=3, relief=tk.SUNKEN)
#         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         self.setup_navbar()
#         self.setup_tools()
#         self.setup_events()
#         self.prev_x = None
#         self.prev_y = None
#
#     def setup_navbar(self):
#         self.navbar = tk.Menu(self.root)
#         self.root.config(menu=self.navbar)
#
#         # File menu
#         self.file_menu = tk.Menu(self.navbar, tearoff=False)
#         self.navbar.add_cascade(label="File", menu=self.file_menu)
#         self.file_menu.add_command(label="Save Snapshot", command=self.take_snapshot)
#         self.file_menu.add_separator()
#         self.file_menu.add_command(label="Exit", command=self.root.quit)
#
#         # Edit menu
#         self.edit_menu = tk.Menu(self.navbar, tearoff=False)
#         self.navbar.add_cascade(label="Edit", menu=self.edit_menu)
#         self.edit_menu.add_command(label="Undo", command=self.undo)
#
#     def setup_tools(self):
#         self.selected_tool = "pen"
#         self.colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"]
#         self.selected_color = self.colors[0]
#         self.brush_sizes = [2, 4, 6, 8]
#         self.selected_size = self.brush_sizes[0]
#         self.pen_types = ["line", "round", "square", "arrow", "diamond"]
#         self.selected_pen_type = self.pen_types[0]
#
#         self.tool_frame = ttk.LabelFrame(self.root, text="Tools")
#         self.tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)
#
#         self.pen_button = ttk.Button(self.tool_frame, text="Pen", command=self.select_pen_tool)
#         self.pen_button.pack(side=tk.TOP, padx=5, pady=5)
#
#         self.eraser_button = ttk.Button(self.tool_frame, text="Eraser", command=self.select_eraser_tool)
#         self.eraser_button.pack(side=tk.TOP, padx=5, pady=5)
#
#         self.brush_size_label = ttk.Label(self.tool_frame, text="Brush Size:")
#         self.brush_size_label.pack(side=tk.TOP, padx=5, pady=5)
#
#         self.brush_size_combobox = ttk.Combobox(self.tool_frame, values=self.brush_sizes, state="readonly")
#         self.brush_size_combobox.current(0)
#         self.brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
#         self.brush_size_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_size(int(self.brush_size_combobox.get())))
#
#         self.color_label = ttk.Label(self.tool_frame, text="Color:")
#         self.color_label.pack(side=tk.TOP, padx=5, pady=5)
#
#         self.color_combobox = ttk.Combobox(self.tool_frame, values=self.colors, state="readonly")
#         self.color_combobox.current(0)
#         self.color_combobox.pack(side=tk.TOP, padx=5, pady=5)
#         self.color_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_color(self.color_combobox.get()))
#
#         self.pen_type_label = ttk.Label(self.tool_frame, text="Pen Type:")
#         self.pen_type_label.pack(side=tk.TOP, padx=5, pady=5)
#
#         self.pen_type_combobox = ttk.Combobox(self.tool_frame, values=self.pen_types, state="readonly")
#         self.pen_type_combobox.current(0)
#         self.pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
#         self.pen_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_pen_type(self.pen_type_combobox.get()))
#
#         self.clear_button = ttk.Button(self.tool_frame, text="Clear Canvas", command=self.clear_canvas)
#         self.clear_button.pack(side=tk.TOP, padx=5, pady=5)
#
#     def setup_events(self):
#         self.canvas.bind("<B1-Motion>", self.draw)
#         self.canvas.bind("<ButtonRelease-1>", self.release)
#
#     def select_pen_tool(self):
#         self.selected_tool = "pen"
#
#     def select_eraser_tool(self):
#         self.selected_tool = "eraser"
#
#     def select_size(self, size):
#         self.selected_size = size
#
#     def select_color(self, color):
#         self.selected_color = color
#
#     def select_pen_type(self, pen_type):
#         self.selected_pen_type = pen_type
#
#     def draw(self, event):
#         if self.selected_tool == "pen":
#             if self.prev_x is not None and self.prev_y is not None:
#                 if self.selected_pen_type == "line":
#                     self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.selected_color,
#                                             width=self.selected_size, smooth=True)
#                 elif self.selected_pen_type == "round":
#                     x1 = event.x - self.selected_size
#                     y1 = event.y - self.selected_size
#                     x2 = event.x + self.selected_size
#                     y2 = event.y + self.selected_size
#                     self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
#                 elif self.selected_pen_type == "square":
#                     x1 = event.x - self.selected_size
#                     y1 = event.y - self.selected_size
#                     x2 = event.x + self.selected_size
#                     y2 = event.y + self.selected_size
#                     self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
#                 elif self.selected_pen_type == "arrow":
#                     x1 = event.x - self.selected_size
#                     y1 = event.y - self.selected_size
#                     x2 = event.x + self.selected_size
#                     y2 = event.y + self.selected_size
#                     self.canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill=self.selected_color,
#                                                outline=self.selected_color)
#                 elif self.selected_pen_type == "diamond":
#                     x1 = event.x - self.selected_size
#                     y1 = event.y
#                     x2 = event.x
#                     y2 = event.y - self.selected_size
#                     x3 = event.x + self.selected_size
#                     y3 = event.y
#                     x4 = event.x
#                     y4 = event.y + self.selected_size
#                     self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=self.selected_color,
#                                                outline=self.selected_color)
#             self.prev_x = event.x
#             self.prev_y = event.y
#
#     def release(self, event):
#         self.prev_x = None
#         self.prev_y = None
#
#     def clear_canvas(self):
#         self.canvas.delete("all")
#
#     def take_snapshot(self):
#         self.canvas.postscript(file="snapshot.eps")
#
#     def undo(self):
#         items = self.canvas.find_all()
#         if items:
#             self.canvas.delete(items[-1])
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Paint Application")
#     app = PaintApp(root)
#     root.mainloop()
#
# ########################################################################################################################
#
# from tkinter import *
# from tkinter.colorchooser import askcolor
#
# window = Tk()
# window.title("Paint")
# window.state('zoomed')
# window.geometry('700x700')
# current_x, current_y = 0, 0
#
# color = 'black'  # rang tanlanmasa qora rangda chizadi
#
#
# def locate_xy(event):
#     global current_x, current_y
#     current_x, current_y = event.x, event.y  # global o`zgaruvchilarni o`zgartiramiz
#
#
# def addLine(event):
#     global current_x, current_y
#     canvas.create_line((current_x, current_y, event.x, event.y),
#                        fill=color)  # liniya chizish uchun canvasning create_line(x1, y1, x2, y2) funksiyasidan foydalanamiz
#     # bunda x1,y1 chiziqning boshlanish kordinatalari, x2,y2 tugash kordinatalari
#     current_x, current_y = event.x, event.y  # Har doim bir xil nuqatadan boshlanmasligi uchun o`zgartirib qo`yamiz
#
#
# def show_color(new_color):
#     global color
#     color = new_color
#
#
# def new_canvas():
#     canvas.delete('all')
#     display_pallete()
#
#
# def choose_color():
#     color_code = askcolor(title="Choose color")[1]
#     global color
#     color = color_code
#
#
# window.rowconfigure(0, weight=1)
# window.columnconfigure(0, weight=1)
#
# menubar = Menu(window)
# window.config(menu=menubar)
# submenu = Menu(menubar, tearoff=0)
# submenu2 = Menu(menubar, tearoff=0)
#
# menubar.add_cascade(label='File', menu=submenu)
# submenu.add_command(label="New Canvas", command=new_canvas)
#
# menubar.add_cascade(label='About Paint', menu=submenu2)
#
# canvas = Canvas(window, background='#fff')
# canvas.grid(row=0, column=0, sticky='nsew')
#
# canvas.bind('<Button-1>', locate_xy)  # Button-1-->sichqoncha bilan bosilganda, o`sha nuqtaning joylashuvini oladi
# canvas.bind('<B1-Motion>', addLine)  # sichqonchani harakatlantirsa, chiziq-liniya chizadi.
#
#
# # canvas.create_rectangle((10, 10, 30,30), fill='black') -ranglarni ko`rsatish uchun rectangle-to`rtburchak yaratadi, xuddi linega o`xshab 4ta parametr qabul qiladi
#
# def display_pallete():  # ranglar palitrasi
#     id = canvas.create_rectangle((10, 10, 30, 30), fill='black')  # xar biriga id berib chiqish kk
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
#
#     id = canvas.create_rectangle((10, 40, 30, 60), fill='gray')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))
#
#     id = canvas.create_rectangle((10, 70, 30, 90), fill='brown4')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
#
#     id = canvas.create_rectangle((10, 100, 30, 120), fill='red')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
#
#     id = canvas.create_rectangle((10, 130, 30, 150), fill='orange')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
#
#     id = canvas.create_rectangle((10, 160, 30, 180), fill='yellow')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
#
#     id = canvas.create_rectangle((10, 190, 30, 210), fill='green')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
#
#     id = canvas.create_rectangle((10, 220, 30, 240), fill='blue')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
#
#     id = canvas.create_rectangle((10, 250, 30, 270), fill='purple')
#     canvas.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
#
#     id = canvas.create_text(50, 300, text='Choose color..', font=("Arial"))
#     canvas.tag_bind(id, '<Button-1>', lambda x: choose_color())
#
#
# display_pallete()
#
# window.mainloop()

########################################################################################################################

# import tkinter as tk
# from tkinter.filedialog import askopenfilename, asksaveasfilename
#
#
# def open_file():
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# def save_file():
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", ".txt")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# window = tk.Tk()
# window.title("Simple Text Editor")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
#
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#
# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")
#
# window.mainloop()


########################################################################################################################


import tkinter as tk

# creating a new tkinter window
master = tk.Tk()

# assigning a title
master.title("MARKSHEET")

# specifying geometry for window size
master.geometry("700x250")

# declaring objects for entering data
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


# function to display the total subject
# credits total credits and SGPA according
# to grades entered
def display():
    # Variable to store total marks
    tot = 0

    # 10*number of subject credits
    # give total credits for grade A
    if e4.get() == "A":
        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        tk.Label(master, text="40").grid(row=3, column=4)
        tot += 40

    # 9*number of subject credits give
    # total credits for grade B
    if e4.get() == "B":
        tk.Label(master, text="36").grid(row=3, column=4)
        tot += 36

    # 8*number of subject credits give
    # total credits for grade C
    if e4.get() == "C":
        tk.Label(master, text="32").grid(row=3, column=4)
        tot += 32

    # 7*number of subject credits
    # give total credits for grade D
    if e4.get() == "D":
        tk.Label(master, text="28").grid(row=3, column=4)
        tot += 28

    # 6*number of subject credits give
    # total credits for grade P
    if e4.get() == "P":
        tk.Label(master, text="24").grid(row=3, column=4)
        tot += 24

    # 0*number of subject credits give
    # total credits for grade F
    if e4.get() == "F":
        tk.Label(master, text="0").grid(row=3, column=4)
        tot += 0

    # Similarly doing with other objects
    if e5.get() == "A":
        tk.Label(master, text="40").grid(row=4, column=4)
        tot += 40
    if e5.get() == "B":
        tk.Label(master, text="36").grid(row=4, column=4)
        tot += 36
    if e5.get() == "C":
        tk.Label(master, text="32").grid(row=4, column=4)
        tot += 32
    if e5.get() == "D":
        tk.Label(master, text="28").grid(row=4, column=4)
        tot += 28
    if e5.get() == "P":
        tk.Label(master, text="28").grid(row=4, column=4)
        tot += 24
    if e5.get() == "F":
        tk.Label(master, text="0").grid(row=4, column=4)
        tot += 0

    if e6.get() == "A":
        tk.Label(master, text="30").grid(row=5, column=4)
        tot += 30
    if e6.get() == "B":
        tk.Label(master, text="27").grid(row=5, column=4)
        tot += 27
    if e6.get() == "C":
        tk.Label(master, text="24").grid(row=5, column=4)
        tot += 24
    if e6.get() == "D":
        tk.Label(master, text="21").grid(row=5, column=4)
        tot += 21
    if e6.get() == "P":
        tk.Label(master, text="28").grid(row=5, column=4)
        tot += 24
    if e6.get() == "F":
        tk.Label(master, text="0").grid(row=5, column=4)
        tot += 0

    if e7.get() == "A":
        tk.Label(master, text="40").grid(row=6, column=4)
        tot += 40
    if e7.get() == "B":
        tk.Label(master, text="36").grid(row=6, column=4)
        tot += 36
    if e7.get() == "C":
        tk.Label(master, text="32").grid(row=6, column=4)
        tot += 32
    if e7.get() == "D":
        tk.Label(master, text="28").grid(row=6, column=4)
        tot += 28
    if e7.get() == "P":
        tk.Label(master, text="28").grid(row=6, column=4)
        tot += 24
    if e7.get() == "F":
        tk.Label(master, text="0").grid(row=6, column=4)
        tot += 0

    # to display total credits
    tk.Label(master, text=str(tot)).grid(row=7, column=4)

    # to display SGPA
    tk.Label(master, text=str(tot / 15)).grid(row=8, column=4)


# end of display function

# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)

# label for registration number
tk.Label(master, text="Reg.No").grid(row=0, column=3)

# label for roll Number
tk.Label(master, text="Roll.No").grid(row=1, column=0)

# labels for serial numbers
tk.Label(master, text="Srl.No").grid(row=2, column=0)
tk.Label(master, text="1").grid(row=3, column=0)
tk.Label(master, text="2").grid(row=4, column=0)
tk.Label(master, text="3").grid(row=5, column=0)
tk.Label(master, text="4").grid(row=6, column=0)

# labels for subject codes
tk.Label(master, text="Subject").grid(row=2, column=1)
tk.Label(master, text="CS 201").grid(row=3, column=1)
tk.Label(master, text="CS 202").grid(row=4, column=1)
tk.Label(master, text="MA 201").grid(row=5, column=1)
tk.Label(master, text="EC 201").grid(row=6, column=1)

# label for grades
tk.Label(master, text="Grade").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)

# labels for subject credits
tk.Label(master, text="Sub Credit").grid(row=2, column=3)
tk.Label(master, text="4").grid(row=3, column=3)
tk.Label(master, text="4").grid(row=4, column=3)
tk.Label(master, text="3").grid(row=5, column=3)
tk.Label(master, text="4").grid(row=6, column=3)

tk.Label(master, text="Credit obtained").grid(row=2, column=4)

# taking entries of name, reg, roll number respectively
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

# button to display all the calculated credit scores and sgpa
button1 = tk.Button(master, text="submit", bg="green", command=display)
button1.grid(row=8, column=1)

tk.Label(master, text="Total credit").grid(row=7, column=3)
tk.Label(master, text="SGPA").grid(row=8, column=3)

master.mainloop()