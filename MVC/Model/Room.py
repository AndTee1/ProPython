class Room:
    def __init__(self,IDRoom,Price,Kind,UsedTime,Status):
        self.IDRoom=IDRoom
        self.UsedTime=UsedTime
        self.Kind=Kind
        self.Price=Price
        self.Status=Status
    def getID(self):
        return self.IDRoom
    def getTime(self):
        return  self.UsedTime
    def getKind(self):
        return  self.Kind
    def getPrice(self):
        return self.Price
    def getStatus(self):
        return self.Status
    def setStatus(self,Status):
        self.Status=Status