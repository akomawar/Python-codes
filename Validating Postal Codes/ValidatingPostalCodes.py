# A postal code  must be a number in the range of (100000-999999).
# A postal code  must not contain more than one alternating repetitive digit pair.
#
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
#
# For example:
#
# 121426 # Here, 1 is an alternating repetitive digit.
# 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits.
# Your task is to validate whether  is a valid postal code or not.
#
# Input Format
#
# One single line of input containing the string .
#
# Output Format
#
# Prints "True" if  is valid. Otherwise, prints "False"


import re

P=input()
k=[]
m=0
while(len(re.findall(r'\d',P,re.I|re.M))==6):
    temp=re.split(r'\D',P,re.I|re.M) ##spliting the string
    temp1=re.findall(r'\d',temp[0]) ## finding numbers
    temp2=re.match(r'\A[0]',temp1[0])
    while(temp2==None):
        k.append(P[0]==P[2])
        k.append(P[1]==P[3])
        k.append(P[2]==P[4])
        k.append(P[3]==P[5])
        m=sum(k)
        while(m<=1):
            print('True')
            break
        while(m>1):
            print('False')
            break
        break
    break
while(len(re.findall(r'\d',P,re.I|re.M))!=6):
    print('False')
    break
