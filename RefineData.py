class RefineData:
    def __init__(self,data_lst,num,errorlst) -> None:
        self.data_lst = data_lst
        self.error_lst = errorlst
        self.num = num


    def Bill_Ref(self):
        if self.data_lst[0] == None:
            return "-"
        else:
            return self.data_lst[0]

    def BP(self):
        if self.data_lst[6] == None or self.data_lst[6] == "":
            return "-"
        else:
            return self.data_lst[6]

    def Extract_City(self,data_lst):
        data_lst.reverse()
        k=0
        if len(data_lst[1])==2:
            k=2
        elif len(data_lst[2])==2:
            k=3
        else:
            k=4
        result = []

        while (k<len(data_lst)):
            result.append(data_lst[k])
            k+=1
        
        result.reverse()
        return ' '.join(result)

        
#3 Finally Getting City form the data
    def get_City(self):
        try:
            if self.data_lst[3] == None and self.data_lst[2] == None:
                second_elem = (str(self.data_lst[1]).split(" "))
                # print(1,second_elem)
                
            elif self.data_lst[3]== None: 
                second_elem = (self.data_lst[2].split(" "))
                # print(2,second_elem)
                           
            else:
                second_elem =  (self.data_lst[3].split(" "))
                # print(3,second_elem)
            
            cityName = self.Extract_City(second_elem)
            return cityName

        except Exception as E:
            self.error_lst.append(f"{self.num} City Error")
            return "-"

#4 Finally Getting Province form the data [E]-4        
    def get_Prov(self): #4
        try:
            data = (str(self.data_lst[4]).split(" "))[::-1]
            # print(data)
            if len(data[1])<=2:
                return data[1]
            else:
                return data[2]

        except Exception as E:
            self.error_lst.append(f"{self.num} Provience Error")

#5 Finally Getting Street Name form the data        
    def get_Str_Name(self):
        try:
            if "Box" in self.data_lst[7]:
                return "-"
            else:
                return self.data_lst[7]
        except Exception as E:
            self.error_lst.append(f"{self.num} Street Name Error")


#2 Finally Getting Postal Code form the data        
    def get_PC(self):
        try:
            f_postal_code = (self.data_lst[4].split(" "))[-1] 
            s_postal_code = (self.data_lst[4].split(" "))[-2]
            if (len(str(s_postal_code))) < 3:
                return f_postal_code
            else:
                return f_postal_code + s_postal_code
        except Exception as E:
            self.error_lst.append(f"{self.num} Postal Code Error")

   

    def get_Country(self):
        try:
            if self.data_lst[12] == None or len(self.data_lst[12])>2:
                return "-"
            else:
                return self.data_lst[12]
        except Exception as E:
            self.error_lst.append(f"{self.num} Country Error")

    def isInt(self,lst):
        try:
            num = int(lst[0])
            return True
        except:
            return False
        
    def get_Unit_no(self):
        lst = str(self.data_lst[1]).split(" ")
        try:
            if (self.isInt(lst)) and ("BOX" in str(self.data_lst[1]).upper()):
                k = 0
                for i in lst:   
                    if str(i).upper() == "BOX":
                        return f"{lst[k]} {lst[k+1]}"     
                    k+=1
                    
            if "BOX" in str(self.data_lst[1]).upper():
                # print("1st Condition")
                return self.data_lst[1]
            elif self.data_lst[3] != None:
                # print("2nd Condition")
                return self.data_lst[2]
            else:
                # print("3rd Condition")
                return "-"
        except Exception as E:
            self.error_lst.append(f"{self.num} Unit Number Error")

    #1 Finally Getting Street number form the data
    def get_Street_No(self):
        try:
            num = int(self.data_lst[8])
            return str(num)

        except Exception as E:
            if "BOX" in str(self.data_lst[8]).upper():
                return "-"
            else:
                num = self.data_lst[8].split(" ")[0]
                if (self.isInt(num)):
                    return num
                else: 
                    return "-"

    def filter(self):
        flt_tuple = (self.Bill_Ref(),self.BP(),self.get_Street_No(),self.get_Str_Name(),self.get_Unit_no(),self.get_City(),self.get_PC(),self.get_Prov(),self.get_Country())
        return tuple(flt_tuple),self.error_lst

if __name__ == '__main__':

    lst = ['4AA3A4213DF31AAFE10000000AAA0C0D', 'PO BOX 1166', 'EMBRUN ON K0A 1W0', None, 'PO BOX 1166EMBRUN ON K0A 1W0', None, '', 'Po Box 1166', 'PO BOX 556', '=RIGHT(E17,7)', 'Embrun', 'ON', 'CA', None, None, None, None, None]
    data = RefineData(lst,1)
    data.filter()