def gcd (a,b):
    if b==0:
        return(a)
    print(a)
    return(gcd(b, a%b))
print(gcd(1424,3084))