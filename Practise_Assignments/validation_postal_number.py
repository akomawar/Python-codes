import re


P=input("Enter postal number : ")
##print(P)

while(re.findall(r'\d{6}',P)):
    print('yes')
    temp=re.split(r'\D',P,re.I|re.M)
    print(temp[0])
    temp1=re.findall(r'\d',temp[0])
    print(temp1)
    temp2=re.match(r'\A[0]',temp1[0])
    print(temp2)
    while(temp2==None):
        print(temp1)
        t1=temp1[0]
        t2=temp1[1]
        t3=temp1[2]
        t4=temp1[3]
        t5=temp1[4]
        t6=temp1[5]
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(temp[0][0])
        while(temp[0][0]==temp[0][1])
        temp3=re.match(r'[t1.*]',t3,re.I|re.M)
        temp4=re.match(r'[t2.*]',t4,re.I|re.M)
        temp5=re.match(r'[t3.*]',t5,re.I|re.M)
        temp6=re.match(r'[t4.*]',t6,re.I|re.M)
        print(temp3)
        print(temp4)
        print(temp5)
        print(temp6)        
        break
##        while(t1==t3 or t2==t4 or  t3==t5 or t4==t6):
            

