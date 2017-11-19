import time
num=int(input("Enter your number"))
for i in range(1,(num+1)):
    print('\n')
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
    time.sleep(3)
    input()
    
