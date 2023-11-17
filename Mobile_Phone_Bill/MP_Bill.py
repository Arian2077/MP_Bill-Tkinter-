from tkinter import *

weight,height = (500,500)

def delete():
    lbl1.destroy()
    lbl2.destroy()
    lbl3.destroy()
    lbl4.destroy()
    answer1.destroy()
    answer2.destroy()
    btn.destroy()
    btn_quit.destroy()
    info()

    
def delete2():
    info_lbl1.destroy()
    info_lbl2.destroy()
    info_lbl3.destroy()
    info_lbl4.destroy()
    info_lbl5.destroy()
    btn_next.destroy()
    page2()

def delete3():
    page2_answer1.destroy()
    page2_answer2.destroy()
    page2_answer3.destroy()
    page2_answer4.destroy()
    page2_lbl1.destroy()
    page2_lbl2.destroy()
    page2_lbl3.destroy()
    page2_lbl4.destroy()
    btn2.destroy()
    final_report()

def info():
    global info_lbl1,info_lbl2,info_lbl3,info_lbl4,info_lbl5,btn_next
    win.geometry("550x450")
    win.config(bg="black")
    
    info_lbl1 = Label(win,text=("***راهنما***"),fg="green",bg="black",font=("B Nazanin Bold",40))
    info_lbl1.pack(pady=15)
    
    info_lbl2 = Label(win,text=("هر دقیقه مکالمه = 10 تومن"),fg="#00FFF7",bg="black",font=("B Nazanin Bold",20))
    info_lbl2.pack(pady=5)
    
    info_lbl3 = Label(win,text=(" هر دقیقه استفاده از اینترنت با تعرفه معمولی = 18 تومن"),fg="#00FFF7",bg="black",font=("B Nazanin Bold",20))
    info_lbl3.pack(pady=5)
    
    info_lbl4 = Label(win,text=("هر پیامک = 5 تومن"),fg="#00FFF7",bg="black",font=("B Nazanin Bold",20))
    info_lbl4.pack(pady=5)
    
    info_lbl5 = Label(win,text=("هر دقیقه پیام صوتی = 5 تومن"),fg="#00FFF7",bg="black",font=("B Nazanin Bold",20))
    info_lbl5.pack(pady=5)
    
    btn_next = Button(win,text="بعدی",width=8,fg="white",bg="green",font=("B Nazanin Bold",20),command=delete2)
    btn_next.pack(pady=15)
    
    
def page1():
    global name,number
    win.geometry("500x500")
    win.config(bg="#00FFF7")
    name = answer1.get()
    number = answer2.get()
    if name == "" and number == "" :
        lbl4.configure(text="!لطفا اطلاعات خود را کامل کنید")
        lbl4.place(x=(weight/2)-140,y=(height/2)+185)
    elif name == "":
        lbl4.configure(text="!لطفا نام کاربری خود را وارد کنید")
        lbl4.place(x=(weight/2)-150,y=(height/2)+185)
    elif number == "":
        lbl4.configure(text="!لطفا شماره موبایل خود را وارد کنید")
        lbl4.place(x=(weight/2)-155,y=(height/2)+185)
    elif len(number) != 11 :
        lbl4.configure(text="!لطفا شماره موبایل خود را به درستی وارد کنید")
        lbl4.place(x=(weight/2)-210,y=(height/2)+185)
    else:
        delete()

def page2():
    global page2_answer1,page2_answer2,page2_answer3,page2_answer4,page2_lbl1,page2_lbl2,page2_lbl3,page2_lbl4,btn2
    win.geometry("500x550")
    win.config(bg="#00FFF7")
    
    page2_lbl1 = Label(text="زمان مکالمه",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    page2_lbl1.place(x=(weight/5)+90,y=(height/5)-90)
    page2_answer1 = Entry(width=40,justify="center",font=("B Nazanin Bold",15))
    page2_answer1.place(x=(weight/3)-57,y=(height/5)-30)
    
    page2_lbl2 = Label(text="زمان اینترنت مصرفی",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    page2_lbl2.place(x=(weight/5)+50,y=(height/5)+15)
    page2_answer2 = Entry(width=40,justify="center",font=("B Nazanin Bold",15))
    page2_answer2.place(x=(weight/3)-57,y=(height/5)+80)
    
    page2_lbl3 = Label(win,text="تعداد پیامک داده شده",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    page2_lbl3.place(x=(weight/3)-20,y=(height/3)+60)
    page2_answer3 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
    page2_answer3.place(x=(weight/3)-57,y=(height/3)+120)
    
    page2_lbl4 = Label(win,text="دقایق ارسال پیام صوتی",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))
    page2_lbl4.place(x=(weight/3)-30,y=(height/2)+85)
    page2_answer4 = Entry(win,width=40,justify="center",font=("B Nazanin Bold",15))
    page2_answer4.place(x=(weight/3)-57,y=(height/2)+140)
    
    btn2 = Button(win,text="تایید",width=8,fg="white",bg="green",font=("B Nazanin Bold",20),command=check)
    btn2.place(x=(weight/2)-73,y=(height/2)+200)



    
    
def check():
    global v1,v2,v3,v4,talk,report,internet,sms,voice,subscription
    try:
        v1 = int(page2_answer1.get())
    except ValueError :
        v1 = 0
    try:
       v2 = int(page2_answer2.get())
    except ValueError :
        v2 = 0
    try:
        v3 = int(page2_answer3.get())
    except ValueError :
        v3 = 0
    try:
        v4 = int(page2_answer4.get())
    except ValueError :
        v4 = 0    
    if v1 == 0 and v2 == 0 and  v3 == 0 and v4 == 0 :
        pass
    talk = v1 * 10
    internet = v2 * 18
    sms = v3 * 5
    voice = v4 * 5
    subscription = 150
    report = talk + internet + sms + voice + subscription
    delete3()
    
def final_report():
    win.configure(bg="black")
    win.geometry("400x550")
    
    report_name = Label(text=("نام کاربری = "+ name),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_name.pack(pady=5)
    
    report_number = Label(text=("شماره موبایل = "+ number),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_number.pack(pady=5)
    
    report_lbl1 = Label(text=("مکالمه = "+str(talk)),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_lbl1.pack(pady=5)
    
    report_lbl2 = Label(text=("اینترنت با تعرفه عادی = "+str(internet)),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_lbl2.pack(pady=5)
    
    report_lbl3 = Label(win,text=("پیامک = "+str(sms)),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_lbl3.pack(pady=5)
    
    report_lbl4 = Label(win,text=("پیام صوتی = "+str(voice)),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_lbl4.pack(pady=5)
    
    report_lbl5 = Label(win,text=("آبونمان = "+str(subscription)),fg="yellow",bg="black",font=("B Nazanin Bold",20))
    report_lbl5.pack(pady=5)
    
    report_lbl6 = Label(win,text=("صورت حساب نهایی = "+str(report)+" تومان"),fg="green",bg="black",font=("B Nazanin Bold",20))
    report_lbl6.pack(pady=5)
    
    
    btn3 = Button(win,text="خروج",width=8,fg="white",bg="red",font=("B Nazanin Bold",20),command=win.destroy)
    btn3.pack(pady=5)


win = Tk()
win.title("قبض تلفن همراه")
win.config(bg="#00FFF7")
win.geometry("500x500")
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

btn = Button(win,text="شروع",width=8,fg="white",bg="green",font=("B Nazanin Bold",20),command=page1)
btn.place(x=(weight/2)-73,y=(height/2)+100)

btn_quit = Button(win,text="خروج",width=4,fg="white",bg="red",font=("B Nazanin Bold",20),command=win.destroy)
btn_quit.place(x=(weight/2)+125,y=(height/2)+100)

lbl4 = Label(win,text="",fg="Red",bg="#00FFF7",font=("B Nazanin Bold",20))


win.mainloop()