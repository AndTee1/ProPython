from tkinter import *
import datetime
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from ttkthemes import themed_tk as tk
from tkinter import ttk
from View.Room import Room
from tkinter import messagebox as mb
time=datetime.datetime.now().ctime()
time=str(time)
class BAction(object):
    def __init__(self,master):
            self.master = master
            # --Frame
            self.top = Frame(master, height=50, bg='white')
            self.top.pack(fill=X)
            self.bottow = Frame(master, height=600, bg="#99ccff")
            self.bottow.pack(fill=X)
            # top Frame design
            self.top_frame_titel = Label(self.top, text="Action Hotel", font="arial 28 underline bold italic", fg="#004d99", bg="white")
            self.top_frame_titel.place(x=250, y=1)
            self.top_frame_time = Label(self.top, text="Day&Time: " + time)
            self.top_frame_time.place(x=650, y=20)
            # bottow Frame design

            self.bottow_frame_lbIDRoom = Label(self.bottow, text="IDRoom: ", font="arial 12 underline bold", fg="#004d99",
                                               bg="#99ccff")
            self.bottow_frame_lbIDRoom.place(x=82, y=20)
            self.bottow_frame_enIDRoom = Entry(self.bottow, bg="white", bd=4, width=25)
            self.bottow_frame_enIDRoom.place(x=155, y=20)
            self.bottow_frame_lbPrice = Label(self.bottow, text="PriceRoom: ", font="arial 12 underline bold",
                                              fg="#004d99", bg="#99ccff")
            self.bottow_frame_lbPrice.place(x=60, y=50)
            self.bottow_frame_enPrice = Entry(self.bottow, bg="white", bd=4, width=25)
            self.bottow_frame_enPrice.place(x=155, y=50)
            self.bottow_frame_lbstatus = Label(self.bottow, text="StatusRoom: ", font="arial 12 underline bold",
                                               fg="#004d99", bg="#99ccff")
            self.bottow_frame_lbstatus.place(x=50, y=80)
            self.bottow_frame_enstatus = Entry(self.bottow, bg="white", bd=4, width=25)
            self.bottow_frame_enstatus.place(x=155, y=80)
            v = ["Day", "Night"]
            k = ["VIP", "Nomarl"]
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
            self.bottow_frame_btnAdd = Button(self.bottow, text="Bill", font="arial 10 underline bold", bg="white",
                                              fg="#004d99", width=15,command=self.bill)
            self.bottow_frame_btnAdd.place(x=20, y=180)

            self.bottow_frame_btnCheckOut = Button(self.bottow, text="CheckOut", font="arial 10 underline bold", bg="white",
                                                  fg="#004d99", width=15,command=self.clear)
            self.bottow_frame_btnCheckOut.place(x=20, y=220)
            self.bottow_frame_btnClear = Button(self.bottow, text="Clear", font="arial 10 underline bold", bg="white",
                                                fg="#004d99", width=15,command=self.addin)
            self.bottow_frame_btnClear.place(x=20, y=260)

            g = open("actionhotel.txt", "r", encoding="utf-8")
            a = g.readlines()
            self.scroll = Scrollbar(self.bottow, width=20)
            self.text = Listbox(self.bottow, yscrollcommand=self.scroll.set, width=65, font="arial 10 underline bold italic", bd=5)
            self.scroll.config(command=self.text.yview)
            for i in range(len(a)):
                self.text.insert(END, str(i) + " " + a[i])
            self.text.place(x=20, y=300)
            self.j = IntVar()
            self.bottow_frame_DVbar=Checkbutton(self.bottow,text="Bar_mini:50000",bg="#99ccff",variable=self.j,font="arial 10 underline bold",fg="#004d99")
            self.bottow_frame_DVbar.place(x=380,y=20)
            self.i=IntVar()

            self.g=IntVar()
            self.bottow_frame_DVFood=Checkbutton(self.bottow,text="Food_Room:40000",bg="#99ccff",variable=self.i,font="arial 10 underline bold",fg="#004d99")
            self.bottow_frame_DVFood.place(x=380,y=50)
            self.bottow_frame_DVGif=Checkbutton(self.bottow,text="GIF_customer:30000",bg="#99ccff",variable=self.g,font="arial 10 underline bold",fg="#004d99")
            self.bottow_frame_DVGif.place(x=380,y=80)

            self.bottow_frame_lbbill = Label(self.bottow, text="Payment of service invoices ", font="arial 15 underline bold italic", bg="#99ccff",
                                     fg="#004d99")
            self.bottow_frame_lbbill.place(x=600, y=20)
        # design bo viền
            self.bottow_frame_lbVien=Label(self.bottow,height=50)
            self.bottow_frame_lbVien.place(x=540,y=0)


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
    def clear(self):
        f=open("actionhotel.txt",'r',encoding="utf-8")
        a=f.readlines()
        f.close()

        if (self.bottow_frame_enIDRoom == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for i in range(len(a)):
                if(self.bottow_frame_enIDRoom.get() in a[i]):
                     b=a[i]
        g=open("actionhotel.txt","w",encoding="utf-8")
        for i in a:
            if (i!=b):
                g.write(i)
        g.close()

    def addin(self):
        gre = self.GetModel()
        f = open("dataroom.txt", "a", encoding="utf-8")
        for i in gre:
            f.write(i)
        f.close()
    def bill(self):

        c=[self.bottow_frame_enIDRoom.get(),self.bottow_frame_CbKind.get(),self.bottow_frame_enstatus.get(),self.bottow_frame_CbTimeSpend.get(),int(self.bottow_frame_enPrice.get())]

        if (self.i.get() == 1 and self.j.get() == 1 and self.g.get() == 1):
            c[4] += 100000
        elif(self.i.get() == 0 and self.j.get() == 0 and self.g.get() == 0):
            c[4] = self.bottow_frame_enPrice.get()
        elif(self.i.get()==1):
           c[4]+=40000

        elif(self.j.get()==1):
            c[4] += 50000

        elif(self.g.get()==1):
            c[4]+=30000
        else:
            c[4]+=80000
        b = ("IDRoom: " + c[0] + "\n", "KindRoom: " + c[1] + "\n", "NameCustomer: " + c[2] + "\n",
             "TimeSpend: " + c[3] + "\n", "PriceEnd: " +str(c[4]))

        self.bottow_frame_bill = Text(self.bottow,font="arial 12 bold italic",width=30,height=15,bd=4)
        self.bottow_frame_bill.insert(END,b)
        self.bottow_frame_bill.place(x=600, y=80)
    def setup(self,event=None):
        g = open("actionhotel.txt", "r", encoding="utf-8")
        a = g.readlines()
        self.scroll = Scrollbar(self.bottow, width=20)
        self.text = Listbox(self.bottow, yscrollcommand=self.scroll.set, width=65,
                            font="arial 10 underline bold italic", bd=5)
        self.scroll.config(command=self.text.yview)
        for i in range(len(a)):
            self.text.insert(END, str(i) + " " + a[i])
        self.text.place(x=20, y=300)

def main3():
    windown = tk.ThemedTk()
    app = BAction(windown)
    windown.get_themes()
    windown.iconbitmap("icon.ico")
    windown.set_theme("keramik")
    windown.bind('<Return>',app.setup)
    windown.title("Business activities")
    windown.geometry("950x550+350+200")
    windown.resizable(False, False)
    windown.mainloop()
if __name__=="__main__":
    main3()
