from tkinter import *
import datetime
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkthemes import themed_tk as tk
time=datetime.datetime.now().ctime()
time=str(time)
class feedback(object):
    def __init__(self,master):
        self.master = master
        # --Frame
        self.top = Frame(master, height=50, bg='white')
        self.top.pack(fill=X)
        self.bottow = Frame(master, height=600, bg="#99ccff")
        self.bottow.pack(fill=X)
        # design bo vien
        self.bottow_lbbo=Label(self.bottow,height=50).place(x=200,y=1)
        self.bottow_lbfeed=Label(self.bottow,text="FeedBackCustomer",font="arial 13 bold underline italic",fg="#004d99",bg="#99ccff").place(x=20,y=10)
        self.top_lbfb=Label(self.top,text="FeedBack And Growth chart",font="arial 20 bold underline italic",fg="#004d99",bg="white").place(x=280,y=10)
        # feedBack
        self.vb=IntVar()
        self.b=IntVar()
        self.ok=IntVar()
        self.g=IntVar()
        self.vg=IntVar()
        self.bottow_checkbtn_VBad=Checkbutton(self.bottow,text="Rất Không Hài Lòng",fg="#004d99",bg="#99ccff",variable=self.vb,font="arial 12 bold underline italic").place(x=10,y=40)
        self.bottow_checkbtn_Bad = Checkbutton(self.bottow, text="Không Hài Lòng", fg="#004d99", bg="#99ccff",
                                               font="arial 12 bold underline italic",variable=self.b).place(x=10, y=70)
        self.bottow_checkbtn_OK = Checkbutton(self.bottow, text="Chấp Nhận Được", fg="#004d99", bg="#99ccff",
                                               font="arial 12 bold underline italic",variable=self.ok).place(x=10, y=100)
        self.bottow_checkbtn_Good = Checkbutton(self.bottow, text="Hài Lòng", fg="#004d99", bg="#99ccff",
                                               font="arial 12 bold underline italic",variable=self.g).place(x=10, y=130)
        self.bottow_checkbtn_VGood = Checkbutton(self.bottow, text="Rất Hài Lòng", fg="#004d99", bg="#99ccff",
                                               font="arial 12 bold underline italic",variable=self.vg).place(x=10, y=160)
        self.bottow_btn_OK=Button(self.bottow,text="Xác Nhận",font="arial 12 bold underline",fg="#004d99",bd=4,width=13,command=self.xacnhan).place(x=10,y=200)
        self.bottow_lb_chuthich=Label(self.bottow,text="B:Rất Không Hài Lòng \n BD:Không Hài Lòng \n OK:Chấp nhận được \n UG:Tốt \n VG:Rất Tốt",fg="#004d99",bg="#99ccff",font="arial 10 bold italic").place(x=10,y=280)
        # do thi

    def FeedBack(self):
        g = open("feedback.txt", "r", encoding="utf-8")
        a = g.read().split(" ")
        self.c = list()
        for i in a:
            self.c.append(int(i))
        for i in range(len(self.c)):
            if(self.vb.get()==1):
                self.c[0]+=10
                break
            elif(self.b.get()==1):
                self.c[1] += 10
                break
            elif (self.ok.get() == 1):
                self.c[2] += 10
                break
            elif (self.g.get() == 1):
                self.c[3] += 10
                break
            elif (self.vg.get() == 1):
                self.c[4] += 10
                break
        b=list()
        for i in range(len(self.c)):
            b=[str(self.c[0])+" ",str(self.c[1])+" ",str(self.c[2])+" ",str(self.c[3])+" ",str(self.c[4])]
        f = open("feedback.txt", "w", encoding="utf-8")
        for i in b:
            f.write(i)
        f.close()
        return self.c
    def xacnhan(self):
        gre=self.FeedBack()
        data1 = {'FeedBack': ['B', 'BD', 'OK', 'UG', 'VG'],
                 'Growth_Speed': gre
                 }
        df1 = DataFrame(data1, columns=['FeedBack', 'Growth_Speed'])
        figure1 = plt.Figure(figsize=(6, 5), dpi=95)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.bottow)
        bar1.get_tk_widget().place(x=300, y=20)
        df1 = df1[['FeedBack', 'Growth_Speed']].groupby('FeedBack').sum()
        df1.plot(kind='line', legend=True, ax=ax1,marker="o")
        ax1.set_title('FeedBack Vs. Growth_Speed')


def main4():
    windown = tk.ThemedTk()
    app = feedback(windown)
    windown.get_themes()
    windown.iconbitmap("icon.ico")
    windown.set_theme("keramik")
    # windown.bind('<Return>', app.setup)
    windown.title("Business activities")
    windown.geometry("950x550+350+200")
    windown.resizable(False, False)
    windown.mainloop()
if __name__=="__main__":
    main4()