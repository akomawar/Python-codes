num = int(input('Enter the  number:  '))
j=1
for i in range(1,(num+1)):
    print('\n')
    while(j<=11):
        print(i,'*',j,'=',i*j)
        j+=1
    j=1

    
##    for j in range(1,11):
##        print(i,'*',j,'=',i*j)
##        
##i=1
##j=1
##while(i<=num):
##    while(j<=10):
##        print(i,'*',j,'=',i*j)
##        j+=1
##    i+=1
##    j=1
input("enter to exit")
