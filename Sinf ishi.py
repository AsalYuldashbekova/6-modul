import random
from tkinter import *

window = Tk()

canvas = Canvas(window, width=600, height=600)
canvas.pack()

score = 0
score_label = Label(window, text=f"Score: {score}")
score_label.pack()

savatcha = canvas.create_rectangle(270, 550, 330, 580, fill="orange")
objects = []

for i in range(25):
    x = random.randint(0, 590)
    y = random.randint(10, 50)
    objects.append(canvas.create_oval(x, y, x + 10, y + 10, fill="red"))


def move_basket(event):
    if event.keysym == "Right":
        canvas.move(savatcha, 20, 0)
    if event.keysym == "Left":
        canvas.move(savatcha, -20, 0)


def move_objects():
    global score
    for obj in objects:
        canvas.move(obj, 0, 7)

        pos = canvas.coords(obj)
        if pos[3] >= 600:
            x = random.randint(0, 590)
            y = random.randint(0, 50)
            canvas.coords(obj, x, y, x + 15, y + 15)
        elif len(canvas.find_overlapping(*canvas.coords(savatcha))) > 1:
            x = random.randint(0, 590)
            y = random.randint(0, 50)
            canvas.coords(obj, x, y, x + 15, y + 15)
            score += 1
            score_label.config(text=f"Score {score}")
    window.after(50, move_objects)


canvas.bind_all("<Key>", move_basket)

canvas.bind_all("<Key>", move_basket)

move_objects()
window.mainloop()




