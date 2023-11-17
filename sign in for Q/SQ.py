from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image



def delete():
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    khas()



def sar():
    pass

def khas():
    win.geometry("600x600")
    ans1 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    ans1.pack(side=(TOP))
    lbl1 = Label(win, text=" :نام", font=("B Nazanin Bold", 15))
    lbl1.pack(TOP)
    # ans2 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    # ans2.place(x=250, y=10)
    # lbl2 = Label(win, text=":نام خانوادگی", font=("B Nazanin Bold", 15))
    # lbl2.place(x=350, y=10)
    # ans3 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    # ans3.place(x=430, y=45)
    # lbl3 = Label(win, text=":نام پدر", font=("B Nazanin Bold", 15))
    # lbl3.place(x=530, y=45)
    # ans4 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    # ans4.place(x=250, y=45)
    # lbl4 = Label(win, text=":محل تولد", font=("B Nazanin Bold", 15))
    # lbl4.place(x=350, y=45)
    # ans5 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    # ans5.place(x=400, y=80)
    # lbl5 = Label(win, text=":ش.شناسنامه", font=("B Nazanin Bold", 15))
    # lbl5.place(x=510, y=80)
    # ans6 = Entry(win, width=10, justify="center", font=("B Nazanin Bold", 15))
    # ans6.place(x=250, y=80)
    # lbl6 = Label(win, text=":ش ملی", font=("B Nazanin Bold", 15))
    # lbl6.place(x=350, y=80)
    # ans7 = Entry(win, width=15, justify="center", font=("B Nazanin Bold", 15))
    # ans7.place(x=10, y=80)
    # lbl7 = Label(win, text=":تاریخ تولد", font=("B Nazanin Bold", 15))
    # lbl7.place(x=150, y=80)
    # ans8 = Entry(win, width=15, justify="center", font=("B Nazanin Bold", 15))
    # ans8.place(x=400, y=120)
    # lbl8 = Label(win, text=":آدرس", font=("B Nazanin Bold", 15))
    # lbl8.place(x=550, y=120)
    # ans9 = Entry(win, width=15, justify="center", font=("B Nazanin Bold", 15))
    # ans9.place(x=400, y=160)
    # lbl9 = Label(win, text=":تلفن", font=("B Nazanin Bold", 15))
    # lbl9.place(x=550, y=160)
    # ans10 = Entry(win, width=15, justify="center", font=("B Nazanin Bold", 15))
    # ans10.place(x=400, y=200)
    # lbl10 = Label(win, text=":موبایل", font=("B Nazanin Bold", 15))
    # lbl10.place(x=550, y=200)
    # ans11 = Entry(win, width=15, justify="center", font=("B Nazanin Bold", 15))
    # ans11.place(x=400, y=240)
    # lbl11 = Label(win, text=":ایمیل", font=("B Nazanin Bold", 15))
    # lbl11.place(x=550, y=240)
    # my_label = Label(win,text="")
    # my_label.pack()
    def myClick():
        link = askopenfilename()
        my_img = ImageTk.PhotoImage(Image.open(link))
        my_label.configure(image=my_img)
        my_label.image = my_img
    btn_add_photo = Button(win, text="انتخاب عکس", command=myClick)
    btn_add_photo.place(x=400, y=280)
    btn = Button(win,text ="ثبت نام",command=sar)
    btn.place(x=300,y=400)

def inter():
    pass

def k2k():
    pass


win = Tk()
win.geometry("400x400")
win.title("")
win.configure(bg="03001C")
win.resizable(0,0)


################ Widgets #####################

lbl_choice = Label(win,text="نوع آزمون را انتخاب کنید",font=("B Nazanin Bold", 20))
btn2 = Button(win,text ="سراری",width=13,font=("B Nazanin Bold", 15),command=sar)
btn3 = Button(win,text ="بین المللی",width=13,font=("B Nazanin Bold", 15),command=inter)
btn4 = Button(win,text ="کاردانی به کارشناسی",width=13,font=("B Nazanin Bold", 15),command=k2k)
btn5 = Button(win,text ="خاص",width=13,font=("B Nazanin Bold", 15),command=delete)

############### Widgets place #################

lbl_choice.place(x=80,y=0)
btn2.place(x=30,y=60)
btn3.place(x=220,y=60)
btn4.place(x=30,y=130)
btn5.place(x=220,y=130)


win.mainloop()