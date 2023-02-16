class company():
    def details(self):
        self.name=input("Enter Name:")
        self.code=int(input("Enter code:"))
        self.salary=int(input("Enter salary:"))
        self.bonus=1000
    def increment(self):
        if(self.salary<20000):
            self.total=self.salary+self.bonus+((self.salary*10)/100)
            print("Total:",self.total)
        elif(self.salary>=21000 and self.salary<=30000):
            self.total=self.salary+self.bonus+((self.salary*10)/100)
            print("Total:",self.total)
        elif(self.salary>31000):
            self.total=self.salary+self.bonus+((self.salary*15)/100)
            print("Total:",self.total)

obj1=company()
obj1.details()
obj1.increment()
