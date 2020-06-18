from MVC.Model.Customer import Customer
from MVC.Model.Room import Room
class CustomerController:
    def __init__(self,Name=Customer.getName,Phone=Customer.getPhone,ID=Customer.getID,UsedTime=Customer.getTime):
        self.Name=Name
        self.Phone=Phone
        self.ID=ID
        self.UserTime=UsedTime
    def getName(self):
        return self.Name
    def getPhone(self):
        return self.Phone
    def getID(self):
        return self.ID
    def getUsedTime(self):
        return self.UserTime
class RoomController:
    def __init__(self,ID=Room.getID,Price=Room.getPrice,Kind=Room.getKind,UsedTime=Room.getTime,Status=Room.getStatus):
        self.ID=ID
        self.Price=Price
        self.Kind=Kind
        self.UsedTime=UsedTime
        self.Status=Status
    def getID(self):
        return self.ID
    def getPrice(self):
        return self.Price
    def getKind(self):
        return self.Kind
    def getUsedTime(self):
        return self.UsedTime
    def getStatus(self):
        return self.Status

class ReadAndOpenFile:
    def __init__(self,master):
        self.master=master
    def Write_File_Customer(self):
        Write_File_Cus = open("../../Data/datacus.txt", "a", encoding="utf-8")
        return Write_File_Cus
    def Read_File_Customer(self):
        Open_File_Cus = open("../../Data/datacus.txt", "r", encoding="utf-8")
        return  Open_File_Cus
    def Read_File_BAction(self):
        Open_File_BA = open("../../Data/actionhotel.txt", 'r', encoding="utf-8")
        return Open_File_BA
    def Write_File_BAction(self):
        Write_File_BA = open("../../Data/actionhotel.txt", 'w', encoding="utf-8")
        return Write_File_BA
    def Read_File_Room(self):
        Open_File_Room=open("../../Data/dataroom.txt", "r", encoding="utf-8")
        return Open_File_Room
    def AWrite_File_Room(self):
        Write_File_Room=open("../../Data/dataroom.txt", "a", encoding="utf-8")
        return Write_File_Room
    def WWrite_File_Room(self):
        WWrite_File_Room=open("../../Data/dataroom.txt", "w", encoding="utf-8")
        return WWrite_File_Room
    def Read_File_FeedBack(self):
        Open_File_FeedBack=open("../../Data/feedback.txt", "r", encoding="utf-8")
        return Open_File_FeedBack
    def Write_File_FeedBack(self):
        WWrite_File_FeedBack=open("../../Data/feedback.txt", "w", encoding="utf-8")
        return WWrite_File_FeedBack