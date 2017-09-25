import re
s=(input())
c=[]
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small='abcdefghijklmnopqrstuvwxyz'
odd='13579'
even='02468'
out=''
a=re.findall(r'\D',s)
b=re.findall(r'\d',s)
for i in small:
    if i in a:
        c.append(i)
for i in cap:
    if i in a:
        c.append(i)
for i in odd:
    if i in b:
        c.append(i)
for i in even:
    if i in b:
        c.append(i)
for i in c:
    out += i
print(out)
        
def checkPr(letter):
    if letter.isalpha():
        if letter.islower():
            return 1
        else:   return 2
    elif int(letter)%2==1:   return 3
    else:   return 4

word = input()
arr = sorted(word,key= lambda x: (checkPr(x),x) )
print(*arr,sep='')
