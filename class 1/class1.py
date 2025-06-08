
for x in range (11):
    for y in range (11):
        product=x*y
        print(x * y, end =" ")
        if product<10:
            print (" ", end = " ")
        if product<100 and product>10:
            print ("", end = " ")
    print()

#int string list
# order is 0,1,2
"""
thislist = ["apple", "bannana", "cherry"]
print(thislist[0])
print(thislist[1])
print(thislist[2])
"""

#run all the strings
"""thislist = ["apple", "bannana", "cherry"]
for x in range(3):
    print(thislist[x])
"""

#run till last string using lengthlist
#with skipping strings
"""thislist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

lengthlist = len(thislist)

for x in range (0, lengthlist, 2):
    print(thislist[x])

#last string
print(thislist[-1])

#print a certain about
print(thislist [2:5])
"""
#printing a certain range with colons and for loops
"""thislist = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J"]
print(thislist [3:8])

thislist2 = [ ]
for x in range (3,8):
    thislist2.append (thislist[x])
print(thislist2)
"""

#assign a new numer
"""thislist[1] = 2
"""

#add a string
"""thislist.append("K")
"""

thislist = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J"]

#remove
thislist.remove("A")

#find a certain index number
index = thislist.index("E")
print(index)

index2 = thislist.index("H")
print(index2)
print("other way", thislist[index:index2])
for x in range (index, index2):
    thislist2.append(thislist[x])