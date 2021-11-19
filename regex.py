"""
In this assignment you will read through and parse a file
with text and numbers. You will extract all the numbers in
the file and compute the sum of the numbers.
"""

"""
Since it is a program with regular expressions, always
start by importing the library "re".
"""

import re

#Opening file:

fname = input("Enter the name of the file you would like to open.")
if len(fname)<1:
    fname = "actual.txt"
fhandle = open(fname)
numlist = list()

#Reading through file:

for line in fhandle:
    r = line.rstrip()
    #Regular expression to return a list of numbers
    y = re.findall('[0-9]+', r)

    if len(y) == 0:
        continue

    #Loop to add each number into numist:

    for num in y:
        x = int(num)
        numlist.append(x)

print(numlist)

#Loop to add all the numbers.
#Sum is stored in the variable "sum".

sum = 0

for iterate in numlist:
    sum  = sum + iterate

print("Sum :", sum)
