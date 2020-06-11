from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter.ttk import Combobox, Separator
from PIL import ImageTk,Image
from View.Customer import Customer
from tkinter import messagebox as mb
time=datetime.datetime.now().ctime()
time=str(time)
class Data_Customer(object):
    def __init__(self,master):
            self.master = master
            # --Frame
            self.top = Frame(master, height=50 ,bg='white')
            self.top.pack(fill=X)
            self.bottow = Frame(master, height=500, bg="#99ccff")
            self.bottow.pack(fill=X)
            # top Frame design
            self.top_frame_titel=Label(self.top,text="Data Customer",font="arial 25 underline bold italic",fg="#004d99",bg="white")
            self.top_frame_titel.place(x=200,y=1)
            self.top_frame_time=Label(self.top,text="Day&Time: "+time)
            self.top_frame_time.place(x=450,y=20)
            # bottow Frame design

            self.bottow_frame_lbUserCustomer=Label(self.bottow,text="NameCustomer: ",font="arial 12 underline bold",fg="#004d99",bg="#99ccff")
            self.bottow_frame_lbUserCustomer.place(x=25,y=20)
            self.bottow_frame_enUserCustomer=Entry(self.bottow,bg="white",bd=4,width=25)
            self.bottow_frame_enUserCustomer.place(x=155,y=20)
            self.bottow_frame_lbCMNDCustomer = Label(self.bottow, text="IDCardCustomer: ", font="arial 12 underline bold",
                                                     fg="#004d99", bg="#99ccff")
            self.bottow_frame_lbCMNDCustomer.place(x=16, y=50)
            self.bottow_frame_enCMNDCustomer = Entry(self.bottow, bg="white", bd=4, width=25)
            self.bottow_frame_enCMNDCustomer.place(x=155, y=50)
            self.bottow_frame_lbPhoneCustomer = Label(self.bottow, text="PhoneCustomer: ", font="arial 12 underline bold",
                                                     fg="#004d99", bg="#99ccff")
            self.bottow_frame_lbPhoneCustomer.place(x=20, y=80)
            self.bottow_frame_enPhoneCustomer = Entry(self.bottow, bg="white", bd=4, width=25)
            self.bottow_frame_enPhoneCustomer.place(x=155, y=80)
            v=["Day","Night"]
            self.bottow_frame_lbTimeSpend=Label(self.bottow,text="UsedTime: ",font="arial 12 underline bold",bg="#99ccff",fg="#004d99")
            self.bottow_frame_lbTimeSpend.place(x=68, y=110)
            self.bottow_frame_CbTimeSpend=Combobox(self.bottow,values=v,width=23)
            self.bottow_frame_CbTimeSpend.place(x=155,y=110)
            # button--controller
            self.bottow_frame_btnAdd=Button(self.bottow,text="Add Customer",font="arial 10 underline bold",bg="white",fg="#004d99",width=15,command=self.add)
            self.bottow_frame_btnAdd.place(x=420,y=40)

            self.bottow_frame_btnSearch = Button(self.bottow, text="Search Customer", font="arial 10 underline bold", bg="white", fg="#004d99",width=15,command=self.search)
            self.bottow_frame_btnSearch.place(x=420, y=80)
            # Design vien
            self.bottow_frame_lbVien=Label(self.bottow,height=9)
            self.bottow_frame_lbVien.place(x=380,y=1)
    def GetModel(self):
        check=False
        if(self.bottow_frame_enPhoneCustomer.get().isdigit() and self.bottow_frame_enCMNDCustomer.get().isdigit()):
              check=True
        if(check==True):
            self.customer=Customer(self.bottow_frame_enUserCustomer.get(),self.bottow_frame_enPhoneCustomer.get(),self.bottow_frame_enCMNDCustomer.get(),self.bottow_frame_CbTimeSpend.get())
            if(self.customer.getName()=="" or self.customer.getCMND()=="" or self.customer.getPhone()=="" or self.customer.getTime()==""):
                return mb.showerror("False","Bạn cần nhập đầy đủ thông tin khách hàng")
            else:
                c=["Name: "+self.customer.getName()," Phone: "+self.customer.getPhone()," CMND: "+self.customer.getCMND()," UsedTime: "+self.customer.getTime()+"\n"]

            return c
        else:
            return mb.showerror("Error","Phone and IDCard are Number")
    def add(self):
        gre=self.GetModel()
        f = open("datacus.txt", "a", encoding="utf-8")
        for i in gre:
            f.write(i)
        f.close()
        g=open("datacus.txt","r",encoding="utf-8")
        a=g.readlines()
        self.scroll=Scrollbar(self.bottow,width=20)
        self.scroll.place(x=615,y=230)
        self.text=Listbox(self.bottow,yscrollcommand=self.scroll.set,width=65,font="arial 12 bold",bd=5)
        self.scroll.config(command=self.text.yview)
        for i in range(len(a)):
            self.text.insert(END,str(i)+" "+a[i])
        self.text.place(x=20,y=230)
    def search(self):
        f=open("datacus.txt",'r',encoding="utf-8")
        a=f.readlines()
        b=list()

        if (self.bottow_frame_enPhoneCustomer == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for line in range(len(a)):
                if(self.bottow_frame_enPhoneCustomer.get() not in a[line]):
                    mb.showerror("Error","Khách hàng không tồn tại")
                    break
                elif(self.bottow_frame_enPhoneCustomer.get() in a[line]):
                    b.append(a[line])
        self.bottow_frame_search=Entry(self.bottow,width=55,font="arial 12 bold",bd=5)
        self.bottow_frame_search.insert(END,b)
        self.bottow_frame_search.place(x=20,y=160)


def main():
    windown = tk.ThemedTk()
    windown.get_themes()
    windown.set_theme("keramik")
    windown.iconbitmap("icon.ico")
    app = Data_Customer(windown)
    windown.title("DataCustomer")
    windown.geometry("650x550+350+200")
    windown.resizable(False, False)
    windown.mainloop()
if __name__=="__main__":
      main()