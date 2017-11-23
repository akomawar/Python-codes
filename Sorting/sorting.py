# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format
#
# A single line of input contains the string S.
#
# Constraints
#
# 0 < len(S) < 1000
#
# Output Format
#
# Output the sorted string S.
#
# Sample Input
#
# =====>> Sorting1234
# Sample Output
#
# =====>> ginortS1324
# Note:
# a) Using join, for or while anywhere in your code, even as substrings, was avoided.
# b) I only used one sorted function in code.

def sor(string):
    if string.isalpha():
        if string.islower():
            return 1
        else:
            return 2
    elif (int(string)%2!=0):
        return 3
    else:
        return 4
s=input()
a=sorted(s,key=lambda x:(sor(x),x))
print(*a,sep='')
