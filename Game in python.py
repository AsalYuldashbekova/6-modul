import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown', 'Gray', 'Green']
score = 0

timeleft = 30


def startGame(event):
    if timeleft == 30:
        countdown()

    nextColour()


def nextColour():
    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: "
                              + str(timeleft))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLORGAME")

root.geometry("375x200")

instructions = tkinter.Label(root, text="Ranglarni tez yozishingiz sinaladi",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Boshlash uchun enter tugmasini bosing",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Vaqt: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()

########################################################################################################################

# from tkinter import *
#
# canvas_width = 200
# canvas_height = 100
#
# colours = ("#476042", "yellow")
# box=[]
#
# for ratio in ( 0.2, 0.35 ):
#    box.append( (canvas_width * ratio,
#                 canvas_height * ratio,
#                 canvas_width * (1 - ratio),
#                 canvas_height * (1 - ratio) ) )
#
# master = Tk()
#
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w.pack()
#
# for i in range(2):
#    w.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])
#
# w.create_line(0, 0,                 # origin of canvas
#               box[0][0], box[0][1], # coordinates of left upper corner of the box[0]
#               fill=colours[0],
#               width=3)
# w.create_line(0, canvas_height,     # lower left corner of canvas
#               box[0][0], box[0][3], # lower left corner of box[0]
#               fill=colours[0],
#               width=3)
# w.create_line(box[0][2],box[0][1],  # right upper corner of box[0]
#               canvas_width, 0,      # right upper corner of canvas
#               fill=colours[0],
#               width=3)
# w.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
#               canvas_width, canvas_height, # lower right corner of canvas
#               fill=colours[0], width=3)
#
# w.create_text(canvas_width / 2,
#               canvas_height / 2,
#               text="Python")
# mainloop()


########################################################################################################################

# from tkinter import *
#
# canvas_width = 400
# canvas_height = 400
#
# python_green = "#476042"
#
#
# def polygon_star(canvas, x, y, p, t, outline=python_green, fill='yellow', width=1):
#     points = []
#     for i in (1, -1):
#         points.extend((x, y + i * p))
#         points.extend((x + i * t, y + i * t))
#         points.extend((x + i * p, y))
#         points.extend((x + i * t, y - i * t))
#
#     canvas.create_polygon(points, outline=outline,
#                           fill=fill, width=width)
#
#
# master = Tk()
#
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w.pack()
#
# p = 50
# t = 15
#
# nsteps = 10
# step_x = int(canvas_width / nsteps)
# step_y = int(canvas_height / nsteps)
#
# for i in range(1, nsteps):
#     polygon_star(w, i * step_x, i * step_y, p, t, outline='red', fill='gold', width=3)
#     polygon_star(w, i * step_x, canvas_height - i * step_y, p, t, outline='red', fill='gold', width=3)
#
# mainloop()

########################################################################################################################

#
# from tkinter import *
#
# canvas_width = 300
# canvas_height = 80
#
# master = Tk()
# canvas = Canvas(master,
#                 width=canvas_width,
#                 height=canvas_height)
# canvas.pack()
#
# bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# nsteps = len(bitmaps)
# step_x = int(canvas_width / nsteps)
#
# for i in range(0, nsteps):
#     canvas.create_bitmap((i + 1) * step_x - step_x / 2, 50, bitmap=bitmaps[i])
#
# mainloop()

########################################################################################################################
