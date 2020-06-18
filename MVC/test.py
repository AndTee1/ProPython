from MVC.cus import Customer
def isObject():
    cus=Customer(NameCustomer=None,PhoneCustomer=None,CMNDCustomer=None,UsedTime=None)
    return cus
def getModel():
    gre=isObject()
    print(gre)
getModel()