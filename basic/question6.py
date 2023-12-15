def perfectn(n):
    per = 0
    for i in range(1,n):
        if ( n % i == 0):
            per   +=  i 
    return per == n 

n = int(input())
if ( perfectn(n)):
    print("perfect")
else:
    print("imperfect")