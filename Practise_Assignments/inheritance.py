class animal:
    def __init__(self,name,hands,legs):
        self.name=name
        self.hands=hands
        self.legs=legs
        print("Name of the animal is {}\nno. of hands it has is {}\nand legs {}".format(name,hands,legs))

class horse(animal):
    def print(self,name,hands,legs):
        animal.__init__(self,name,hands,legs)

class elephant(animal):
    def print(self,name,hands,legs):
        animal.__init__(self,name,hands,legs)
    
p1=animal('dynasore',4,2)
p1.name
p1.hands
p1.legs
print('\n')
p2=horse('male-horse',2,2)
p2.name
p2.hands
p2.legs
print('\n')
p3=elephant('baby',2,2)
p3.name
p3.hands
p3.legs
