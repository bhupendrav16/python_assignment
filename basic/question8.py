def hcf( n1,n2):
    if n1 == 0  :
        return n2 
    if n2 == 0:
        return n1 
    while ( n1 != n2):
        if ( n1 > n2 ):
            n1 = n1 - n2
        else:
            n2 = n2 -n1 
    return n1
def lcm ( n1,n2):
    h = hcf(n1,n2)
    return (n1*n2)//h 
n1 = int(input())
n2  = int(input())
print(lcm(n1,n2))