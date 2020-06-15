def Write_File_Customer():
    Write_File_Cus = open("../../Data/datacus.txt", "a", encoding="utf-8")
    return Write_File_Cus
def Read_File_Customer():
    Open_File_Cus = open("../../Data/datacus.txt", "r", encoding="utf-8")
    return  Open_File_Cus
def Read_File_BAction():
    Open_File_BA = open("../../Data/actionhotel.txt", 'r', encoding="utf-8")
    return Open_File_BA
def Write_File_BAction():
    Write_File_BA = open("../../Data/actionhotel.txt", 'w', encoding="utf-8")
    return Write_File_BA
def Read_File_Room():
    Open_File_Room=open("../../Data/dataroom.txt", "r", encoding="utf-8")
    return Open_File_Room
def AWrite_File_Room():
    Write_File_Room=open("../../Data/dataroom.txt", "a", encoding="utf-8")
    return Write_File_Room
def WWrite_File_Room():
    WWrite_File_Room=open("../../Data/dataroom.txt", "w", encoding="utf-8")
    return WWrite_File_Room
def Read_File_FeedBack():
    Open_File_FeedBack=open("../../Data/feedback.txt", "r", encoding="utf-8")
    return Open_File_FeedBack
def Write_File_FeedBack():
    WWrite_File_FeedBack=open("../../Data/feedback.txt", "w", encoding="utf-8")
    return WWrite_File_FeedBack