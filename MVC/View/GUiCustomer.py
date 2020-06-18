from tkinter import *
import datetime
from ttkthemes import themed_tk as tk
from tkinter.ttk import Combobox
from MVC.Model.Customer import Customer
from tkinter import messagebox as mb
from MVC.Controller.OpenAndCloseFile import ReadAndOpenFile,CustomerController
time=datetime.datetime.now().ctime()
time=str(time)
class Data_Customer(object):
    def __init__(self, Master):
            self.Master = Master
            '''
            Design Frame
            '''
            self.Top = Frame(Master, height=50, bg='white')
            self.Top.pack(fill=X)
            self.Bottow = Frame(Master, height=500, bg="#99ccff")
            self.Bottow.pack(fill=X)
            '''
            Design Top Frame
            '''
            self.Top_Frame_Titel=Label(self.Top, text="Data Customer", font="arial 25 underline bold italic", fg="#004d99", bg="white")
            self.Top_Frame_Titel.place(x=200, y=1)
            self.Top_Frame_Time=Label(self.Top, text="Day&Time: " + time)
            self.Top_Frame_Time.place(x=450, y=20)
            '''
            Design Bottow Frame
            '''
            self.Bottow_Frame_LbUserCustomer=Label(self.Bottow, text="NameCustomer: ", font="arial 12 underline bold", fg="#004d99", bg="#99ccff")
            self.Bottow_Frame_LbUserCustomer.place(x=25, y=20)
            self.Bottow_Frame_EnUserCustomer=Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnUserCustomer.place(x=155, y=20)
            self.Bottow_Frame_LbCMNDCustomer = Label(self.Bottow, text="IDCardCustomer: ", font="arial 12 underline bold",
                                                     fg="#004d99", bg="#99ccff")
            self.Bottow_Frame_LbCMNDCustomer.place(x=16, y=50)
            self.Bottow_Frame_EnCMNDCustomer = Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnCMNDCustomer.place(x=155, y=50)
            self.Bottow_Frame_LbPhoneCustomer = Label(self.Bottow, text="PhoneCustomer: ", font="arial 12 underline bold",
                                                      fg="#004d99", bg="#99ccff")
            self.Bottow_Frame_LbPhoneCustomer.place(x=20, y=80)
            self.Bottow_Frame_EnPhoneCustomer = Entry(self.Bottow, bg="white", bd=4, width=25)
            self.Bottow_Frame_EnPhoneCustomer.place(x=155, y=80)
            Option_Combobox=["Day","Night"]
            self.Bottow_Frame_lbTimeSpend=Label(self.Bottow, text="UsedTime: ", font="arial 12 underline bold", bg="#99ccff", fg="#004d99")
            self.Bottow_Frame_lbTimeSpend.place(x=68, y=110)
            self.bottow_Frame_CbTimeSpend=Combobox(self.Bottow, values=Option_Combobox, width=23)
            self.bottow_Frame_CbTimeSpend.place(x=155, y=110)


            self.Bottow_Frame_BtnAdd=Button(self.Bottow, text="Add Customer", font="arial 10 underline bold", bg="white", fg="#004d99", width=15, command=self.Add_NewCustomer)
            self.Bottow_Frame_BtnAdd.place(x=420, y=40)
            self.Bottow_Frame_BtnSearch = Button(self.Bottow, text="Search Customer", font="arial 10 underline bold", bg="white", fg="#004d99", width=15, command=self.Search_Customer)
            self.Bottow_Frame_BtnSearch.place(x=420, y=80)
            '''
            Design Vien
            '''
            self.Bottow_Frame_LbVien=Label(self.Bottow, height=9)
            self.Bottow_Frame_LbVien.place(x=380, y=1)
    '''
    Hàm lấy giá trị nhập từ MVC để ghi vào object
    '''
    def GetModel(self):
        check=False
        if(self.Bottow_Frame_EnPhoneCustomer.get().isdigit() and self.Bottow_Frame_EnCMNDCustomer.get().isdigit()):
              check=True
        if(check==True):
            self.customer=CustomerController(self.Bottow_Frame_EnUserCustomer.get(), self.Bottow_Frame_EnPhoneCustomer.get(), self.Bottow_Frame_EnCMNDCustomer.get(), self.bottow_Frame_CbTimeSpend.get())
            if(self.customer.getName()=="" or self.customer.getID()=="" or self.customer.getPhone()=="" or self.customer.getUsedTime()==""):
                return mb.showerror("False","Bạn cần nhập đầy đủ thông tin khách hàng")
            else:
                Data_Show=["Name: "+self.customer.getName()," Phone: "+self.customer.getPhone()," CMND: "+self.customer.getID()," UsedTime: "+self.customer.getUsedTime()+"\n"]

            return Data_Show
        else:
            return mb.showerror("Error","Phone and IDCard are Number")
    def Add_NewCustomer(self):
        Gre=self.GetModel()
        Write_File = ReadAndOpenFile.Write_File_Customer(self)
        for i in Gre:
            Write_File.write(i)
        Write_File.close()
        Open_File=ReadAndOpenFile.Read_File_Customer(self)
        List_Show=Open_File.readlines()
        self.Scroll=Scrollbar(self.Bottow, width=20)
        self.Scroll.place(x=615, y=230)
        self.List_Box=Listbox(self.Bottow, yscrollcommand=self.Scroll.set, width=65, font="arial 12 bold", bd=5)
        self.Scroll.config(command=self.List_Box.yview)
        for i in range(len(List_Show)):
            self.List_Box.insert(END, str(i) + " " + List_Show[i])
        self.List_Box.place(x=20, y=230)
    def Search_Customer(self):
        Open_File=ReadAndOpenFile.Read_File_Customer(self)
        List_Show=Open_File.readlines()
        Open_File.close()
        Data_Show=list()

        if (self.Bottow_Frame_EnPhoneCustomer.get() == ""):
            return mb.showerror("Error", "Bạn chưa nhập Thông Tin Tìm Kiếm")
        else:
            for LINE in List_Show:
                if (self.Bottow_Frame_EnPhoneCustomer.get() in LINE):
                    Data_Show.append(LINE)
                    break
        if(self.Bottow_Frame_EnPhoneCustomer.get() not in LINE):
            mb.showerror("Error","Khách Hàng Không Tồn Tại")
        self.Bottow_Frame_Search=Entry(self.Bottow, width=55, font="arial 12 bold", bd=5)
        self.Bottow_Frame_Search.insert(END, Data_Show)
        self.Bottow_Frame_Search.place(x=20, y=160)


def main():
    Root_Customer = tk.ThemedTk()
    Root_Customer.get_themes()
    Root_Customer.set_theme("keramik")
    Root_Customer.iconbitmap("icon.ico")
    app = Data_Customer(Root_Customer)
    Root_Customer.title("DataCustomer")
    Root_Customer.geometry("650x550+350+200")
    Root_Customer.resizable(False, False)
    Root_Customer.mainloop()
if __name__=="__main__":
      main()