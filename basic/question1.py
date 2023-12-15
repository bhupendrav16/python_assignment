def checkcondition(n):
    s = ""
    if n % 3 == 0 and n % 5 == 0:
        s += "Brudite-Python Training"
    elif n % 3 == 0 :
        s += "Brudite"
    elif n % 5 == 0:
        s += "Python Training"
    return s 
n = int(input())
print(checkcondition(n))