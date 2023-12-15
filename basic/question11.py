
def single_digit(n):
    while ( n  > 9):
        s = 0
        while ( n > 0):
            s +=  n%10 
            n = n//10

        n= s 
        
    return n 
n = int(input())
print(single_digit(n))


