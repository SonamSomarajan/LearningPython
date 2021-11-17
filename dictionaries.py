"""
9.4 Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail
messages. The program looks for 'From ' lines and takes
the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps
the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop
to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = dict()
l=list()
maxno = None
maxperson = None

for ite in handle:
    lst = ite.split()

    if len(lst) == 0:
        continue

    if lst[0] is "From":
        l.append(lst[1])

for i in l:
    d[i] = d.get(i,0)+1

for k, v in d.items():

    if maxno == None or v > maxno:
        maxno = v
        maxperson = k
        continue

print(maxperson, maxno)
