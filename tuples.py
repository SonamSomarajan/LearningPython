"""
10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the
'From ' line by finding the time and then splitting the
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print
out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
secondlist = list()
thirdlist = list()
fourthlist = list()
firstdictionary = dict()

"""
First list contains all the bits of each
line in the file in the form of a list.
"""
for it in handle:
    firstlist = it.split()

    if len(firstlist) == 0:
        continue

#"""
#Secondlist is a list that contains the
#time those lines that start with the word "From".
#"""
    if firstlist[0] == "From":
        secondlist.append(firstlist[5])

"""
Thirdlist is a list that contains only the hour
element of time, taken from the second list, of
the mails that start with "From".
"""
for it in secondlist:
    n = it.split(":")
    thirdlist.append(n[0])

"""
Firstdictionary is a dictionary that conatins the
hour element of time and histogram of the occurance
of each hour.
key = hour
value = histogram
"""
for it in thirdlist:
    firstdictionary[it] = firstdictionary.get(it,0)+1

"""
Fourthlist is a list of tuples containing the exact
same values as Firstdictionary. Difference is that
the key and value has been flipped.
key = histogram
value = hours
"""

for key, value in firstdictionary.items():
    newtuple = (key, value)
    fourthlist.append(newtuple)

"""
Sorting items of fourthlist:
"""
print(fourthlist)

fourthlist = sorted(fourthlist)

for value, key in fourthlist:
    print(value, key)

#fourthlist = sorted([(v, k) for k, v in firstdictionary.items()])
