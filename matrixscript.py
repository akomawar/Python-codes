import re

inp=input("Enter No. N (Rows) : ")
print(inp)

a=re.split(r'\s',inp)
print(a)

N=a[0]
M=a[1]
print(N)
print(M)

matrix=[]
temp=[]
for i in range(int(N)):
    matrix.append(input())
    
print(matrix)

for i in range(int(M)):
    for j in range(int(N)):
        temp.append(matrix[j][i])
print(temp)

temp1=''.join(temp)
print(temp1)

print(re.sub(r"(?=\w)", " ", temp1))
      
##(?<=\w)([^\w]+)(?=\w)
