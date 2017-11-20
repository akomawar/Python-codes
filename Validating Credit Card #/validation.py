# You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.
#
# Examples:
#
# Valid Credit Card Numbers
#
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
# Invalid Credit Card Numbers
#
# 42536258796157867       #17 digits in card number → Invalid
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

# Input Format
#
# The first line of input contains an integer N.
# The next N lines contain credit card numbers.
#
# Constraints
# 0 < N < 100
#
# Output Format
#
# Prints 'Valid' if the credit card number is valid. Otherwise, prints 'Invalid'.

class creditcard:
    def cardnumber(self,number):
        self.number=number
    def __str__(self):
        return (self.number)
    def unique_chars_set(self,s):
        return len(s) == len(set(s))

N=int(input())
for i in range(N):
    a=creditcard()
    a.cardnumber(input())
    num='0123456789-'
    hyphen='-'
    start='456'
    k=0
    m=0
    n=0
    p=0
    q=[]
    s=0
    r=[]
   ## print(a.number)
 ##   print(len(a.number))
    if(len(a.number)==19 or len(a.number)==16):
  ##      print('In')
        for i in a.number:
            if i in num:
                k+=1
        if(k==19 or k==16):
            for i in a.number:
                if i in hyphen:
                    m+=1
        if(m==3):
            temp=a.number.split('-')
            for i in temp:
                if (len(i)==4):
                    n+=1
            if(n==4):
                for i in a.number[0]:
                    if i in start:
                        p+=1
                    else:
                        print('Invalid')

                if(p==1):
                    q=list(a.number)
##                    print(q)
                    q.remove('-')
                    q.remove('-')
                    q.remove('-')

##                    print(q)
                    for i in range(len(q)-3):
                        if(q[i]==q[i+1] and q[i]==q[i+2] and q[i]==q[i+3]):
                            s+=1

                    if(s==0):
                        print('Valid')
                    else:
                        print('Invalid')
            else:
                print('Invalid')

        elif(m==0):
            for i in a.number[0]:
                    if i in start:
                        p+=1
                    else:
                        print('Invalid')
            if(p==1):
                q=list(a.number)
                for i in range(len(q)-3):
                    if(q[i]==q[i+1] and q[i]==q[i+2] and q[i]==q[i+3]):
                        s+=1
                if(s==0):
                    print('Valid')
                else:
                    print('Invalid')

    else:
        print('Invalid')
