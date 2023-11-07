# # import tkinter
# # from tkinter import *
# # import random
# # window = Tk()
# # window.geometry("500x500")
# #
# # user = input("Tosh/Qaychi/Qog`oz:").lower()
# # box = ["tosh", "qaychi", "qog`oz"]
# # taxmin = random.randint(0, 3)
# # laptop = box[taxmin]
# # print(f"Siz:{user}\nKompyuter:{laptop}")
# # if user ==laptop:
# #     print("Durrang!")
# # elif user == "tosh" and laptop == "qaychi" or user == "qaychi" and laptop == "qog'oz" or user == "qog'oz" and laptop == "tosh":
# #     print("Tabriklayman siz G'olibsiz!")
# # else:
# #     print("Afsuski siz Mag'lubsiz!")
# #
# #
# #
# #
# # # mainloop()
# # # import tkinter as tk
# # # # import tkinter
# # # from tkinter import ttk
# # #
# # # window = tk.Tk()
# # # n = tk.StringVar()
# # # country = ttk.Combobox(window, width=27, textvariable=n)
# # #
# # # country['values'] = ('Python',
# # #                      'C',
# # #                      'C++',
# # #                      'Java')
# # # country.place(x=0, y=0)
# # #
# # # sp = ttk.Spinbox(window, from_=0, to=20, width=20, background="Green")
# # # sp.place(x=10, y=50)
# # #
# # # st = tk.Scrollbar(window,
# # #                    side = "RIGHT",
# #
# # #
# # # from tkinter import *
# # # from tkinter import ttk
# # # window = Tk()
# # # tk = Tk()
# # #
# # # tk.geometry("250x200")
# # #
# # # languages = ["Python", "JavaScript", "C++", "Java"]
# # # languages_var = Variable(value=languages)
# # #
# # # languages_listbox = Listbox(listvariable=languages_var)
# # #
# # # languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
# # #
# # # tk.mainloop()
# #
# # # #######################################################################################################################
# # #
# # # window.geometry('500x500')
# # # v1 = DoubleVar()
# # #
# # # s1 = Scale(window, variable=v1,
# # #            from_=1, to=100,
# # #            orient=VERTICAL)
# # #
# # # s1.pack()
# # # list_box = Listbox(window)
# # # for i in range(0, 101):
# # #     list_box.insert(f"")
# # # list_box.place(x=0, y=0)
# # #
# # # scrollbar = Scrollbar(window)
# # # scrollbar.pack(side=RIGHT, fill=BOTH)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # def delete():
# # #     selection = languages_listbox.curselection()
# # #     languages_listbox.delete(selection[0])
# # #
# # #
# # #
# # # def add():
# # #     new_language = language_entry.get()
# # #     languages_listbox.insert(0, new_language)
# # #
# # # tk = Tk()
# # # tk.title("METANIT.COM")
# # # tk.geometry("300x250")
# # # tk.columnconfigure(index=0, weight=4)
# # # tk.columnconfigure(index=1, weight=1)
# # # tk.rowconfigure(index=0, weight=1)
# # # tk.rowconfigure(index=1, weight=3)
# # # tk.rowconfigure(index=2, weight=1)
# # #
# # #
# # # language_entry = ttk.Entry()
# # # language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
# # # ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
# # #
# # #
# # # languages_listbox = Listbox()
# # # languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
# # #
# # #
# # # languages_listbox.insert(END, "Python")
# # # languages_listbox.insert(END, "C#")
# # #
# # # ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
# # # mainloop()
# # # sc = Scrollbar(window)
# # # sc.pack()
# #
# #
# #
# #
# # # import tkinter
# # # from PIL import ImageTk, Image
# # #
# # # from PIL import ImageTk, Image
# # # from tkinter import *
# # #
# # # window = Tk()
# # #
# # #
# # #
# # # window.geometry("500x500")
# # # img_2 = ImageTk.PhotoImage(file='img_2.png')
# # # img_3 = ImageTk.PhotoImage(file='img_3.png')
# # # img_5 = ImageTk.PhotoImage(file='img_5.png')
# # #
# # # img = [img_2, img_3, img_5]
# # #
# # # current_index = 0
# # #
# # #
# # # def keyingi():
# # #     global current_index
# # #     current_index = (current_index + 1) % len(img)
# # #
# # #     image = img[current_index]
# # #
# # #     image_label.configure(image=image)
# # #
# # #
# # # image_label = Label(window, image=img[current_index])
# # # image_label.place(x=0, y=0)
# # #
# # # btn = Button(window, text="oldingi")
# # # btn.place(x=10, y=300)
# # # btn = Button(window, text="Chiqish")
# # # btn.place(x=80, y=300)
# # # btn = Button(window, text="Keyingi", command=keyingi)
# # # btn.place(x=150, y=300)
# # #
# # #
# # #
# # # window.mainloop()
# #
# #
# #
# # # photo = PhotoImage(fi
# # #
# # #
# # # le='img_1.png')
# # # photo_image = photo.subsample(10, 10)
# # #
# # # btn = Button(window, text='btn', image=photo_image)
# # # btn.place(x=0, y=0)
# #
# # # button = Button(text="Sotib olish")
# # # button.place(x=100, y=100)
# #
# # #
# # # window.geometry("500x500")
# # # photo = ImageTk.PhotoImage(file='img_1.png')
# # # phot = Label(window, image=photo)
# # # phot.place(x=0, y=0)
# #
# #
# # # programma = tk.Label(text="What would you like order?")
# # # programma.place(x=0,y=0)
# # # text = tk.Checkbutton(text="Sandwich")
# # # text.place(x=0,y=50)
# # # textt = tk.Checkbutton(text="Salad")
# # # textt.place(x=0,y=75)
# # # tex = tk.Checkbutton(text="Soup")
# # # tex.place(x=0,y=100)
# # # texrt = tk.Checkbutton(text="Pizza")
# # # texrt.place(x=0,y=125)
# #
# #
# # # programma = tk.Label(text="Select Programming language of your choice")
# # # programma.place(x=0,y=0)
# # # text = tk.Checkbutton(text="Java")
# # # text.place(x=0,y=50)
# # # textt = tk.Checkbutton(text="C++")
# # # textt.place(x=0,y=75)
# # # tex = tk.Checkbutton(text="Python")
# # # tex.place(x=0,y=100)
# # # texrt = tk.Checkbutton(text="C")
# # # texrt.place(x=0,y=125)
# #
# #
# # # window.mainloop()
# #
# # # import random
# # #
# # # attemps = 0
# # #
# # # myName = input("Ismingizni kiriting:")
# # # number = random.randint(1, 100)
# # # print("Salom!,Men 1 dan 50 gacha bo`lgan sondan bittasini o`ylayman")
# # #
# # # while attemps <10:
# # #     print("Taxmin qiling!")
# # #     taxmin_son = int(input())
# # #     attemps += 1
# # #
# # #     if taxmin_son < number:
# # #         print("Sizning taxnimingiz past")
# # #     if taxmin_son > number:
# # #         print("Sizning taxminingiz katta")
# # #     if taxmin_son == number:
# # #         break
# # #
# # # if taxmin_son == number:
# # #     print(myName,"Tabriklaymiz,siz raqamni topdingiz! ")
# # # if taxmin_son != number:
# # #     print("Siz yutqazdingiz ")
# # #
# # #
# # # import tkinter as tk
# # #
# # # window = tk.Tk()
# # # window.configure(background="green")
# # # window.geometry("500x500")
# #
# #
# # # window.mainloop()
# #
# #
# # # from tkinter import *
# # # from tkinter.ttk import Combobox
# # #
# # # window = Tk()
# # # var = StringVar()
# # # var.set("one")
# # # data = ("one", "two", "three", "four")
# # # cb = Combobox(window, values=data)
# # # cb.place(x=60, y=150)
# # #
# # # lb = Listbox(window, height=5, selectmode='multiple')
# # # for num in data:
# # #     lb.insert(END, num)
# # # lb.place(x=250, y=150)
# # #
# # # v0 = IntVar()
# # # v0.set(1)
# # # r1 = Radiobutton(window, text="male", variable=v0, value=1)
# # # r2 = Radiobutton(window, text="female", variable=v0, value=2)
# # # r1.place(x=100, y=50)
# # # r2.place(x=180, y=50)
# # #
# # # v1 = IntVar()
# # # v2 = IntVar()
# # # C1 = Checkbutton(window, text="Cricket", variable=v1)
# # # C2 = Checkbutton(window, text="Tennis", variable=v2)
# # # C1.place(x=100, y=100)
# # # C2.place(x=180, y=100)
# # #
# # # window.title('Hello Python')
# # # window.geometry("400x300+10+10")
# # # window.mainloop()
# #
# #
# # # import tkinter as tk
# # #
# # # window = tk.Tk()
# # #
# # # frame1 = tk.Frame(master=window, height=50, bg="blue")
# # # frame1.pack(fill=tk.X)
# # #
# # # frame4 = tk.Frame(master=window, height=5, bg="red")
# # # frame4.pack(fill=tk.X)
# # #
# # #
# # # frame2 = tk.Frame(master=window, height=50, bg="white")
# # # frame2.pack(fill=tk.X)
# # #
# # # frame5 = tk.Frame(master=window, height=5, bg="red")
# # # frame5.pack(fill=tk.X)
# # #
# # #
# # # frame3 = tk.Frame(master=window, height=50, bg="green")
# # # frame3.pack(fill=tk.X)
# # #
# # # window.mainloop()
# # #
# #
# #
# # # import tkinter as tk
# # #
# # # window = tk.Tk()
# # # window.geometry("335x500")
# # # window.title("tk")
# # #
# # # # def btn_click(number):
# # # # #     amallar = ['-','+','*','/']
# # # #     amal = ''
# # # #     sonlar = ''
# # # #     if number in amallar:
# # # #         amal = number
# # # #     sonlar += number
# # # #     hisob.insert(tk.END,number)
# # #
# # #
# # #
# # # def hisoblash():
# # #     global expression
# # #     result = str(eval(expression))
# # #     hisob.insert(tk.END, result)
# # #
# # # hisob = tk.Text(height=5, width=40)
# # # hisob.place(x=0, y=0)
# # #
# # # yetti = tk.Button(text="7",width=10,height=5, command=lambda: btn_click(7))
# # # yetti.place(x=0, y=84)
# # #
# # # sakkiz = tk.Button(text="8",width=10,height=5, command=lambda: btn_click(8))
# # # sakkiz.place(x=84, y=84)
# # #
# # # toqqiz = tk.Button(text="9",width=10,height=5, command=lambda: btn_click(9))
# # # toqqiz.place(x=168, y=84)
# # #
# # # kopaytirish = tk.Button(text="x",width=10,height=5, command=lambda: btn_click("x"))
# # # kopaytirish.place(x=252, y=84)
# # #
# # # tort = tk.Button(text="4",width=10,height=5, command=lambda: btn_click(4))
# # # tort.place(x=0, y=170)
# # #
# # # besh = tk.Button(text="5",width=10,height=5, command=lambda: btn_click(5))
# # # besh.place(x=84, y=170)
# # #
# # # olti = tk.Button(text="6",width=10,height=5, command=lambda: btn_click(6))
# # # olti.place(x=168, y=170)
# # #
# # # ayirish = tk.Button(text="-",width=10,height=5, command=lambda: btn_click("-"))
# # # ayirish.place(x=252, y=170)
# # #
# # # bir = tk.Button(text="1",width=10,height=5, command=lambda: btn_click(1))
# # # bir.place(x=0, y=258)
# # #
# # # ikki = tk.Button(text="2", width=10, height=5, command=lambda: btn_click(2))
# # # ikki.place(x=84, y=258)
# # #
# # # uch = tk.Button(text="3",width=10,height=5, command=lambda: btn_click(3))
# # # uch.place(x=168, y=258)
# # #
# # # qoshish = tk.Button(text="+",width=10,height=5, command=lambda: btn_click("+"))
# # # qoshish.place(x=252, y=258)
# # #
# # # nol = tk.Button(text="0",width=10,height=5, command=lambda: btn_click(0))
# # # nol.place(x=0, y=345)
# # #
# # # teng = tk.Button(text="=",width=10,height=5, command=lambda: btn_click("="))
# # # teng.place(x=84, y=345)
# # #
# # # ce = tk.Button(text="CE",width=10,height=5)
# # # ce.place(x=168, y=345)
# # #
# # # bolish = tk.Button(text="÷",width=10,height=5, command=lambda: btn_click("÷"))
# # # bolish.place(x=252, y=345)
# #
# #
# # # ogirlik = tk.Label(text="Og`irlikni KG da kiriting:")
# # # ogirlik.place(x=0,y=0)
# # # kiritish = tk.Entry()
# # # kiritish.place(x=135,y=0)
# # #
# # # funtt = 2.20462
# # # untsiya = 35.274
# # # gram = 1000
# # #
# # # def funtda():
# # #     kg = funtt * int(kiritish.get())
# # #     kkg = untsiya * int(kiritish.get())
# # #     kgg = gram * int(kiritish.get())
# # #
# # #     kiriti.insert(tk.END, kg)
# # #     kirit.insert(tk.END, kgg)
# # #     kiritishi.insert(tk.END, kkg)
# # #
# # # grram = tk.Label(text="Gramm")
# # # grram.place(x=50,y=30)
# # # kirit = tk.Text(window, width=18, height=1)
# # # kirit.place(x=0, y=55)
# # #
# # # pou = tk.Label(text="Pount")
# # # pou.place(x=200,y=30)
# # # kiriti = tk.Text(window, width=18, height=1)
# # # kiriti.place(x=175,y=55)
# # #
# # # oun = tk.Label(text="Ounce")
# # # oun.place(x=350,y=30)
# # # kiritishi = tk.Text(window, width=18, height=1)
# # # kiritishi.place(x=350,y=55)
# # #
# # # hisoblash = tk.Button(text = "Hisoblash",command=funtda)
# # # hisoblash.place(x=400,y=10)
# #
# # # def get_age():
# # #     age = 2023 - int(text.get())
# # #     text2 = f"Sizning yoshingiz:{age}"
# # #     l1 = tk.Label(window, text=text2)
# # #     l1.place(x=0, y=200)
# # #
# # # label1 = tk.Label(window, text="Yil")
# # #
# # # yosh = tk.Entry(window)
# # #
# # # kun = tk.Label(window, text="Kun:")
# # # kun.place(x=0, y=0)
# # # entry = tk.Entry()
# # # entry.place(x=60, y=0)
# # # oy = tk.Label(window, text="Oy:")
# # # oy.place(x=0, y=40)
# # # entri = tk.Entry()
# # # entri.place(x=60, y=40)
# # # yil = tk.Label(window, text="Yil:")
# # # yil.place(x=0, y=80)
# # # text = tk.Entry()
# # # text.place(x=60, y=80)
# # #
# # #
# # #
# # #
# # # button = tk.Button(text="Hisoblang", command=get_age)
# # # button.place(x=70, y=125)
# # #
# # # chiqish = tk.Button(text="Chiqish", width=10, bg="white", fg="black")
# # # chiqish.place(x=160, y=125)
# #
# # # kun = tk.Label(window,text="Username:")
# # # kun.place(x=0 , y=0)
# # # entry = tk.Entry()
# # # entry.place(x=60,y=0)
# # # oy = tk.Label(window,text="Email:")
# # # oy.place(x=0,y=40)
# # # entri = tk.Entry()
# # # entri.place(x=60,y=40)
# # # username = tk.Label(window, text="Gender")
# # # male_label = tk.Radiobutton(window,text="Male",value=False)
# # # female_label = tk.Radiobutton(window,text="Female",value=True)
# # # username.place(x=0,y=80)
# # # male_label.place(x=70,y=80)
# # # female_label.place(x=180,y=80)
# # # age = tk.Label(text="Age")
# # # age.place(x=0,y=120)
# # # text = tk.Entry()
# # # text.place(x=60,y=120)
# # # button = tk.Button(text="Submit",bg="red",fg="white")
# # # button.place(x=100,y=150)
# #
# #
# # # def username_get():
# # #     name = f""
# # # text = tk.Label(text="Username")
# # # text.grid(row=0, column=0)
# # #
# # # malumot = tk.Entry()
# # # malumot.grid(row=0, column=1)
# # #
# # # text = tk.Label(text="Password")
# # # text.grid(row=1, column=0)
# # #
# # # malumott = tk.Entry()
# # # malumott.grid(row=1,column=1)
# # #
# # # btn = tk.Button(text="Login")
# # # btn.grid(row=2, column=1)
# # #
# #
# #
# # # salom = tk.Button(text="CE",width=10,height=5,)
# # # salom.place(x=1254,y=0)
# # # c = tk.Button(text="C",width=10,height=5)
# # # c.place(x=1504,y=0)
# # # x = tk.Button(text="≪",width=10,height=5)
# # # x.place(x=875,y=0)
# # # bol = tk.Button(text="÷",width=10,height=5)
# # # bol.place(x=950,y=0)
# # # son = tk.Button(text="7",width=10,height=5)
# # # son.place(x=725,y=83)
# # # sonn = tk.Button(text="8",width=10,height=5)
# # # sonn.place(x=800,y=83)
# # # sonni = tk.Button(text="9",width=10,height=5)
# # # sonni.place(x=875,y=83)
# # # sonnin = tk.Button(text="x",width=10,height=5)
# # # sonnin.place(x=950,y=83)
# # # soni = tk.Button(text="4",width=10,height=5)
# # # soni.place(x=725,y=165)
# # # sone = tk.Button(text="5",width=10,height=5)
# # # sone.place(x=800,y=165)
# # # sonl = tk.Button(text="6",width=10,height=5)
# # # sonl.place(x=875,y=165)
# # # sonq = tk.Button(text="–",width=10,height=5)
# # # sonq.place(x=950,y=165)
# # # soa = tk.Button(text="1",width=10,height=5)
# # # soa.place(x=725,y=245)
# # # s = tk.Button(text="2",width=10,height=5)
# # # s.place(x=800,y=245)
# # # so = tk.Button(text="3",width=10,height=5)
# # # so.place(x=875,y=245)
# # # sonnl = tk.Button(text="+",width=10,height=5)
# # # sonnl.place(x=950,y=245)
# #
# #
# # # window.mainloop()
# #
# # # import tkinter as *
# # #
# # # window = Tk()
# # # window.geometry("300x200")
# # # window.title("Budilnik")
# # # window.configure(bg="#345")
# # #
# # # h = StringVar()
# # # m = StringVar()
# # # s = StringVar()
# # #
# # # h.set("00")
# # # m.set("00")
# # # s.set("00")
# # #
# # # hour = Entry(window,width=4, textvariable=h)
# # # hour.place(x=40,y=20)
# # # minute = Entry(window,width=4,textvariable=m)
# # # minute.place(x=70,y=20)
# # # second = Entry(window,width=4,textvariable=s)
# # # second.place(x=100,y=20)
# # #
# # #
# # #
# # # def countdowntimer():
# # #     user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
# # #     while user_input>-1:
# # #         minutes,seconds = divmod(user_input,60)
# # #
# # #         hours = 0
# # #         if minutes>60:
# # #             hours,minutes = divmod(minutes,60)
# # #
# # #             h.set("{0:2d}".format(hours))
# # #             m.set("{0:2d}".format(minutes))
# # #             s.set("{0:2d}".format(seconds))
# # #
# # #             window.update()
# # #             time.sleep(1)
# # #
# # #
# # #
# # #             if user_input == 0:
# # #                 messagebox.showinfo("Budilnik","Vaqt tugadi")
# # #
# # #             user_input -= 1
# # # btn = Button(window,text="Budilnik qo`ying!",command=countdowntimer)
# # # btn.place(x=80,y=90)
# # #
# # #
# # #
# # #
# # # mainloop()
# #
# #
# # # import tkinter as tk
# # #
# # #
# # # window = tk.Tk()
# # # window.geometry('300x500')
# # # salom = tk.Label(text="First name:")
# # # salom.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # familiya = tk.Label(text="Last name:")
# # # familiya.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # manzil1 = tk.Label(text="Address Line 1:")
# # # manzil1.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # manzil2 = tk.Label(text="Address Line 2:")
# # # manzil2.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # shahar = tk.Label(text="City:")
# # # shahar.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # state = tk.Label(text="State/Province:")
# # # state.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # code = tk.Label(text="Postel Code:")
# # # code.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # mamlakat = tk.Label(text="Country:")
# # # mamlakat.pack()
# # # entry = tk.Entry()
# # # entry.pack()
# # # button = tk.Button(text="Clear")
# # # button.place(x=290,y=250)
# # # button = tk.Button(text="Submit")
# # # button.place(x=290,y=190)
# # #
# # #
# # #
# # #
# # # tk.mainloop()
# # #
# # # # from tkinter import *
# # # # window = Tk()
# # # # window.geometry('100x100')
# # # # master = Tk()
# # # # var1 = IntVar()
# # # # Checkbutton(master, text='Algebra', variable=var1).grid(row=0, sticky=W)
# # # # var2 = IntVar()
# # # # Checkbutton(master, text='Ona tili', variable=var2).grid(row=1, sticky=W)
# # # # var3 = IntVar()
# # # # Checkbutton(master, text='Informatika', variable=var3).grid(row=2, sticky=W)
# # # # var4 = IntVar()
# # # # Checkbutton(master, text='Geometriya', variable=var4).grid(row=3, sticky=W)
# # # # var5 = IntVar()
# # # # Checkbutton(master, text='Fizika', variable=var5).grid(row=4, sticky=W)
# # # # var6 = IntVar()
# # # # Checkbutton(master, text='Jismoniy tarbiya', variable=var6).grid(row=5, sticky=W)
# # # #
# # # mainloop()
# #
# #
# # # import random
# # #
# # # attemps = 0
# # #
# # # myName = input("Ismingizni kiriting:")
# # # number = random.randint(1,50)
# # # print("Salom!,Men 1 dan 50 gacha bo`lgan sondan bittasini o`ylayman")
# # #
# # # while attemps <10:
# # #     print("Taxmin qiling!")
# # #     taxmin_son = int(input())
# # #     attemps += 1
# # #
# # #     if taxmin_son < number:
# # #         print("Sizning taxnimingiz past")
# # #     if taxmin_son > number:
# # #         print("Sizning taxminingiz katta")
# # #     if taxmin_son == number:
# # #         break
# # #
# # # if taxmin_son == number:
# # #     print(myName,"Tabriklaymiz,siz raqamni topdingiz! ")
# # # if taxmin_son != number:
# # #     print("Siz yutqazdingiz ")
# #
# #
# # # import tkinter
# # # from tkinter import *
# # # # import tkinter.ttk
# # # from tkinter.ttk import *
# # #
# # #
# # #
# # # window = Tk()
# # # window.geometry("600x600",)
# # # window.title("Salom")
# # #
# # # frame = Frame()
# # # btn = Button(window, text="Meni o`chir", style='W.TButton',command=window.destroy)
# # # style = Style()
# # # style.configure('W.TButton',font = ('calibri',10,"bold","underline"),foreground="yellow",background="black")
# # # label = Label(frame,text="Label",justify=LEFT)
# # # label.pack(side=LEFT)
# # # msg = Message(window,text="PDP Junior o`quvchilari")
# # #
# # # text = Text(window, height=4,width=52)
# # #
# # # mainloop()
# #
# #
# # # import random
# # # import turtle
# # #
# # # score = 0
# # # high_score = 0
# # #
# # # screen = turtle.Screen()
# # # screen.title("Snace Game")
# # # screen.setup(width=600, height=600)
# # # screen.tracer(0)
# # #
# # # # head of the snace
# # # head = turtle.Turtle()
# # # head.shape("square")
# # # head.color("green")
# # # head.up()
# # # head.goto(0, 0)
# # # head.direcrion = "Stop"
# # #
# # # # food in the game
# # # food = turtle.Turtle()
# # # colors = random.choice(['red', 'green', 'orange', 'blue'])
# # # shapes = random.choice(["square", "triangle", "circle"])
# # # food.speed(0)
# # # food.shape(shapes)
# # # food.color(colors)
# # # food.up()
# # # food.goto(0, 100)
# # #
# # # pen = turtle.Turtle()
# # # pen.speed(0)
# # # pen.shape("square")
# # # pen.color("white")
# # # pen.up()
# # # pen.hideturtle()
# # # pen.goto(0, 250)
# # # pen.write(f"Score {score} /High score {high_score}, align='centre'")
# # #
# # #
# # # # assigning keydirections
# # #
# # # def group():
# # #     if head.direction != "Down":
# # #         head.direction = "Up"
# # #
# # #
# # # def godown():
# # #     if head.direction != "Up":
# # #         head.direction = "Down"
# # #
# # #
# # # def goright():
# # #     if head.direction != "left":
# # #         head.direction = "right"
# # #
# # #
# # # def goleft():
# # #     if head.direction != "left":
# # #         head.direction = "right"
# # #
# # #
# # # def move():
# # #     if head.direction == "Up":
# # #         y = head.ycor(y+20)
# # #         head.sety()
# # #
# # # segments = []
# # #
# # # while True:
# # #     screen.update()
# # #     if head.xcor()>290 or head.xcor() -290 or head.ycor() < -290 or head.ycor() < -290:
# # #         time.sleep(1)
# # #         head.goto(0,0)
# # #         head.direcrion = "Stop"
# # #         colors = random.choice(['red', 'green', 'orange', 'blue'])
# # #         shapes = random.choice(["square", "triangle", "circle"])
# # #
# # # for segment in segments:
# # #     segment.goto(1000,1000)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # screen.listen()
# # # screen.onkeypress(godown,"Up")
# # #
# # #
# # # screen.mainloop()
# #
# # # from tkinter import *
# # # import random
# # #
# # # GAME_WIDTH = 700
# # # GAME_HEIGHT = 700
# # # SPEED =50
# # # SPACE_SIZE =50
# # # BODY_PARTS =3
# # # SNACE_COLOR ="#00FF00"
# # # FOOD_COLOR = "#FF0000"
# # # BACKGROUND_COLOR = "#000000"
# # #
# # # #
# # # class Snake:
# # #     pass
# # #
# # # class Food:
# # #     pass
# # #
# # # def next_turn():
# # #     pass
# # #
# # # def change_direction(new_direction):
# # #     pass
# # #
# # # def game_over():
# # #     pass
# #
# #
# # # import turtle as t
# # #
# # # colors = ['red','cyan''green','yellow','white','orange']
# # #
# # # t.bgcolor("black")
# # # t.speed(0)
# # # for x in range(200):
# # #     t.pencolor(colors[x % 6])
# # #     t.forward(x)
# # #     t.left(59)
# # #
# # # t.hideturtle()
# # #
# # # t.done()
# #
# #
# # # import turtle as t
# # #
# # # t.bgcolor('black')
# # # t.speed(0)
# # # col = ('yellow','red','pink','cyan','light green','blue')
# # #
# # # for i in range(150):
# # #     t.pencolor(col[i%6])
# # #     t.circle(190-i/2,90)
# # #     t.lt(90)
# # #     t.circle(190-i/3,90)
# # #     t.lt(60)
# # # t.exitonclick()
# #
# #
# # # import turtle as t
# # # import colorsys
# # # t.bgcolor("black")
# # # t.speed(0)
# # # t.pensize(3)
# # # t.huc = 0.0
# # #
# # # for i in range(300):
# # #     color = colorsys.hsv_to_rgb()
# # #     t.pencolor(color)
# # #     t.huc = 0.005
# # #     t.right(i)
# # #     t.circle
# # #     t.fd(i)
# # #     t.left(91)
# #
# #
# # # import turtle
# # #
# # # sc = turtle.Screen()
# # # sc.title("Pong Game")
# # # sc.bgcolor("green")
# # # sc.setup(width=1000, height=600)
# # #
# # # # chap qanot
# # # left_pad = turtle.Turtle()
# # # left_pad.speed(0)
# # # left_pad.shape("square")
# # # left_pad.color("black")
# # # left_pad.shapesize(stretch_wid=8, stretch_len=2)
# # # left_pad.penup()
# # # left_pad.goto(-400, 0)
# # #
# # # # o'ng qanot
# # #
# # # right_pad = turtle.Turtle()
# # # right_pad.speed(0)
# # # right_pad.shape("square")
# # # right_pad.color("black")
# # # right_pad.shapesize(stretch_wid=8, stretch_len=2)
# # # right_pad.penup()
# # # right_pad.goto(400, 0)
# # #
# # # # Ball
# # # hit_ball = turtle.Turtle()
# # # hit_ball.speed(0)
# # # hit_ball.shape("circle")
# # # hit_ball.color("red")
# # # hit_ball.penup()
# # # hit_ball.goto(0, 0)
# # # hit_ball.dx = 5
# # # hit_ball.dy = -5
# # #
# # # # score
# # # left_player = 0
# # # right_player = 0
# # #
# # # # Display score
# # #
# # # sketch = turtle.Turtle()
# # # sketch.speed(0)
# # # sketch.color("blue")
# # # sketch.penup()
# # # sketch.hideturtle()
# # # sketch.goto(0, 260)
# # # sketch.write("Left_player : 0 / Right_player: 0",
# # #              align="center", font=("Courier", 24, "normal"))
# # #
# # #
# # # # Vertikat harakatlantirish
# # # def paddleaup():
# # #     y = left_pad.ycor()
# # #     y += 20
# # #     left_pad.sety(y)
# # #
# # #
# # # def paddleadown():
# # #     y = left_pad.ycor()
# # #     y -= 20
# # #     left_pad.sety(y)
# # #
# # #
# # # def padddleaup():
# # #     y = right_pad.ycor()
# # #     y += 20
# # #     right_pad.sety(y)
# # #
# # #
# # # def padddleadown():
# # #     y = right_pad.ycor()
# # #     y -= 20
# # #     right_pad.sety(y)
# # #
# # #
# # # sc.listen()
# # # sc.onkeypress(paddleaup, 'e')
# # # sc.onkeypress(paddleadown, 'x')
# # # sc.onkeypress(padddleaup, 'u')
# # # sc.onkeypress(padddleadown, 'm')
# # #
# # # while True:
# # #     sc.update()
# # #     hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
# # #     hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
# # #     if hit_ball.ycor()>280:
# # #         hit_ball.setx(-280)
# # #         hit_ball.dy*= -1
# # #
# # #     if hit_ball.xcor()<-280:
# # #         hit_ball.setx(-280)
# # #         hit_ball.dy *= -1
# # #
# # #     if hit_ball.xcor()>500:
# # #         hit_ball.goto(0,0)
# # #         hit_ball.dy *= -1
# # #         left_player += 1
# # #         sketch.clear()
# # #         sketch.write(f"Left Player:{left_player}/ Right player : {right_player}")
# # #
# # #     if hit_ball.xcor()<-500:
# # #         hit_ball.goto(0,0)
# # #         hit_ball.dy *= -1
# # #         right_player += 1
# # #         sketch.clear()
# # #         sketch.write(f"Left Player : {left_player}/ Right Player:{right_player}")
# # #
# # #     if (hit_ball.xcor()>360 and hit_ball.xcor()<370) and (
# # #             hit_ball.ycor()<right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() -40):
# # #         hit_ball.setx(360)
# # #         hit_ball.dx *= -1
# # #
# # #     if (hit_ball.xcor() < -360 and hit_ball.xcor() >-370) and (
# # #             hit_ball.ycor() <left_pad.ycor() +40 and hit_ball.ycor() >left_pad.ycor() -40):
# # #         hit_ball.setx(-360)
# # #         hit_ball.dx *= -1
# #
# #
# # # sc.mainloop()
# #
# #
# # # turtle.exitonclick()
# #
# # # import turtle
# # #
# # #
# # # pen = turtle.Turtle()
# # #
# # #
# # #
# # # def ring(col, rad):
# # #
# # #     pen.fillcolor(col)
# # #
# # #     pen.begin_fill()
# # #
# # #
# # #     pen.circle(rad)
# # #
# # #
# # #     pen.end_fill()
# # #
# # #
# # #
# # #
# # # pen.up()
# # # pen.setpos(-35, 95)
# # # pen.down
# # # ring('black', 15)
# # #
# # #
# # # pen.up()
# # # pen.setpos(35, 95)
# # # pen.down()
# # # ring('black', 15)
# # #
# # #
# # # pen.up()
# # # pen.setpos(0, 35)
# # # pen.down()
# # # ring('white', 40)
# # #
# # #
# # # pen.up()
# # # pen.setpos(-18, 75)
# # # pen.down
# # # ring('black', 8)
# # #
# # #
# # # pen.up()
# # # pen.setpos(18, 75)
# # # pen.down()
# # # ring('black', 8)
# # #
# # #
# # #
# # #
# # # pen.up()
# # # pen.setpos(-18, 77)
# # # pen.down()
# # # ring('white', 4)
# # #
# # #
# # # pen.up()
# # # pen.setpos(18, 77)
# # # pen.down()
# # # ring('white', 4)
# # #
# # #
# # # pen.up()
# # # pen.setpos(0, 55)
# # # pen.down
# # # ring('black', 5)
# # #
# # #
# # # pen.up()
# # # pen.setpos(0, 55)
# # # pen.down()
# # # pen.right(90)
# # # pen.circle(5, 180)
# # # pen.up()
# # # pen.setpos(0, 55)
# # # pen.down()
# # # pen.left(360)
# # # pen.circle(5, -180)
# # # pen.hideturtle()
# #
# #
# # # from turtle import *
# # #
# # # import random
# # #
# # # speed(speed='fastest')
# # #
# # #
# # # def draw(n, x, angle):
# # #
# # #     for i in range(n):
# # #
# # #         colormode(255)
# # #
# # #
# # #         a = random.randint(0, 255)
# # #         b = random.randint(0, 255)
# # #         c = random.randint(0, 255)
# # #
# # #
# # #         pencolor(a, b, c)
# # #         fillcolor(a, b, c)
# # #
# # #
# # #         begin_fill()
# # #
# # #
# # #         for j in range(5):
# # #             forward(5 * n - 5 * i)
# # #             right(x)
# # #             forward(5 * n - 5 * i)
# # #             right(72 - x)
# # #
# # #
# # #         end_fill()
# # #
# # #
# # #         rt(angle)
# # #
# # #
# # #
# # # n = 30
# # # x = 144
# # # angle = 18
# # #
# # # draw(n, x, angle)
# #
# #
# # # import turtle
# # # import turtle as t
# # #
# # #
# # # t.speed(8)
# # # turtle.bgcolor("pink")
# # #
# # # for i in range(2):
# # #     t.begin_fill()
# # #     t.fillcolor("yellow")
# # #     t.fd(210)
# # #     t.right(90)
# # #     t.forward(100)
# # #     t.rt(90)
# # #     t.end_fill()
# # # t.penup()
# # # t.setposition(30, 25)
# # # t.down()
# # # t.color("purple")
# # # t.left(90)
# # # t.width(5)
# # # t.fd(50)
# # # t.right(90)
# # # t.up()
# # # t.goto(70, 75)
# # # t.down()
# # # t.color("white")
# # # t.right(90)
# # # t.fd(50)
# # # t.penup()
# # # t.setposition(100, 75)
# # # t.down()
# # # t.color("dark gray")
# # # t.fd(50)
# # # t.up()
# # # t.setposition(130, 75)
# # # t.down()
# # # t.color("white")
# # # t.forward(50)
# # # t.up()
# # # t.setposition(160, 75)
# # # t.down()
# # # t.color("gray")
# # # t.forward(50)
# # # t.up()
# # # t.setposition(190, 75)
# # # t.down()
# # # t.color("purple")
# # # t.fd(50)
# # # t.up()
# # # turtle.home()
# # # t.down()
# # # t.hideturtle()
# # # t.textinput("Tug`ilgan kuning bilan!", "Ismingizni kiriting:")
# # # t.textinput("Tug`ilgan kuning bilan!", "Yoshingizni kiriting:")
# # # t.write("Tug`ilgan kuning bilan X")
# #
# #
# # # i = 0
# # # while i<1000:
# # #     i = i+1
# # #     t.fd(1+i*1)
# # #     t.right(90)
# #
# #
# # # for i in range(50):
# # #     t.width(20)
# # #     t.fd(15+15*i)
# # #     t.rt(90)
# #
# #
# # # import random as r
# # #
# # # t.getscreen()
# # #
# # # t.speed(1)
# # #
# # # list1 = ['classic','arrow','turtle','square','circle','triangle']
# # # t.shape(r.choice(list1))
# # #
# # #
# # # t.color('red')
# # # t.width(5)
# # # t.begin_fill()
# # # t.fillcolor("pink")
# # # t.circle(150)
# # # t.end_fill()
# # # t.up()
# # # t.setposition(0,75)
# # # t.down()
# # # t.begin_fill()
# # # t.fillcolor("yellow")
# # # t.circle(75)
# # # t.end_fill()
# # # t.up()
# # # t.setposition(0,-5)
# # # t.down()
# # # t.begin_fill()
# # # t.fillcolor("light green")
# # # t.width(7)
# # # t.color("dark green")
# # # t.left(270)
# # # t.forward(200)
# # # t.back(50)
# # # t.left(135)
# # # t.forward(75)
# # # t.left(135)
# # # t.forward(100)
# # # t.left(135)
# # # t.forward(70)
# # # t.hideturtle()
# # # t.end_fill()
#
#
# # t.Screen().setup(600,600,startx=200,starty=30)
# # t.bgpic("gullar.gif")
# # t.numinput("Salom", 'Telefon raqamingizni kiriting:')
# #
# # t.setposition(+20,210)
# # t.pendown()
# # t.width(1)
# # t.circle(3)
# # t.penup()
# # t.setposition(0,185)
# # t.pendown()
# # t.begin_fill()
# # t.fillcolor("orange")
# # t.width(3)
# # t.left(80)
# # t.forward(10)
# # t.left(90)
# # t.forward(10)
# # t.left(90)
# # t.forward(10)
# # t.left(90)
# # t.forward(10)
# # t.end_fill()
# # t.penup()
# # t.setposition(0,145)
# # t.pendown()
# # t.circle(3)
# # t.penup()
# # t.setposition(0,125)
# # t.pendown()
# # t.circle(3)
# # t.penup()
# # t.setposition(0,105)
# # t.pendown()
# # t.circle(3)
# # t.penup()
# # t.setposition(150,135)
# # t.pendown()
# # t.lt(125)
# # t.forward(135)
# # t.penup()
# # t.setposition(-150,135)
# # t.pendown()
# # t.lt(125)
# # t.forward(135)
# # t.hideturtle()
# # t.pencolor("white")
#
# #
# # # t.fd(180)
# # # t.rt(125)
# # # t.fd(200)
# # # t.rt(125)
# # # t.fd(180)
# # # t.rt(45)
# # # t.fd(45)
# # # t.rt(135)
# # # t.fd(50)
# # # t.left(135)
# # # t.fd(50)
# # # t.rt(135)
# # # t.fd(50)
# # # t.left(135)
# # # t.fd(50)
# # # t.rt(135)
# # # t.fd(50)
# # # t.left(135)
# # # t.fd(50)
# # # t.rt(135)
# # # t.fd(50)
# # # t.left(135)
# # # t.fd(50)
# # # t.rt(135)
# # # t.fd(50)
# # # .exitonclick()
# # import math
# # import tkinter
#
#
# from tkinter import *
# from openpyxl import *
#
# wb = load_workbook("C:\\Users\\asaly\\PycharmProjects\\pythonProject1\\data.xlsx")
# sheet = wb.active
#
# window = Tk()
#
# window.geometry("500x300")
#
# window.config(background="lime")
#
#
# # def focus_name(event):
# #     ism_get.focus_set()
#
#
# def focus_familiya(event):
#     familiya_get.focus_set()
#
#
# def focus_kurs(event):
#     kurs_get.focus_set()
#
#
# def focus_nomer(event):
#     nomer_get.focus_set()
#
#
# def focus_family_nomer(event):
#     ota_onasining_nomeri_get.focus_set()
#
#
# def focus_email(event):
#     email_get.focus_set()
#
#
# def focus_address(event):
#     address_get.focus_set()
#
#
# def clear():
#     ism_get.delete('0', END)
#
#
# def insert():
#     if (ism_get.get() == "" or
#             familiya_get.get() == "" or
#             kurs_get.get() == "" or
#             nomer_get.get() == "" or
#             ota_onasining_nomeri_get.get() == "" or
#             email_get.get() == "" or
#             address_get.get() == ""):
#         print("To`ldirilmagan qator mavjud!")
#
#     else:
#         current_row = sheet.max_row
#         current_column = sheet.max_column
#         sheet.cell(row=1, column=1).value = "Ism"
#         sheet.cell(row=1, column=2).value = "Familiya"
#         sheet.cell(row=1, column=3).value = "Kurs"
#         sheet.cell(row=1, column=4).value = "Telefon raqam"
#         sheet.cell(row=1, column=5).value = "Ota-onasing nomeri"
#         sheet.cell(row=1, column=6).value = "Email"
#         sheet.cell(row=current_row + 1, column=1).value = ism_get.get()
#         sheet.cell(row=current_row + 1, column=2).value = familiya_get.get()
#         sheet.cell(row=current_row + 1, column=3).value = kurs_get.get()
#         sheet.cell(row=current_row + 1, column=4).value = nomer_get.get()
#         sheet.cell(row=current_row + 1, column=5).value = ota_onasining_nomeri_get.get()
#         sheet.cell(row=current_row + 1, column=6).value = email_get.get()
#         sheet.cell(row=current_row + 1, column=7).value = address_get.get()
#         wb.save("C:\\Users\\asaly\\PycharmProjects\\pythonProject1\\data5.xlsx")
#
#
# forma = Label(text="Forma")
# forma.place(x=250, y=0)
#
# ism = Label(text="Ism")
# ism.place(x=10, y=20)
#
# ism_get = Entry()
# ism_get.place(x=150, y=20)
#
# familiya = Label(text="Familiya")
# familiya.place(x=10, y=50)
#
# familiya_get = Entry()
# familiya_get.place(x=150, y=50)
#
# kurs = Label(text="Kurs")
# kurs.place(x=10, y=80)
#
# kurs_get = Entry()
# kurs_get.place(x=150, y=80)
#
# nomer = Label(text="Telefon raqami")
# nomer.place(x=10, y=110)
#
# nomer_get = Entry()
# nomer_get.place(x=150, y=110)
#
# ota_onasining_nomeri = Label(text="Ota-onasining telefoni")
# ota_onasining_nomeri.place(x=10, y=140)
#
# ota_onasining_nomeri_get = Entry()
# ota_onasining_nomeri_get.place(x=150, y=140)
#
# email = Label(text="Email")
# email.place(x=10, y=170)
#
# email_get = Entry()
# email_get.place(x=150, y=170)
#
# address = Label(text="Address")
# address.place(x=10, y=200)
#
# address_get = Entry()
# address_get.place(x=150, y=200)
#
# toldirish = Button(text="To`ldirish", background="red", command=insert)
# toldirish.place(x=250, y=230)
#
# mainloop()
#
# # """#        # WIDTH = 600#"""
# # #        # HEIGHT = 600
# #         #
# #         # canvas = Canvas(window, width=WIDTH, height=HEIGHT)
# #         # canvas.pack()
# #         #
# #         # text = canvas.create_text(WIDTH - 300, HEIGHT - 20, text="Harakatlanish uchun --> w, s, a, d", font=5)
# #         #
# #         # player = canvas.create_rectangle
# #         #
# #         # x1 = WIDTH / 2
# #         # y1 = HEIGHT / 2
# #         # player(x1, y1, x1 - 10, y1 - 10, fill='green')
# #         #
# #         #
# #         # def draw_up():
# #         #     player(x1, y1, x1 - 10, y1 - 10, fill='green')
# #         #
# #         #
# #         # def del_up():
# #         #     player(x1, y1, x1 - 10, y1 - 10, fill='white')
# #         #
# #         #
# #         # def harakatlanish(event):
# #         #     global x1, y1
# #         #     print(event.keysym)
# #         #
# #         #     if event.keysym == "Up":
# #         #         del_up()
# #         #         y1 -= 10
# #         #
# #         #     if event.keysym == "Down":
# #         #         del_up()
# #         #         y1 += 10
# #         #
# #         #     if event.keysym == "Right":
# #         #         del_up()
# #         #         x1 += 10
# #         #
# #         #     if event.keysym == "Left":
# #         #         del_up()
# #         #         x1 -= 10
# #         #     draw_up()
# #         #
# #         #
# #         # window.bind("<Key>", harakatlanish)
# #
# #         # window.mainloop()
# #
# #         # canvas.create_line(10, 10, 200, 10, 200, 150, 10, 150, 10, 10)
# #         # canvas.create_rectangle(10, 50, 110, 100, fill="blue", width=10)
# #         # canvas.create_oval(100, 50, 110, 100)
# #         # canvas.create_text(200, 200, text="Hello", font=300, fill="blue")
# #         # canvas.create_rectangle(10, 100, 110, 150, fill="blue", width=10)
# #         # canvas.create_rectangle(110, 50, 220, 100, fill="green", width=10)
# #
# #         # canvas.create_oval(100, 50, 300, 240, outline="red", width=20)
# #         # canvas.create_text(200, 150, text="80", font='Arial 70 bold', fill="black")
# #
# #         # canvas.create_oval(100, 50, 300, 240, outline="red", width=20)
# #         # canvas.create_text(200, 150, text="6 t", font='Arial 70 bold', fill="black")
# #
# #         #
# #         # canvas.create_rectangle(10, 100, 150, 250, fill="dark blue", width=5)
# #         # canvas.create_text(75, 160, text="P", font='Arial 40 bold', fill="white")
# #         # canvas.create_text(75, 190, text="reserved", font='Arial 20 bold', fill="white")
# #
# #         # canvas.create_rectangle(10, 100, 150, 250, fill="dark blue", width=5)
# #         # canvas.create_text(75, 160, text="H", font='Arial 40 bold', fill="white")
# #         # canvas.create_text(75, 195, text="HOSPITAL", font='Arial 15 bold', fill="white")
# #
# #         #                       Uyga vazifa                             #
#
# """l1 = Label(window, text="Ildizni topish uchun son kiriting", font=20)
#         l1.place(x=80, y=20)
#
#         entry1 = Entry(window, bg="white")
#         entry1.place(x=100, y=60)
#
#         def get_sqrt(event):
#             number = entry1.get()
#
#             l2 = Label(window, text=f"{number} ning ildizi: ")
#             l2.place(x=160, y=200)
#
#             l3 = Label(window, text=f"{float(math.sqrt(int(number)))}")
#             l3.place(x=200, y=230)
#
#         entry1.bind("<Return>", get_sqrt)"""
#
# # def handle_click(event):
# #     print(event.char)
# #
# #
# # def log(event):
# #     Label(window, text=f"You pressed: {event.char}").pack()
# #
# #
# # button = Button(window, text="Button")
# #
# # button.bind("<Key>", log)
# # button.focus()
# # button.pack(expand=True)
#
# # def entry_data():
# #     print(enter_name.get())
# #     print(last_nam.get())
# #     print(jins.get())
# #     print(enter_age.get())
# #     print(millat.get())
# #     print(sp1.get())
# #
# #
# # name = Label(text="First Name")
# # name.place(x=50, y=30)
# #
# # enter_name = Entry()
# # enter_name.place(x=30, y=50)
# #
# # last_name = Label(text="Last name")
# # last_name.place(x=250, y=30)
# #
# # last_nam = Entry()
# # last_nam.place(x=230, y=50)
# #
# # title = Label(text="Title")
# # title.place(x=450, y=30)
# #
# # m = tkinter.StringVar()
# # jins = ttk.Combobox(window, width=19, textvariable=m)
# #
# # jins["values"] = ("qiz bola", "o'g'il bola", "Ayol", "Erkak")
# # jins.place(x=400, y=50)
# #
# #
# # age = Label(text="Age")
# # age.place(x=75, y=100)
# #
# # n = tkinter.StringVar()
# # enter_age = ttk.Combobox(window, width=19, textvariable=n)
# #
# # enter_age["values"] = ('10', '11', '12', '13', '14', '14', '15', '16 ', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30')
# # enter_age.place(x=20, y=130)
# #
# # nationality = Label(text="Nationality")
# # nationality.place(x=250, y=100)
# #
# # l = tkinter.StringVar()
# # millat = ttk.Combobox(window, width=19, textvariable=l)
# #
# # millat["values"] = ("O'zbek", "English", "Rus", "Qazaq", "Nemis", "Turk", "Hind", "Hitoy", "Arab", "American", "Koreys",
# #                     "Qirg'iz", "Tojik")
# # millat.place(x=240, y=130)
# #
# # status = Label(text="Registation Status")
# # status.place(x=30, y=200)
# #
# # registratsiya = Checkbutton(text="Currently Registered")
# # registratsiya.place(x=20, y=230)
# #
# # courses = Label(text="# Completed Courses")
# # courses.place(x=250, y=200)
# #
# # sp1 = Spinbox(window, from_=0, to=30)
# # sp1.place(x=240, y=230)
# #
# # semesters = Label(text="# Semesters")
# # semesters.place(x=500, y=200)
# #
# # sp2 = Spinbox(window, from_=0, to=30)
# # sp2.place(x=460, y=230)
# #
# # accept = Checkbutton(text="I accept the terms and conditions.")
# # accept.place(x=20, y=300)
# #
# # enter_data = Button(text="Enter data", width=80, height=1, command=entry_data)
# # enter_data.place(x=20, y=380)
#
# mainloop()
############################################################################
import tkinter
from tkinter import messagebox, simpledialog, filedialog

# messagebox.showinfo("Axborot", "Bu axborotli xabar")
# messagebox.showerror("Xato", "Bu xato xabar")
# messagebox.showwarning("Ogohlantirish", "Bu ogohlantiruvchi xabar")

# messagebox.askquestion("Savol", "Bu ogohlantiruvchi xabar")           #Yes \ no
# messagebox.askokcancel("Savol", "Bu ogohlantiruvchi xabar")            # Yes \ cannel
# messagebox.askretrycancel("Savol", "Bu ogohlantiruvchi xabar")           # Retry \ cannel
# messagebox.askyesno("Savol", "Bu ogohlantiruvchi xabar")                 # Bu ham yes \ no
# messagebox.askyesnocancel("Savol", "Bu ogohlantiruvchi xabar")                 # Yes \ no \ Cannel

# response = messagebox.askyesnocancel("Savol", "Siz chiqmoqchimisiz")
# value = simpledialog.askfloat("Question", "Dars necha soat davom etadi?")
# print(value)

# mevalar = ['uzum', 'olma', 'nok', 'anor', 'gilos']
#
# value = simpledialog.askstring("Question", "Meva kiriting:")
#
# if value in mevalar:
#     print("Bizda bor")
#
# else:
#     print(f"{value} Bizda yo'q")

# filename = filedialog.askopenfilename(title="Faylni ochish", filetypes=[('*txttext', "*png")])


# sorov = simpledialog.askstring("Savol", "Ismingiz nima:")
# value = simpledialog.askfloat("Question", "Dars qachon boshlanadi:")
# yil = simpledialog.askinteger("Question", "Yoshingiz nechi:")


from tkinter import *

window = Tk()
window.geometry("400x500")

write = Label(text="Add products", height=20, width=20)
write.place()
# filename = filedialog.asksaveasfilename(title="Save", filetypes=[('Text File', "*txt")], defaultextension='.txt')
# if filename:
#     with open(filename, 'w') as file:
#         file.write(f" Ismi: {sorov} "
#                    f" \n Dars vaqti: {value} "
#                    f"\n Yoshi: {yil}")
#         print(f"File saqlandi")
# else:
    # print("Bekor qilindi!")


mainloop()
# value = simpledialog.askinteger("Question", "Nechanchi yilsiz?")
# print(value)

# window.config(menu=my_menu)
#
#
# def on_open():
#     file_path = filedialog.askopenfilename()
#     print("Selected file", file_path)
#
#
# file_menu = Menu(my_menu, tearoff=0)
# my_menu.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New File')
#
# file_menu.add_command(label='Open', command=on_open, accelerator="Ctrl+O")
#
# file_menu.add_separator()
# file_menu.add_command(label='Exit', command=window.quit)
#
# sub_menu = Menu(file_menu, tearoff=0)
#
# sub_menu.add_command(label='Color Themes')
#
# file_menu.add_cascade(label='Preferences', menu=sub_menu)

# mainloop()
