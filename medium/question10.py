def numofstone(n):
    res = []
    j = 0
    for i in range(n):

        res.append(n+j)
        j+=2 
    return res 
n = int(input())
print(numofstone(n))