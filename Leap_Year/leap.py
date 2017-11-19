# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source
#
# Task
# function to check if the year is leap or not.
#
# Input Format
#
# Read y, the year that needs to be checked.
#
# Constraints
#
#
# Output Format
#
# Your function must return a boolean value (True/False)

def is_leap(year):
    leap = False
    if(year>=1900 and year<=10**5):
        if(year%400==0):
            leap=True
        elif(year%100==0):
            leap=False
        elif(year%4==0):
            leap=True
        return leap

year = int(input())
print(is_leap(year))
