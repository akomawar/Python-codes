class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.attend=0
        self.marks=[]
        self.balance=0
        self.credit=20
##        print("Welcome {} to the school".format(name))
        print("Name of the student is {} and the age is {}".format(name,age))

    def addmarks(self,ma):
        self.marks.append(ma)
    def attenddays(self):
        self.attend +=1
    def getavg(self):
        return sum(self.marks)/len(self.marks)
    
    def __str__(self):
        return("Name of the student is {}\nthe age is {}".format(self.name,self.age))
    def __del__(self):
        print("the student {} does not exist".format(self.name))

p1=student('ankit',24)
p2=student('omkar',23)
print(p1)
print(p2)
del(p1)
del(p2)
