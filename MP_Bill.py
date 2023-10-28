from tkinter import *

weight,height = (500,500)


# def verify():
#     get_ans1 = answer1.get()
#     get_ans2 = answer2.get()
#     if get_ans1 == "" and get_ans2 == "" :
#         lbl4.configure(text="!لطفا اطلاعات خود را کامل کنید")
#         lbl4.place(x=(weight/2)-140,y=(height/2)+185)
#     elif get_ans1 == "":
#         lbl4.configure(text="!لطفا نام کاربری خود را وارد کنید")
#         lbl4.place(x=(weight/2)-150,y=(height/2)+185)
#     elif get_ans2 == "":
#         lbl4.configure(text="!لطفا شماره موبایل خود را وارد کنید")
#         lbl4.place(x=(weight/2)-155,y=(height/2)+185)
#     elif len(get_ans2) < 11 :
#         lbl4.configure(text="!لطفا شماره موبایل خود را به درستی وارد کنید")
#         lbl4.place(x=(weight/2)-210,y=(height/2)+185)
#     else:
#         page2()

def delete():
    answer1.delete(0,END)
    answer2.delete(0,END)
    btn.destroy()
    page2()

def page2():
    lbl1.destroy()
    win.geometry("500x600")
    lbl2.config(text="زمان مکالمه",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    lbl2.place(x=(weight/5)+90,y=(height/5)-90)
    answer1.config(width=40,justify="center",font=("B Nazanin Bold",15))
    answer1.place(x=(weight/3)-57,y=(height/5)-30)
    
    lbl3.config(text="زمان اینترنت مصرفی",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    lbl3.place(x=(weight/5)+50,y=(height/5)+15)
    answer2.config(width=40,justify="center",font=("B Nazanin Bold",15))
    answer2.place(x=(weight/3)-57,y=(height/5)+80)
    
    lbl4 = Label(win,text="تعداد پیامک داده شده",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    lbl4.place(x=(weight/3)-20,y=(height/3)+60)
    answer3 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
    answer3.place(x=(weight/3)-57,y=(height/3)+120)
    
    lbl4 = Label(win,text="تعداد پیامک داده شده",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    lbl4.place(x=(weight/3)-20,y=(height/3)+60)
    answer3 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
    answer3.place(x=(weight/3)-57,y=(height/3)+120)
    
    btn2 = Button(win,text="تایید",width=8,fg="white",bg="green",font=("B Nazanin Bold",20),command=check)
    btn2.place(x=(weight/2)-73,y=(height/2)+180)
    
    
def check():
    print("hello")



win = Tk()
win.title("قبض پرداختی موبایل")
win.config(bg="#00FFF7")
win.geometry(str(weight)+"x"+str(height))
win.resizable(0,0)

lbl1 = Label(win,text="خوش آمدید",fg="Green",bg="#00FFF7",font=("B Nazanin Bold",40))
lbl1.pack()


lbl2 = Label(win,text="نام کاربری",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
lbl2.place(x=(weight/3)+26,y=(height/3)-50)
answer1 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
answer1.place(x=(weight/3)-57,y=(height/3)+10)

lbl3 = Label(win,text="شماره موبایل",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
lbl3.place(x=(weight/3)+20,y=(height/3)+60)
answer2 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
answer2.place(x=(weight/3)-57,y=(height/3)+120)

btn = Button(win,text="تایید",width=8,fg="white",bg="green",font=("B Nazanin Bold",20),command=delete)
btn.place(x=(weight/2)-73,y=(height/2)+100)

lbl4 = Label(win,text="",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))





win.mainloop()
