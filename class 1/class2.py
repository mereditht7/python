#first question combine these two lists into a new list [1, 2, 3, 4, 5, 6]
thislist1 = [1, 2, 3]
thislist2 = [4, 5, 6]

newlist1 = [ ]

for x in range (0,3):
    newlist1.append (thislist1[x])

for x in range (0,3):
    newlist1.append (thislist2[x])

print(newlist1)

#second question combine these two lists into a new list [1, 2, 3, 4, 5, 6]
thislist3 = [1, 3, 5]
thislist4 = [2, 4, 6]

newlist2 = [ ]
for x in range (0,3):
    newlist2.append (thislist3[x])
    newlist2.append (thislist4[x])

print(newlist2)

#third question sum all the numbers from the question above
sum = 0
for x in range (0,3):
    sum = sum + thislist3[x] + thislist4[x]

print(sum)

#fourth question add 7 to thislist3
thislist5 = [1, 3, 5, 7, 9, 11]
thislist4 = [2, 4, 6]
newlist4 = [ ]

lengthlist1 = len(thislist5)
lengthlist2 = len(thislist4)
"""
if lengthlist1 > lengthlist2:
    longerlengthlist=lengthlist1
else: 
    longerlengthlist=lengthlist2
"""

for x in range (max (lengthlist1, lengthlist2)):
    print(x)
    if x < len(thislist5):
        newlist4.append (thislist5[x])
        print(newlist4)
    if x < len(thislist4):
        newlist4.append (thislist4[x])
        print(newlist4)

print(newlist4)