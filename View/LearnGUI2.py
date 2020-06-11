from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from tkinter import ttk
from  View.GUiCustomer import main
from View.GUIRoom import  main1
from View.GUIBAction import main3
from tkinter import messagebox as mb
from PIL import  ImageTk,Image
from  View.feedBackCustomer import main4
date=datetime.datetime.now().date()
date=str(date)
time=datetime.datetime.now().time()
time=str(time)
class App(object):
    def __init__(self,master):
        self.master=master
        #--Frame
        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottow=Frame(master,height=500,bg="#99ccff")
        self.bottow.pack(fill=X)
        # top frame design
        self.top_icon_label1=Label(self.top,text="AndTee's Hotel",font="arial 25 underline bold italic",bg='white',fg='#004d99')
        self.top_icon_label1.place(x=230,y=50)
        self.date=Label(self.top,text="Today is:"+date+"Time:"+time,font="arial 12 italic",fg="black",bg="#eff5f5")
        self.date.place(x=605,y=120)
        # self.img=ImageTk.PhotoImage(Image.open("View\\iconnha.ico","r"))
        # self.bottow_lb=Label(self.top,image=self.img).place(x=20,y=20)
        # bottow frame design
        self.bottow_btnCustomer=Button(self.bottow,text="Data Customer",width=15,font="arial 12 underline bold italic",fg="#004d99",bg="white",bd=4,command=self.datacus)
        self.bottow_btnCustomer.place(x=20,y=50)
        self.bottow_btnRoom = Button(self.bottow, text="Data Room", width=15, font="arial 12 underline bold italic", fg="#004d99",
                                         bg="white", bd=4,command=self.dataroom)
        self.bottow_btnRoom.place(x=20, y=100)
        self.bottow_btnAction = Button(self.bottow, text="Business activities", width=15, font="arial 12 underline bold italic", fg="#004d99",
                                         bg="white", bd=4,command=self.Baction)
        self.bottow_btnAction.place(x=20, y=150)
        self.bottow_btnFeedBack=Button(self.bottow,text="FeedBackCustomer",font="arial 12 underline bold italic", fg="#004d99",bg="white", bd=4,command=self.FeedBack).place(x=20,y=200)
        self.bottow_status=Label(self.bottow,text="Current information of the hotel",font="arial 20 underline bold italic",bg="#99ccff",fg="#004d99")
        self.bottow_status.place(x=280,y=10)
        g = open("dataroom.txt", "r", encoding="utf-8")
        a = g.readlines()
        self.scroll = Scrollbar(self.bottow, width=20)
        self.scroll.place(x=615, y=230)
        self.text = Listbox(self.bottow, yscrollcommand=self.scroll.set, width=65, font="arial 13 bold", bd=5)
        self.scroll.config(command=self.text.yview)
        for i in range(len(a)):
            self.text.insert(END, str(i) + " " + a[i])
        self.text.place(x=230, y=80)
        # design vien
        self.bottow_frame_lbvien=Label(self.bottow,height=50).place(x=200,y=1)
    def setup(self,event=None):
        g = open("dataroom.txt", "r", encoding="utf-8")
        a = g.readlines()
        self.scroll = Scrollbar(self.bottow, width=20)
        self.scroll.place(x=615, y=230)
        self.text = Listbox(self.bottow, yscrollcommand=self.scroll.set, width=65, font="arial 13 bold", bd=5)
        self.scroll.config(command=self.text.yview)
        for i in range(len(a)):
            self.text.insert(END, str(i) + " " + a[i])
        self.text.place(x=230, y=80)
    def datacus(self):
        cus=main()
    def dataroom(self):
        room=main1()
    def Baction(self):
        act=main3()
    def FeedBack(self):
        feed=main4()
def onclick(event=None):
    name = entry_User.get()
    passw = entry_Pass.get()
    a = "Bạn Nhập sai thông tin tài khoản"
    b = "Bạn chưa nhập đầy đủ thông tin"
    if (name == "AndTee" and passw == "123456"):
        return show2()
    elif (name == "" or passw == ""):
        return mb.showerror("Error", b)
    else:
        return mb.showerror("Error", a)
    pass
windown=tk.ThemedTk()
windown.get_themes()
windown.set_theme("keramik")
windown.iconbitmap("icon.ico")
windown.title("Đăng Nhập Account")
windown.geometry("450x150+150+150")
windown.resizable(False,False)
windown.bind('<Return>',onclick)
frame=Frame(windown,height=150,bg="#99ccff")
frame.pack(fill=X)
        #--Design SignIn---
label_user=Label(frame,text="UserName: ",font="arial 12 underline bold italic",bg="#99ccff",fg="#004d99")
label_user.place(x=20,y=20)
label_Pass=Label(frame,text="PassWork: ",font="arial 12 underline bold italic",bg="#99ccff",fg="#004d99")
label_Pass.place(x=20,y=50)
entry_User=Entry(frame,bg="white",bd=5,width=30)
entry_User.place(x=110,y=20)
entry_Pass = Entry(frame, bg="white", bd=5, width=30,show="*")
entry_Pass.place(x=110, y=50)


def gameon():
    name = entry_User.get()
    passw = entry_Pass.get()
    a = "Bạn Nhập sai thông tin tài khoản"
    b = "Bạn chưa nhập đầy đủ thông tin"
    if (name == "AndTee" and passw == "123456"):
        return show2()
    elif (name == "" or passw == ""):
        return mb.showerror("Error", b)
    else:
        return mb.showerror("Error", a)
def show2():
    main_frame2()

btn_sign=Button(frame,text="Sign In",font="arial 10 underline bold ",fg="Green",width=12,command=onclick)
btn_sign.place(x=60,y=100)
btn_Cancel = Button(frame, text="Cancel", font="arial 10 underline bold ", fg="Red", width=12,command=windown.destroy)
btn_Cancel.place(x=260, y=100)
def main_frame2():
    windown=tk.ThemedTk()

    app=App(windown)
    windown.get_themes()
    windown.iconbitmap("icon.ico")
    windown.set_theme("keramik")
    windown.title("Trang Chủ")
    windown.bind('<Return>',app.setup)
    windown.geometry("850x550+350+200")
    windown.resizable(False,False)
    windown.mainloop()
windown.mainloop()
