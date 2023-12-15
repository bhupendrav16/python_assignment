def alpha( s):
    if ( s >= 'a' and s <='z'  or  s>='A' and  s<= 'Z'):
        return True 
    return False 

def count_alph_n(s):
    cntalpha = 0
    cntnumber = 0
    for ele in s:
        if ( alpha(ele) == 1):
            cntalpha += 1
        if (ele.isnumeric()):
            cntnumber += 1 
    return cntalpha,cntnumber

s = input()
alph , number = count_alph_n(s)
print("alpha =", alph , "number = ",number)
        