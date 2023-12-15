def sumoddinrange(s,e):
    sumodd = 0
    for i in range(s,e+1):
        #inclusive of end
        if i % 2 !=0 :
            sumodd += i 
    return sumodd 
s =int(input())
e = int(input())
print(sumoddinrange(s,e))