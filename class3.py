"""newlist = [1, 2, 4, 6, 5, 9, 122, 33]

lengthoflist = len(newlist)
sumoflist = sum(newlist)

print("lenth", len(newlist))

print("sum", sum(newlist))

print(sumoflist/lengthoflist)

#using python library

sum = 0
counter = 0

for x in newlist:
    sum = sum + x
    counter = counter + 1
    print(sum)
    print(counter)

print("sum from for loop", sum)
print("counter from for loop", counter)
print("average", sum/counter)
#more python version
"""
#summary
#growing variable (ex growing sum)
#for loop that does blahblah = pseudocode "fake code"


newlist = [12, 34, 65, 43, 25, 16, 45, 17, 78, 98, 4, 10]
"""largest = 0

for x in newlist:
    if x > largest:
        largest=x

print(largest)
"""
#printing largest

diff_original = abs(newlist[0] - newlist[1])
for x in range (len(newlist)):
    for y in range(x+1, len(newlist)): 
        difference = abs(newlist[x]-newlist[y])
        if difference < diff_original:
            diff_original = difference
    
print(diff_original)



#finding the smallest difference between the numbers in newlist