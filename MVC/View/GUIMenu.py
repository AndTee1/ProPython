from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from MVC.View.GUiCustomer import main
from MVC.View.GUIRoom import  main1
from MVC.View.GUIBAction import main3
from tkinter import messagebox as mb
from MVC.Controller.OpenAndCloseFile import ReadAndOpenFile
from MVC.View.feedBackCustomer import main4
date=datetime.datetime.now().date()
date=str(date)
time=datetime.datetime.now().time()
time=str(time)
class App(object):
    def __init__(self, Master):
        self.Master=Master
        '''
        Design Frame
        '''
        self.Top=Frame(Master, height=150, bg='white')
        self.Top.pack(fill=X)
        self.Bottow=Frame(Master, height=500, bg="#99ccff")
        self.Bottow.pack(fill=X)
        '''
        Top frame design
        '''
        self.Top_icon_label1=Label(self.Top, text="AndTee's Hotel", font="arial 25 underline bold italic", bg='white', fg='#004d99')
        self.Top_icon_label1.place(x=230,y=50)
        self.Date=Label(self.Top, text="Today is:" + date + "Time:" + time, font="arial 12 italic", fg="black", bg="#eff5f5")
        self.Date.place(x=605, y=120)
        '''
        Bottow frame design
        '''
        self.Bottow_BtnCustomer=Button(self.Bottow, text="Data Customer", width=15, font="arial 12 underline bold italic", fg="#004d99", bg="white", bd=4, command=self.Open_FrameCustomer)
        self.Bottow_BtnCustomer.place(x=20, y=50)
        self.Bottow_BtnRoom = Button(self.Bottow, text="Data Room", width=15, font="arial 12 underline bold italic", fg="#004d99",
                                     bg="white", bd=4, command=self.Open_FrameRoom)
        self.Bottow_BtnRoom.place(x=20, y=100)
        self.Bottow_BtnAction = Button(self.Bottow, text="Business activities", width=15, font="arial 12 underline bold italic", fg="#004d99",
                                       bg="white", bd=4, command=self.Open_FrameBAction)
        self.Bottow_BtnAction.place(x=20, y=150)
        self.Bottow_BtnFeedBack=Button(self.Bottow, text="FeedBackCustomer", font="arial 12 underline bold italic", fg="#004d99", bg="white", bd=4, command=self.Open_FrameFeedBack).place(x=20, y=200)
        self.Bottow_Status=Label(self.Bottow, text="Current information of the hotel", font="arial 20 underline bold italic", bg="#99ccff", fg="#004d99")
        self.Bottow_Status.place(x=280, y=10)
        Open_File = open("../../Data/dataroom.txt", "r", encoding="utf-8")
        List_Show = Open_File.readlines()
        self.Scroll = Scrollbar(self.Bottow, width=20)
        self.Scroll.place(x=615, y=230)
        self.List_Box = Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65, font="arial 13 bold", bd=5)
        self.Scroll.config(command=self.List_Box.yview)
        for i in range(len(List_Show)):
            self.List_Box.insert(END, str(i) + " " + List_Show[i])
        self.List_Box.place(x=230, y=80)
        '''
        Design Bo Viền
        '''
        self.Bottow_Frame_Lbvien=Label(self.Bottow, height=50).place(x=200, y=1)
    '''
    Hàm xử lý Upload lại dữ liệu cho LixtBox
    '''
    def Upload(self,event=None):
        Open_File = ReadAndOpenFile.Read_File_Room(self)
        List_Show = Open_File.readlines()
        self.Scroll = Scrollbar(self.Bottow, width=20)
        self.Scroll.place(x=615, y=230)
        self.List_Box = Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65, font="arial 13 bold", bd=5)
        self.Scroll.config(command=self.List_Box.yview)
        for i in range(len(List_Show)):
            self.List_Box.insert(END, str(i) + " " + List_Show[i])
        self.List_Box.place(x=230, y=80)
    def Open_FrameCustomer(self):
        main()
    def Open_FrameRoom(self):
        main1()
    def Open_FrameBAction(self):
        main3()
    def Open_FrameFeedBack(self):
        main4()
'''
Hàm xử lý Nút Enter cho SignIN
'''
def Onclick(event=None):
    UserName = Entry_User.get()
    Pass = Entry_Pass.get()
    if (UserName == "AndTee" and Pass == "123456"):
        return Open_FrameMenu()
    elif (UserName == "" or Pass == ""):
        return mb.showerror("Error", "Bạn chưa nhập đầy đủ thông tin")
    else:
        return mb.showerror("Error", "Bạn Nhập sai thông tin tài khoản")
Root_SignIn=tk.ThemedTk()
Root_SignIn.get_themes()
Root_SignIn.set_theme("keramik")
Root_SignIn.iconbitmap("icon.ico")
Root_SignIn.title("Đăng Nhập Account")
Root_SignIn.geometry("450x150+150+150")
Root_SignIn.resizable(False, False)
Root_SignIn.bind('<Return>', Onclick)

'''
        --Design SignIn---
'''
Frame_SignIn=Frame(Root_SignIn, height=150, bg="#99ccff")
Frame_SignIn.pack(fill=X)
Label_User=Label(Frame_SignIn, text="UserName: ", font="arial 12 underline bold italic", bg="#99ccff", fg="#004d99")
Label_User.place(x=20, y=20)
Label_Pass=Label(Frame_SignIn, text="PassWork: ", font="arial 12 underline bold italic", bg="#99ccff", fg="#004d99")
Label_Pass.place(x=20, y=50)
Entry_User=Entry(Frame_SignIn, bg="white", bd=5, width=30)
Entry_User.place(x=110,y=20)
Entry_Pass = Entry(Frame_SignIn, bg="white", bd=5, width=30, show="*")
Entry_Pass.place(x=110, y=50)
def Open_FrameMenu():
    Frame_Menu() and Root_SignIn.destroy()

Btn_SignIn=Button(Frame_SignIn, text="Sign In", font="arial 10 underline bold ", fg="Green", width=12, command=Onclick)
Btn_SignIn.place(x=60, y=100)
Btn_Cancel = Button(Frame_SignIn, text="Cancel", font="arial 10 underline bold ", fg="Red", width=12, command=Root_SignIn.destroy)
Btn_Cancel.place(x=260, y=100)
def Frame_Menu():
    Frame_Menu=tk.ThemedTk()

    app=App(Frame_Menu)
    Frame_Menu.get_themes()
    Frame_Menu.iconbitmap("icon.ico")
    Frame_Menu.set_theme("keramik")
    Frame_Menu.title("Trang Chủ")
    Frame_Menu.bind('<Return>', app.Upload)
    Frame_Menu.geometry("850x550+350+200")
    Frame_Menu.resizable(False, False)
    Frame_Menu.mainloop()
Root_SignIn.mainloop()
