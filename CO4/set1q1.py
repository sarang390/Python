class student:
    def display(self,a,b):
        self.a=a
        self.b=b
        print("MCAS1:")
        print(self.a)
        print("MCAS2:")
        print(self.b)
        print("After merging:")
        self.c=self.a+self.b
        print(self.c)
    def insert(self):
        (self.a).append("e")
        print(self.a)
    def sorting(self):
        print(sorted(self.a))
        print(sorted(self.b))
    def search(self,element):
        self.element=element
        if self.element in self.b:
            print("Element found")
        else:
            print("Not found")

MCAS1=["a","d","c"]
MCAS2=["f","d"]
obj1=student()
obj1.display(MCAS1,MCAS2)
print("After inserting a new element to MCAS1:")
obj1.insert()
print("After sorting:")
obj1.sorting()
n=input("Enter the element to search:")
obj1.search(n)