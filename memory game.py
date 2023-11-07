from random import shuffle
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Xotira o`yin")
window.geometry("1000x800")
time_remaining = 20

time_label = Label(window, text=f"Time remaining {time_remaining}", font=("Arial", 24))
time_label.pack(pady=20)

blank_image = PhotoImage(file="blank.png")
image_files = ['img_1.png', 'img_2.png', 'img_3.png', ]
images = [PhotoImage(file=image) for image in image_files]
images = images + images

shuffle(images)


def time_update():
    global time_remaining
    time_remaining -= 1
    time_label.config(text=f"Time remaining {time_remaining}")

    if time_remaining == 0:
        messagebox.showinfo(title="Xabar", message="Game over")
        window.destroy()

    window.after(1000, time_update)


button_frame = Frame(window)
button_frame.pack()

buttons = []

clicked_buttons = []

for i in range(8):
    button = Button(button_frame, width=200, height=200, image=blank_image)
    button.grid(row=i // 4, column=i % 4, pady=20, padx=20)
    buttons.append(button)

time_update()
window.mainloop()
