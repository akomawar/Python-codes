# Neo has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
#
# Capture.JPG
#
# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.
#
# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
#
# Neo feels that there is no need to use 'if' conditions for decoding.
#
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
#
# Input Format
#
# The first line contains space-separated integers N (rows) and M (columns) respectively.
# The next N lines contain the row elements of the matrix script.
#
# Constraints
#
# 0 < N, M < 100
#
# Note: A 0 score will be awarded for using 'if' conditions in your code.
#
# Output Format
#
# Print the decoded matrix script.
#
# Sample Input
#
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
#
# Sample Output
#
# This is Matrix#  %!
#
# Explanation
# The decoded script is:
#
# This$#is% Matrix#  %!
# Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.
#
# So, the final decoded script is:
#
# This is Matrix#  %!


import re

inp=input()
##print(inp)

a=re.split(r'\s',inp)
##print(a)

N=a[0]
M=a[1]
##print(N)
##print(M)

matrix=[]
temp=[]
for i in range(int(N)):
    matrix.append(input())

##print(matrix)

for i in range(int(M)):
    for j in range(int(N)):
        temp.append(matrix[j][i])
##print(temp)

temp1=''.join(temp)
##print(temp1)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", temp1))
