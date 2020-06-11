from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from View.Room import Room
from tkinter import messagebox as mb
time=datetime.datetime.now().ctime()
time=str(time)
class DataRoom(object):
    def __init__(self,master):
        self.master=master
        #--Frame
        self.top=Frame(master,height=50,bg="white")
        self.top.pack(fill=X)
        self.bottow = Frame(master, height=600, bg="#99ccff")
        self.bottow.pack(fill=X)
        # top Frame design
        self.top_frame_titel = Label(self.top, text="Data Room", font="arial 25 underline bold italic", fg="#004d99", bg="white")
        self.top_frame_titel.place(x=200, y=1)
        self.top_frame_time = Label(self.top, text="Day&Time: " + time)
        self.top_frame_time.place(x=430, y=20)
        # bottow Frame design

        self.bottow_frame_lbIDRoom = Label(self.bottow, text="IDRoom: ", font="arial 12 underline bold", fg="#004d99",
                                                 bg="#99ccff")
        self.bottow_frame_lbIDRoom.place(x=80, y=20)
        self.bottow_frame_enIDRoom = Entry(self.bottow, bg="white", bd=4, width=25)
        self.bottow_frame_enIDRoom.place(x=155, y=20)
        self.bottow_frame_lbPrice = Label(self.bottow, text="PriceRoom: ", font="arial 12 underline bold",
                                                 fg="#004d99", bg="#99ccff")
        self.bottow_frame_lbPrice.place(x=58, y=50)
        self.bottow_frame_enPrice = Entry(self.bottow, bg="white", bd=4, width=25)
        self.bottow_frame_enPrice.place(x=155, y=50)
        self.bottow_frame_lbstatus = Label(self.bottow, text="StatusRoom: ", font="arial 12 underline bold",
                                                  fg="#004d99", bg="#99ccff")
        self.bottow_frame_lbstatus.place(x=49, y=80)
        self.bottow_frame_enstatus = Entry(self.bottow, bg="white", bd=4, width=25)
        self.bottow_frame_enstatus.place(x=155, y=80)
        v = ["Day", "Night"]
        k = ["VIP","Nomarl"]
        self.bottow_frame_lbTimeSpend = Label(self.bottow, text="UsedTime: ", font="arial 12 underline bold", bg="#99ccff",
                                              fg="#004d99")
        self.bottow_frame_lbTimeSpend.place(x=68, y=110)
        self.bottow_frame_CbTimeSpend = Combobox(self.bottow, values=v, width=23)
        self.bottow_frame_CbTimeSpend.place(x=155, y=110)
        self.bottow_frame_lbKind = Label(self.bottow, text="KindRoom: ", font="arial 12 underline bold", bg="#99ccff",
                                              fg="#004d99")
        self.bottow_frame_lbKind.place(x=64, y=140)
        self.bottow_frame_CbKind = Combobox(self.bottow, values=k, width=23)
        self.bottow_frame_CbKind.place(x=155, y=140)
        self.bottow_frame_btnAdd = Button(self.bottow, text="Add New Room", font="arial 10 underline bold", bg="white",
                                          fg="#004d99", width=15,command=self.add)
        self.bottow_frame_btnAdd.place(x=420, y=40)

        self.bottow_frame_btnCheckIn = Button(self.bottow, text="CheckIn", font="arial 10 underline bold", bg="white",
                                             fg="#004d99", width=15,command=self.checkin)
        self.bottow_frame_btnCheckIn.place(x=420, y=80)
        self.bottow_frame_btnClear = Button(self.bottow, text="Clear", font="arial 10 underline bold", bg="white",
                                              fg="#004d99", width=15, command=self.clear)
        self.bottow_frame_btnClear.place(x=420, y=120)

    def GetModel(self):
        check=False
        if(self.bottow_frame_enPrice.get().isdigit() and self.bottow_frame_enIDRoom.get().isdigit()):
              check=True
        if(check==True):
            self.room=Room(self.bottow_frame_enIDRoom.get(),self.bottow_frame_enPrice.get(),self.bottow_frame_CbKind.get(),self.bottow_frame_CbTimeSpend.get(),self.bottow_frame_enstatus.get())
            if(self.room.getID()=="" or self.room.getTime()=="" or self.room.getKind()=="" or self.room.getPrice()==""or self.room.getStatus()==""):
                return mb.showerror("False","Bạn cần nhập đầy đủ thông tin")
            else:
                c=["ID: "+self.room.getID()," Price: "+self.room.getPrice()," Kind: "+self.room.getKind()," UsedTime: "+self.room.getTime()," Status: "+self.room.getStatus()+"\n"]

            return c
        else:
            return mb.showerror("Error","Price and ID are Number")

    def add(self):
        gre=self.GetModel()
        f = open("dataroom.txt", "a", encoding="utf-8")
        for i in gre:
            f.write(i)
        f.close()
        g=open("dataroom.txt","r",encoding="utf-8")
        a=g.readlines()
        self.scroll=Scrollbar(self.bottow,width=20)
        self.scroll.place(x=615,y=230)
        self.text=Listbox(self.bottow,yscrollcommand=self.scroll.set,width=65,font="arial 12 bold",bd=5)
        self.scroll.config(command=self.text.yview)
        for i in range(len(a)):
            self.text.insert(END,str(i)+" "+a[i])
        self.text.place(x=20,y=230)
    def checkin(self):
        gre=self.GetModel()
        f=open("actionhotel.txt","a",encoding="utf-8")
        for i in gre:
            f.write(i)
        f.close()

    def clear(self):
        f=open("dataroom.txt",'r',encoding="utf-8")
        a=f.readlines()
        f.close()

        if (self.bottow_frame_enIDRoom == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for i in range(len(a)):
                if(self.bottow_frame_enIDRoom.get() in a[i]):
                     b=a[i]
        g=open("dataroom.txt","w",encoding="utf-8")
        for i in a:
            if (i!=b):
                g.write(i)
        g.close()



def main1():
    windown=tk.ThemedTk()
    windown.get_themes()
    windown.iconbitmap("icon.ico")
    windown.set_theme("keramik")
    dataroom=DataRoom(windown)
    windown.title("DataRoom")
    windown.geometry("650x550+350+200")
    windown.resizable(False,False)
    windown.mainloop()
if __name__=="__main__":
    main1()
