class number:
    def __init__(self,list):
        self.l=1
        self.list1=list1
    def evennumbers(self):
        return [num for num in self.list1 if num%2==0]
    def not_divisible(self):
        return [num for num in self.list1 if num%3!=0]
    
l=10
list1=[1,2,3,4,5,6,7,8,9,11]
print(list)
number=number(l,list1)
list2=number.evennumbers()
print(list2)
list3=number.not_divisible()
print(list3)