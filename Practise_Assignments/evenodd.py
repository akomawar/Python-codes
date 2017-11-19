n = int(input("Enter your number : "))
if (n>=1 or n<=100):
    if(n%2==1):
        print('Weird')
    elif(n%2==0):
        if(2<=n and n<=5):
            print('Not Weird')
        elif(6<=n and n<=20):
            print('Weird')
        else:
            print('Not Weird')
    

