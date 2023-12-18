def powerof2(n):
    if n==0:
        return 1
    l =  powerof2(n//2) +n//2
    return l 

n = int(input())
if ( powerof2(n) == n):
    print("Power of 2")
else:
    print("Not a Power of 2")