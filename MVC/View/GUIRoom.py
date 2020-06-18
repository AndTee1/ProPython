from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from tkinter.ttk import Combobox
from MVC.Model.Room import Room
from tkinter import messagebox as mb
from MVC.Controller.OpenAndCloseFile import ReadAndOpenFile,RoomController
time=datetime.datetime.now().ctime()
time=str(time)
class DataRoom(object):
    def __init__(self, Master):
        self.Master=Master
        '''
        Design Frame
        '''
        self.Top=Frame(Master, height=50, bg="white")
        self.Top.pack(fill=X)
        self.Bottow = Frame(Master, height=600, bg="#99ccff")
        self.Bottow.pack(fill=X)
        '''
        Design Top Frame
        '''
        self.Top_Frame_Titel = Label(self.Top, text="Data Room", font="arial 25 underline bold italic", fg="#004d99", bg="white")
        self.Top_Frame_Titel.place(x=200, y=1)
        self.Top_Frame_Time = Label(self.Top, text="Day&Time: " + time)
        self.Top_Frame_Time.place(x=430, y=20)
        '''
        Design Bottow Frame
        '''
        self.Bottow_Frame_LbIDRoom = Label(self.Bottow, text="IDRoom: ", font="arial 12 underline bold", fg="#004d99",
                                           bg="#99ccff")
        self.Bottow_Frame_LbIDRoom.place(x=80, y=20)
        self.Bottow_Frame_EnIDRoom = Entry(self.Bottow, bg="white", bd=4, width=25)
        self.Bottow_Frame_EnIDRoom.place(x=155, y=20)
        self.Bottow_Frame_LbPrice = Label(self.Bottow, text="PriceRoom: ", font="arial 12 underline bold",
                                          fg="#004d99", bg="#99ccff")
        self.Bottow_Frame_LbPrice.place(x=58, y=50)
        self.Bottow_Frame_EnPrice = Entry(self.Bottow, bg="white", bd=4, width=25)
        self.Bottow_Frame_EnPrice.place(x=155, y=50)
        self.Bottow_Frame_LbStatus = Label(self.Bottow, text="StatusRoom: ", font="arial 12 underline bold",
                                           fg="#004d99", bg="#99ccff")
        self.Bottow_Frame_LbStatus.place(x=49, y=80)
        self.Bottow_Frame_EnStatus = Entry(self.Bottow, bg="white", bd=4, width=25)
        self.Bottow_Frame_EnStatus.place(x=155, y=80)
        Option_CbTime = ["Day", "Night"]
        Option_CbKind = ["VIP","Nomarl"]
        self.Bottow_Frame_LbTimeSpend = Label(self.Bottow, text="UsedTime: ", font="arial 12 underline bold", bg="#99ccff",
                                              fg="#004d99")
        self.Bottow_Frame_LbTimeSpend.place(x=68, y=110)
        self.Bottow_Frame_CbTimeSpend = Combobox(self.Bottow, values=Option_CbTime, width=23)
        self.Bottow_Frame_CbTimeSpend.place(x=155, y=110)
        self.Bottow_Frame_LbKind = Label(self.Bottow, text="KindRoom: ", font="arial 12 underline bold", bg="#99ccff",
                                         fg="#004d99")
        self.Bottow_Frame_LbKind.place(x=64, y=140)
        self.Bottow_Frame_CbKind = Combobox(self.Bottow, values=Option_CbKind, width=23)
        self.Bottow_Frame_CbKind.place(x=155, y=140)
        self.Bottow_Frame_BtnAdd = Button(self.Bottow, text="Add New Room", font="arial 10 underline bold", bg="white",
                                          fg="#004d99", width=15, command=self.AddNewRoom)
        self.Bottow_Frame_BtnAdd.place(x=420, y=40)

        self.Bottow_Frame_BtnCheckIn = Button(self.Bottow, text="CheckIn", font="arial 10 underline bold", bg="white",
                                              fg="#004d99", width=15, command=self.CheckInForCustomer)
        self.Bottow_Frame_BtnCheckIn.place(x=420, y=80)
        self.Bottow_Frame_BtnClear = Button(self.Bottow, text="ClearRoom", font="arial 10 underline bold", bg="white",
                                            fg="#004d99", width=15, command=self.ReturnRoom)
        self.Bottow_Frame_BtnClear.place(x=420, y=120)
    '''
    Fun xử lý ngoại lệ nhập và ghi dữ liệu từ MVC vào Object
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
                Data_Show=["ID: "+self.room.getID()," Price: "+self.room.getPrice()," Kind: "+self.room.getKind()," UsedTime: "+self.room.getUsedTime()," Status: "+self.room.getStatus()+"\n"]
            return Data_Show
        else:
            return mb.showerror("Error","Price and ID are Number")

    def AddNewRoom(self):
        Gre=self.GetModel()
        Write_File = ReadAndOpenFile.AWrite_File_Room(self)
        for i in Gre:
            Write_File.write(i)
        Write_File.close()
        Open_File=ReadAndOpenFile.Read_File_Room(self)
        List_Show=Open_File.readlines()
        self.Scroll=Scrollbar(self.Bottow, width=20)
        self.Scroll.place(x=615, y=230)
        self.List_Box=Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65, font="arial 12 bold", bd=5)
        self.Scroll.config(command=self.List_Box.yview)
        for i in range(len(List_Show)):
            self.List_Box.insert(END, str(i) + " " + List_Show[i])
        self.List_Box.place(x=20, y=230)
    def CheckInForCustomer(self):
        Gre=self.GetModel()
        Write_File=ReadAndOpenFile.Write_File_BAction(self)
        for i in Gre:
            Write_File.write(i)
        Write_File.close()
    '''
    Fun Return lại các phòng còn trống
    '''
    def ReturnRoom(self):
        Open_File=ReadAndOpenFile.Read_File_Room(self)
        List_Show=Open_File.readlines()
        Open_File.close()

        if (self.Bottow_Frame_EnIDRoom == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for i in range(len(List_Show)):
                if(self.Bottow_Frame_EnIDRoom.get() in List_Show[i]):
                     Data_Show=List_Show[i]
        Write_File=ReadAndOpenFile.WWrite_File_Room(self)
        for i in List_Show:
            if (i!=Data_Show):
                Write_File.write(i)
        Write_File.close()



def main1():
    Root_Room=tk.ThemedTk()
    Root_Room.get_themes()
    Root_Room.iconbitmap("icon.ico")
    Root_Room.set_theme("keramik")
    DataRoom(Root_Room)
    Root_Room.title("DataRoom")
    Root_Room.geometry("650x550+350+200")
    Root_Room.resizable(False,False)
    Root_Room.mainloop()
if __name__=="__main__":
    main1()
