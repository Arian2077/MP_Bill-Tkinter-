from tkinter import *
from tkinter import messagebox
import pygame
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image

#I used pygame for making Buttom's sound effect and pic_get for submit section
pygame.mixer.init()
pic_get = False

'''after clicking on submit (ثبت نام) buttom , the program will send all of your informations to this section
then it checks that did you fill all of the sections or you didn't '''
def submit():
    print(pic_get)
    lst_give = [ans1,ans2,ans3,ans4,ans5,ans6,ans7_1,ans7_2,ans7_3,ans8,ans9,ans10,ans11] 
    lst_get=[]
    for i in range(0,12):
        lst_get.append(lst_give[i].get())
    if "" in lst_get :
        messagebox.showerror("!اخطار","لطفا برای ثبت نام تمام بخش ها را پر کنید")
    elif pic_get == False:
        messagebox.showerror("!اخطار","لطفا عکس خود را وارد کنید")
    else:
        messagebox.showinfo("تبریک","ثبت نام شما با موفقیت انجام شد")
        win.quit()

#it will delete all the widgets of previous page
def delete():
    pygame.mixer.music.load("Sound Effect/button-124476.mp3")
    pygame.mixer.music.play(loops=0)
    lbl_choice.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    khas()

def sar():
    pygame.mixer.music.load("Sound Effect/button-124476.mp3")
    pygame.mixer.music.play(loops=0)

def khas():
    global ans1,ans2,ans3,ans4,ans5,ans6,ans7_1,ans7_2,ans7_3,ans8,ans9,ans10,ans11,pic_get
    win.geometry("600x500")
    win.configure(bg="#301E67")
    # get the photo from the path you choose then resize it to 100x100 and show it for you
    def myClick():
        global pic_get
        pygame.mixer.music.load("Sound Effect/button-124476.mp3")
        pygame.mixer.music.play(loops=0)
        link = askopenfilename()
        my_img = Image.open(link)
        resize_img = my_img.resize((100,100))
        img = ImageTk.PhotoImage(resize_img)
        pic.configure(image=img)
        pic.image = img
        pic_get = True
    
    ################## Labels #######################
    lbl1 = Label(win, text=" :نام",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl2 = Label(win, text=":نام خانوادگی",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl3 = Label(win, text=":نام پدر",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl4 = Label(win, text=":محل تولد",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl5 = Label(win, text=":ش.شناسنامه",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl6 = Label(win, text=":ش.ملی",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl7_1 = Label(win, text=":تاریخ تولد",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl7_2 = Label(win, text="/",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl7_3 = Label(win, text="/",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl8 = Label(win, text=":آدرس",fg="#B6EADA",bg="#301E67", font=("B Nazanin Bold", 15))
    lbl9 = Label(win, text=":تلفن",fg="#B6EADA",bg="#301E67",  font=("B Nazanin Bold", 15))
    lbl10 = Label(win, text=":موبایل",fg="#B6EADA",bg="#301E67",  font=("B Nazanin Bold", 15))
    lbl11 = Label(win, text=":ایمیل",fg="#B6EADA",bg="#301E67",  font=("B Nazanin Bold", 15))
    
    ################## Entries #######################
    ans1 = Entry(win, width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
    ans2 = Entry(win, width=20,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans3 = Entry(win,width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
    ans4 = Entry(win, width=20,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans5 = Entry(win,  width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
    ans6 = Entry(win, width=20,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans7_1 = Entry(win, width=5,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans7_2 = Entry(win, width=5,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans7_3 = Entry(win, width=5,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans8 = Entry(win, width=20,fg="#B6EADA",bg="#5B8FB9", justify="center", font=("B Nazanin Bold", 15))
    ans9 = Entry(win,  width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
    ans10 = Entry(win,  width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
    ans11 = Entry(win,  width=20,fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15))
     
    ################## location of Labels #######################
    lbl1.place(x=490,y=10)
    lbl2.place(x=230,y=10)
    lbl3.place(x=490, y=70)
    lbl4.place(x=230,y=70)
    lbl5.place(x=490, y=130)
    lbl6.place(x=230, y=130)
    lbl7_1.place(x=490, y=190)
    lbl7_2.place(x=435,y=190)
    lbl7_3.place(x=373,y=190)
    lbl8.place(x=230, y=190)
    lbl9.place(x=490, y=250)    
    lbl10.place(x=230, y=250)
    lbl11.place(x=490, y=310)
    
    ################## location of Entries #######################
    ans1.place(x=340,y=10)
    ans2.place(x=80,y=10)
    ans3.place(x=340, y=70)
    ans4.place(x=80,y=70)
    ans5.place(x=340, y=130)
    ans6.place(x=80, y=130)
    ans7_1.place(x=450, y=190)
    ans7_2.place(x=390, y=190)
    ans7_3.place(x=330, y=190)
    ans8.place(x=80, y=190)
    ans9.place(x=340, y=250)
    ans10.place(x=80, y=250)
    ans11.place(x=340, y=310)

    pic = Label(win,text="",fg="#B6EADA",bg="#301E67", )
    pic.place(x=100,y=360)
    btn1 = Button(win,width=17,text="انتخاب عکس",fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 10),command=myClick)
    btn1.place(x=80,y=310)
    
    btn2 = Button(win,text="ثبت نام",fg="#B6EADA",bg="#5B8FB9",justify="center", font=("B Nazanin Bold", 15),command=submit)
    btn2.place(x=260,y=400)

def inter():
    pygame.mixer.music.load("Sound Effect/button-124476.mp3")
    pygame.mixer.music.play(loops=0)

def k2k():
    pygame.mixer.music.load("Sound Effect/button-124476.mp3")
    pygame.mixer.music.play(loops=0)
    
win = Tk()
win.geometry("400x200")
win.title("ثبت نام آزمون")
win.configure(bg="#03001C")
win.resizable(0,0)

################ Widgets #####################

lbl_choice = Label(win,fg="#B6EADA",bg="#03001C",text="نوع آزمون را انتخاب کنید",font=("B Nazanin Bold", 20))
btn2 = Button(win,fg="#B6EADA",bg="#5B8FB9",text ="سراری",width=13,font=("B Nazanin Bold", 15),command=sar)
btn3 = Button(win,fg="#B6EADA",bg="#5B8FB9",text ="بین المللی",width=13,font=("B Nazanin Bold", 15),command=inter)
btn4 = Button(win,fg="#B6EADA",bg="#5B8FB9",text ="کاردانی به کارشناسی",width=13,font=("B Nazanin Bold", 15),command=k2k)
btn5 = Button(win,fg="#B6EADA",bg="#5B8FB9",text ="خاص",width=13,font=("B Nazanin Bold", 15),command=delete)

############### Widgets place #################

lbl_choice.place(x=80,y=0)
btn2.place(x=25,y=60)
btn3.place(x=215,y=60)
btn4.place(x=25,y=130)
btn5.place(x=215,y=130)


win.mainloop()
