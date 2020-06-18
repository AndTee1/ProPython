from tkinter import *
import datetime
from tkinter.ttk import Combobox
from ttkthemes import themed_tk as tk
from MVC.Model.Room import Room
from MVC.Controller.OpenAndCloseFile import ReadAndOpenFile,RoomController
from tkinter import messagebox as mb
time=datetime.datetime.now().ctime()
time=str(time)
class BAction(object):
    def __init__(self, Master):
            self.Master = Master
            '''
            Design Frame
            '''
            self.Top = Frame(Master, height=50, bg='white')
            self.Top.pack(fill=X)
            self.Bottow = Frame(Master, height=600, bg="#99ccff")
            self.Bottow.pack(fill=X)
            '''
            Design Top Frame
            '''
            self.Top_Frame_Titel = Label(self.Top, text="Action Hotel", font="arial 28 underline bold italic", fg="#004d99", bg="white")
            self.Top_Frame_Titel.place(x=250, y=1)
            self.Top_Frame_Time = Label(self.Top, text="Day&Time: " + time)
            self.Top_Frame_Time.place(x=650, y=20)
            '''
            Design Bottow Frame
            '''
            self.Bottow_Frame_LbIDRoom = Label(self.Bottow, text="IDRoom: ", font="arial 12 underline bold", fg="#004d99",
                                               bg="#99ccff")
            self.Bottow_Frame_LbIDRoom.place(x=82, y=20)
            self.Bottow_Frame_EnIDRoom = Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnIDRoom.place(x=155, y=20)
            self.Bottow_Frame_LbPrice = Label(self.Bottow, text="PriceRoom: ", font="arial 12 underline bold",
                                              fg="#004d99", bg="#99ccff")
            self.Bottow_Frame_LbPrice.place(x=60, y=50)
            self.Bottow_Frame_EnPrice = Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnPrice.place(x=155, y=50)
            self.Bottow_Frame_LbStatus = Label(self.Bottow, text="StatusRoom: ", font="arial 12 underline bold",
                                               fg="#004d99", bg="#99ccff")
            self.Bottow_Frame_LbStatus.place(x=50, y=80)
            self.Bottow_Frame_EnStatus = Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnStatus.place(x=155, y=80)
            Option_CBKind = ["Day", "Night"]
            Option_CBTimeSpend = ["VIP", "Nomarl"]
            self.Bottow_Frame_LbTimeSpend = Label(self.Bottow, text="UsedTime: ", font="arial 12 underline bold", bg="#99ccff",
                                                  fg="#004d99")
            self.Bottow_Frame_LbTimeSpend.place(x=68, y=110)
            self.Bottow_Frame_CbTimeSpend = Combobox(self.Bottow, values=Option_CBKind, width=23)
            self.Bottow_Frame_CbTimeSpend.place(x=155, y=110)
            self.Bottow_Frame_LbKind = Label(self.Bottow, text="KindRoom: ", font="arial 12 underline bold", bg="#99ccff",
                                             fg="#004d99")
            self.Bottow_Frame_LbKind.place(x=64, y=140)
            self.Bottow_Frame_CbKind = Combobox(self.Bottow, values=Option_CBTimeSpend, width=23)
            self.Bottow_Frame_CbKind.place(x=155, y=140)
            self.Bottow_Frame_BtnAdd = Button(self.Bottow, text="Bill", font="arial 10 underline bold", bg="white",
                                              fg="#004d99", width=15, command=self.BillForCustomer)
            self.Bottow_Frame_BtnAdd.place(x=20, y=180)

            self.Bottow_Frame_BtnCheckOut = Button(self.Bottow, text="CheckOut", font="arial 10 underline bold", bg="white",
                                                   fg="#004d99", width=15, command=self.CheckOutForCustomer)
            self.Bottow_Frame_BtnCheckOut.place(x=20, y=220)
            self.Bottow_Frame_BtnClear = Button(self.Bottow, text="ClearRoom", font="arial 10 underline bold", bg="white",
                                                fg="#004d99", width=15, command=self.ReturnRoom)
            self.Bottow_Frame_BtnClear.place(x=20, y=260)

            Open_File =ReadAndOpenFile.Read_File_BAction(self)
            List_Show = Open_File.readlines()
            self.Scroll = Scrollbar(self.Bottow, width=20)
            self.List_Box = Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65, font="arial 10 underline bold italic", bd=5)
            self.Scroll.config(command=self.List_Box.yview)
            for i in range(len(List_Show)):
                self.List_Box.insert(END, str(i) + " " + List_Show[i])
            self.List_Box.place(x=20, y=300)
            self.Bar = IntVar()
            self.Bottow_Frame_DVbar=Checkbutton(self.Bottow, text="Bar_mini:50000", bg="#99ccff", variable=self.Bar, font="arial 10 underline bold", fg="#004d99")
            self.Bottow_Frame_DVbar.place(x=380, y=20)
            self.Food=IntVar()

            self.Gif=IntVar()
            self.Bottow_Frame_DVFood=Checkbutton(self.Bottow, text="Food_Room:40000", bg="#99ccff", variable=self.Food, font="arial 10 underline bold", fg="#004d99")
            self.Bottow_Frame_DVFood.place(x=380, y=50)
            self.Bottow_Frame_DVGif=Checkbutton(self.Bottow, text="GIF_customer:30000", bg="#99ccff", variable=self.Gif, font="arial 10 underline bold", fg="#004d99")
            self.Bottow_Frame_DVGif.place(x=380, y=80)

            self.Bottow_Frame_Lbbill = Label(self.Bottow, text="Payment of service invoices ", font="arial 15 underline bold italic", bg="#99ccff",
                                             fg="#004d99")
            self.Bottow_Frame_Lbbill.place(x=600, y=20)
            '''
            Design Bo viền
            '''
            self.Bottow_Frame_LbVien=Label(self.Bottow, height=50)
            self.Bottow_Frame_LbVien.place(x=540, y=0)

    '''
    Hãm xử lý ngoại lệ nhập và ghi dữ liệu từ MVC Về Object
    '''
    def GetModel(self):
        check=False
        if(self.Bottow_Frame_EnPrice.get().isdigit() and self.Bottow_Frame_EnIDRoom.get().isdigit()):
              check=True
        if(check==True):
            self.room=RoomController(self.Bottow_Frame_EnIDRoom.get(), self.Bottow_Frame_EnPrice.get(), self.Bottow_Frame_CbKind.get(), self.Bottow_Frame_CbTimeSpend.get(), self.Bottow_Frame_EnStatus.get())
            if(self.room.getID()=="" or self.room.getUsedTime()=="" or self.room.getKind()=="" or self.room.getPrice()==""or self.room.getStatus()==""):
                return mb.showerror("False","Bạn cần nhập đầy đủ thông tin")
            else:
                Data_Room=["ID: "+self.room.getID()," Price: "+self.room.getPrice()," Kind: "+self.room.getKind()," UsedTime: "+self.room.getUsedTime()," Status: "+self.room.getStatus()+"\n"]

            return Data_Room
        else:
            return mb.showerror("Error","Price and ID are Number")
    '''
    Hàm set lại dữ liệu từ MVC Để sử dụng cho Fun BillForCustomer
    '''
    def Model(self):
        self.room = Room(self.Bottow_Frame_EnIDRoom.get(), self.Bottow_Frame_EnPrice.get(), self.Bottow_Frame_CbKind.get(), self.Bottow_Frame_CbTimeSpend.get(), self.Bottow_Frame_EnStatus.get())
        Data_Room=[self.Bottow_Frame_EnIDRoom.get(), int(self.Bottow_Frame_EnPrice.get()), self.Bottow_Frame_CbKind.get(), self.Bottow_Frame_CbTimeSpend.get(), self.Bottow_Frame_EnStatus.get()]
        return Data_Room
    def CheckOutForCustomer(self):
        Open_File=ReadAndOpenFile.Read_File_BAction(self)
        List_Show=Open_File.readlines()
        Open_File.close()

        if (self.Bottow_Frame_EnIDRoom == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for i in range(len(List_Show)):
                if(self.Bottow_Frame_EnIDRoom.get() in List_Show[i]):
                     Data_Show=List_Show[i]
        Write_File=ReadAndOpenFile.Write_File_BAction(self)
        for i in List_Show:
            if (i!=Data_Show):
                Write_File.write(i)
        Write_File.close()

    def ReturnRoom(self):
        Gre = self.GetModel()
        Open_File = ReadAndOpenFile.AWrite_File_Room(self)
        for i in Gre:
            Open_File.write(i)
        Open_File.close()
    def BillForCustomer(self):
        Gre=self.Model()
        if (self.Food.get() == 1 and self.Bar.get() == 1 and self.Gif.get() == 1):
            Gre[1] += 100000
        elif(self.Food.get() == 0 and self.Bar.get() == 0 and self.Gif.get() == 0):
            Gre[1] = self.Bottow_Frame_EnPrice.get()
        elif(self.Food.get() == 1):
           Gre[1]+=40000

        elif(self.Bar.get() == 1):
            Gre[1] += 50000

        elif(self.Gif.get() == 1):
            Gre[1]+=30000
        self.Data_Show = ("IDRoom: " + Gre[0] + "\n", "KindRoom: " + Gre[2] + "\n", "NameCustomer: " + Gre[4] + "\n",
             "TimeSpend: " + Gre[3] + "\n", "PriceEnd: " + str(Gre[1]))

        self.Bottow_Frame_Bill = Text(self.Bottow, font="arial 12 bold italic", width=30, height=15, bd=4)
        self.Bottow_Frame_Bill.insert(END, self.Data_Show)
        self.Bottow_Frame_Bill.place(x=600, y=80)
    '''
    Sử lý Nút Enter để Upload lại dữ liệu cho ListBox
    '''
    def Upload(self,event=None):
        Open_File = ReadAndOpenFile.Read_File_BAction(self)
        List_Show = Open_File.readlines()
        self.Scroll = Scrollbar(self.Bottow, width=20)
        self.List_Box = Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65,
                                font="arial 10 underline bold italic", bd=5)
        self.Scroll.config(command=self.List_Box.yview)
        for i in range(len(List_Show)):
            self.List_Box.insert(END, str(i) + " " + List_Show[i])
        self.List_Box.place(x=20, y=300)

def main3():
    Root_BAction = tk.ThemedTk()
    app = BAction(Root_BAction)
    Root_BAction.get_themes()
    Root_BAction.iconbitmap("icon.ico")
    Root_BAction.set_theme("keramik")
    Root_BAction.bind('<Return>',app.Upload)
    Root_BAction.title("Business activities")
    Root_BAction.geometry("950x550+350+200")
    Root_BAction.resizable(False, False)
    Root_BAction.mainloop()
if __name__=="__main__":
    main3()
