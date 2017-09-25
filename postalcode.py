class postalcode:
    def postalnum(self,number):
        self.number=number
    def __str__(self):
        return(self.number)


a=postalcode()
a.postalnum('122312')
print(a.number)

while(len(a.number)==6):
    b=list(a.number)
    print(b)
    break
    for i in range(len(b)):
        print('y')
        break
    
