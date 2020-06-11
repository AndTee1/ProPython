class Customer:
    def __init__(self,NameCustomer,PhoneCustomer,CMNDCustomer,UsedTime):
        self.NameCustomer=NameCustomer
        self.PhoneCustomer=PhoneCustomer
        self.CMNDCustomer=CMNDCustomer
        self.UsedTime=UsedTime
    def getName(self):
        return self.NameCustomer
    def setName(self,NameCustomer):
        self.NameCustomer=NameCustomer
    def getPhone(self):
        return self.PhoneCustomer
    def setPhone(self,PhoneCustomer):
        self.PhoneCustomer=PhoneCustomer
    def getCMND(self):
        return self.CMNDCustomer
    def setCMND(self,CMNDCustomer):
        self.CMNDCustomer=CMNDCustomer
    def getTime(self):
        return self.UsedTime

