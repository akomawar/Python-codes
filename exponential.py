num=int(input('Enter no.: '))
exp=int(input('enter the expo: '))
result=pow(num,exp)
print(result)

result=1

for i in range(1,(exp+1)):
    result=result*num
print(result)


result=1
i=1
while(i<=exp):
    result=result*num
    i+=1
print(result)
