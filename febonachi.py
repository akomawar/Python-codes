while 1:
    num=int(input("Enter Number: "))
    j=[]
    j.append(0)
    j.append(1)
    if(num==0 or num==1):
            print("Fibonachi Series : ",num)
    else:
        for i in range(2,num+1):
            j.append(j[i-1]+j[i-2])
        print("Fibonachi Series : ",j)

    
    
