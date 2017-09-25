if __name__ == '__main__':
    n = int(input())
    c=0
    if(n>0):
        if(n<10):
            for i in range(n):
                c=c*10+(i+1)
            print(c)
        elif(n>=10 and n<100):
            for i in range(9):
                c=c*10+(i+1)
            for i in range(10,(n+1)):
                c=c*100+i
            print(c)
        elif(n>=100 and n<1000):
            for i in range(9):
                c=c*10+(i+1)
            for i in range(10,100):
                c=c*100+i
            for i in range(100,(n+1)):
                c=c*1000+i
            print(c)
        elif(n>=1000 and n<10000):
            for i in range(9):
                c=c*10+(i+1)
            for i in range(10,100):
                c=c*100+i
            for i in range(100,1000):
                c=c*1000+i
            for i in range(1000,n+1):
                c=c*10000+i
            print(c)
