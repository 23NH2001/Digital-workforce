class RefineData:
    def __init__(self,data_lst,num,errorlst) -> None:
        self.data_lst = data_lst
        self.error_lst = errorlst
        self.num = num

    def Bill_Ref(self):
        pass

    def BP(self):
        pass

    def Extract_City(self,data_lst):
        pass

    def get_City(self):
        pass
        
    def get_Prov(self): 
        pass

    def get_Str_Name(self):
        pass

    def get_PC(self):
        pass

    def get_Country(self):
        pass

    def isInt(self,lst):
        pass
        
    def get_Unit_no(self):
        pass

    def get_Street_No(self):
        pass

    def filter(self)->list:
        # flt_tuple = (self.Bill_Ref(),self.BP(),self.get_Street_No(),self.get_Str_Name(),self.get_Unit_no(),self.get_City(),self.get_PC(),self.get_Prov(),self.get_Country())
        # return tuple(flt_tuple),self.error_lst
        pass

if __name__ == '__main__':

    lst = ['4AA3A4213DF31AAFE10000000AAA0C0D', 'PO BOX 1166', 'EMBRUN ON K0A 1W0', None, 'PO BOX 1166EMBRUN ON K0A 1W0', None, '', 'Po Box 1166', 'PO BOX 556', '=RIGHT(E17,7)', 'Embrun', 'ON', 'CA', None, None, None, None, None]    
    data = RefineData(lst,1)
    data.filter()