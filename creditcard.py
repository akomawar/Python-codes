class creditcard:
    def cardnumber(self,number):
        self.number=number
    def __str__(self):
        return (self.number)
    def unique_chars_set(self,s):
        return len(s) == len(set(s))

n=int(input())
for i in range(n):
    a=creditcard()
    a.cardnumber(input())
    num='0123456789-'
    hyphen='-'
    start='456'
    k=0
    m=0
    n=0
    p=0
    q=[]
    s=0
   ## print(a.number)

    if(len(a.number)==19 or len(a.number)==16):
    ##    print('yes')
        for i in a.number:
            if i in num:
                k+=1          
            else:
                print('Invalid')
        if(k==19 or k==16):
            for i in a.number:
                if i in hyphen:
                    m+=1
        if(m==3):
     ##       print('hyphen success')
            temp=a.number.split('-')
            for i in temp:
                if (len(i)==4):
                    n+=1
                else:
                    print('Invalid')
            if(n==4):
                for i in a.number[0]:
                    if i in start:
                        p+=1
                    else:
                        print('Invalid')
                
                if(p==1):
      ##              print('In')
                    q=list(a.number)
      ##              print(q)
                    for i in range(len(q)-3):
                        if(q[i]==q[i+1] and q[i]==q[i+2] and q[i]==q[i+3]):
                           ## print('Invalid')
                            s+=1
                            
                    if(s==0):
                        print('Valid')
                    else:
                        print('Invalid')
                    
                        
        elif(m==0):
            for i in a.number[0]:
                    if i in start:
                        p+=1
                    else:
                        print('Invalid')
            if(p==1):
      ##          print('In')
                q=list(a.number)
      ##          print(q)
                for i in range(len(q)-3):
                    if(q[i]==q[i+1] and q[i]==q[i+2] and q[i]==q[i+3]):
                        ##print('Invalid')
                        ##break
                        s+=1
                if(s==0):
                    print('Valid')
                else:
                    print('Invalid')
                    
    else:
        print('Invalid')

else:
    print('Invalid')
    
