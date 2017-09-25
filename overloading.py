class apt42:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def __str__(self):
        return ("City : {}\nState : {}".format(self.city,self.state))

s1=apt42('Chico','California')
print(s1)

class roomates(apt42):
    def __init__(self,name,age,city,state):
        apt42.__init__(self,city,state)
        self.name=name
        self.age=age
    def __str__(self):
        return ("\nName : {}\nAge : {}\n".format(self.name,self.age)+apt42.__str__(self))

s2=roomates('AK',24,'Chico','California')
print(s2)

class postalcode(apt42):
    def __init__(self,city,state,postal):
        apt42.__init__(self,city,state)
        self.postal=postal
    def __str__(self):
        return(apt42.__str__(self)+"\nPostal Code : {}".format(self.postal))

s3=postalcode("Chico","CAL",95928)
print(s3)
