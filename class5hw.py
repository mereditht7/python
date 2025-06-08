import random

x = random.randint(0,101)
print(x)
low = 0
high = x
mid = (low + high)/2

while high - low > 0.001:
    print(mid)
    if mid*mid>x:
        high = mid
    elif mid*mid<x:
        low = mid
    else:
        break
    mid = (low + high)/2
    print(x)