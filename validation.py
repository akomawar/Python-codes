class password:
    def constrains(self,s):
        self.s=s
    def __str__(self):
        return (self.s)
    def unique_chars_set(self,s):
        return len(s) == len(set(s))

T=int(input())
for i in range(T):
    a=password()
    a.constrains(input())
    j=0
    k=0
    l=0
    n=0
    symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
    if(a.unique_chars_set(a.s)):
        if (len(a.s)==10):
            for i in a.s:
                if(i.isupper()):
                    j+=1
            if(j>1):
                for i in a.s:
                    if(i.isalpha()==False):
                        k+=1
                if(k>=3):
                    for i in a.s:
                        if(i.isalnum()):
                            l+=1
                        
                    if(l==10):
                        print('Valid')
                    else:
                        print('Invalid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
                                    
                        
                   
