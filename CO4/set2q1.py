class mcas1:
    def get(self):
        self.name=input("Enter Name:")
        self.roll=int(input("Enter ROllNo:"))
    def display(self):
        print("Name:",self.name)
        print("RollNo:",self.roll)
class test(mcas1):
    def grades(self):
        self.mark1=int(input("Enter mark 1:"))
        self.mark2=int(input("Enter mark 2:"))
        self.mark3=int(input("Enter mark 3:"))
    def gradesdisplay(self):
        self.per=((self.mark1+self.mark2+self.mark3)/300)*100
        print(self.per)
        if self.per>=90:
            print("Grade A")
        elif self.per>=80 and self.per<90:
            print("Grade B")
        elif self.per>=70 and self.per<80:
            print("Grade C")
        elif self.per>=60 and self.per<70:
            print("Grade D")
        else:
            print("Failed")

obj1=test()
obj1.get()
obj1.grades()
obj1.display()
obj1.gradesdisplay()