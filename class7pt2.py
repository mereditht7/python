"""
def sum_of_digits(x):
    sum_of_digits = 0
    for i in range (len(str(x))):
        remainder = x%10
        sum_of_digits = sum_of_digits + remainder
        if sum_of_digits == 0:
            return
        else:
            x = x //10
    print(sum_of_digits)
    return(sum_of_digits)
print(sum_of_digits (1234))
#adding digits of a number
"""

def sum_of_digits (n):
    if n == 0:
        return (0)
    print(n)
    return (n%10 + sum_of_digits(n//10))
print(sum_of_digits(1234))

def sequence (n):
    if n==0 or n==1:
        return(0)
    print(n)
    return ((n-1)+(n-2))
print(sequence(3))