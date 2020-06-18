from tkinter import *
import datetime
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from MVC.Controller.OpenAndCloseFile import ReadAndOpenFile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkthemes import themed_tk as tk

time = datetime.datetime.now().ctime()
time = str(time)


class Feedback(object):
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
        self.Bottow_Lbbo = Label(self.Bottow, height=50).place(x=200, y=1)
        self.Bottow_LbFeedBack = Label(self.Bottow, text="FeedBackCustomer", font="arial 13 bold underline italic",
                                       fg="#004d99", bg="#99ccff").place(x=20, y=10)
        self.Top_LbFb = Label(self.Top, text="FeedBack And Growth chart", font="arial 20 bold underline italic",
                              fg="#004d99", bg="white").place(x=280, y=10)
        '''
        Design Bottow Frame
        '''
        self.VeryBad = IntVar()
        self.Bad = IntVar()
        self.OK = IntVar()
        self.Good = IntVar()
        self.VeryGood = IntVar()
        self.Bottow_CheckBtn_VBad = Checkbutton(self.Bottow, text="Rất Không Hài Lòng", fg="#004d99", bg="#99ccff",
                                                variable=self.VeryBad, font="arial 12 bold underline italic").place(x=10,
                                                                                                                    y=40)
        self.Bottow_CheckBtn_Bad = Checkbutton(self.Bottow, text="Không Hài Lòng", fg="#004d99", bg="#99ccff",
                                               font="arial 12 bold underline italic", variable=self.Bad).place(x=10, y=70)
        self.Bottow_CheckBtn_OK = Checkbutton(self.Bottow, text="Chấp Nhận Được", fg="#004d99", bg="#99ccff",
                                              font="arial 12 bold underline italic", variable=self.OK).place(x=10,
                                                                                                             y=100)
        self.Bottow_CheckBtn_Good = Checkbutton(self.Bottow, text="Hài Lòng", fg="#004d99", bg="#99ccff",
                                                font="arial 12 bold underline italic", variable=self.Good).place(x=10,
                                                                                                                 y=130)
        self.Bottow_CheckBtn_VGood = Checkbutton(self.Bottow, text="Rất Hài Lòng", fg="#004d99", bg="#99ccff",
                                                 font="arial 12 bold underline italic", variable=self.VeryGood).place(x=10,
                                                                                                                      y=160)
        self.Bottow_BtnOK = Button(self.Bottow, text="Xác Nhận", font="arial 12 bold underline", fg="#004d99", bd=4,
                                   width=13, command=self.Accept).place(x=10, y=200)
        self.Bottow_LbNote = Label(self.Bottow,
                                   text="B:Rất Không Hài Lòng \n BD:Không Hài Lòng \n OK:Chấp nhận được \n UG:Tốt \n VG:Rất Tốt",
                                   fg="#004d99", bg="#99ccff", font="arial 10 bold italic").place(x=10, y=280)

    '''
    Fun Cộng Điểm FeedBack vào Valus của dict ở Fun Accept()
    '''
    def FeedBack(self):
        Open_File = ReadAndOpenFile.Read_File_FeedBack(self)
        List_Show = Open_File.read().split(" ")
        Open_File.close()
        self.DataFile = list()
        for i in List_Show:
            self.DataFile.append(int(i))
        for i in range(len(self.DataFile)):
            if (self.VeryBad.get() == 1):
                self.DataFile[0] += 10
                break
            if (self.Bad.get() == 1):
                self.DataFile[1] += 10
                break
            if (self.OK.get() == 1):
                self.DataFile[2] += 10
                break
            if (self.Good.get() == 1):
                self.DataFile[3] += 10
                break
            if (self.VeryGood.get() == 1):
                self.DataFile[4] += 10
                break
        Date_Show = list()
        for i in range(len(self.DataFile)):
            Date_Show = [str(self.DataFile[0]) + " ", str(self.DataFile[1]) + " ", str(self.DataFile[2]) + " ", str(self.DataFile[3]) + " ", str(self.DataFile[4])]
        Write_File = ReadAndOpenFile.Write_File_FeedBack(self)
        for i in Date_Show:
            Write_File.write(i)
        Write_File.close()
        return self.DataFile
    '''
    Fun Show And Update biểu đồ Feedback
    '''
    def Accept(self):
        Valus_Y = self.FeedBack()
        Data_Brand = {'FeedBack': ['B', 'BD', 'OK', 'UG', 'VG'],
                 'Growth_Speed': Valus_Y
                 }
        DF1 = DataFrame(Data_Brand, columns=['FeedBack', 'Growth_Speed'])
        Figure1 = plt.Figure(figsize=(6, 5), dpi=95)
        Ax1 = Figure1.add_subplot(111)
        Bar1 = FigureCanvasTkAgg(Figure1, self.Bottow)
        Bar1.get_tk_widget().place(x=300, y=20)
        DF1 = DF1[['FeedBack', 'Growth_Speed']].groupby('FeedBack').sum()
        DF1.plot(kind='line', legend=True, ax=Ax1, marker="o")
        Ax1.set_title('FeedBack Vs. Growth_Speed')


def main4():
    Root_FeedBack = tk.ThemedTk()
    Feedback(Root_FeedBack)
    Root_FeedBack.get_themes()
    Root_FeedBack.iconbitmap("icon.ico")
    Root_FeedBack.set_theme("keramik")
    Root_FeedBack.title("Business activities")
    Root_FeedBack.geometry("950x550+350+200")
    Root_FeedBack.resizable(False, False)
    Root_FeedBack.mainloop()


if __name__ == "__main__":

    main4()

