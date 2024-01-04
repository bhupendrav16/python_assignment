def without_using_comp(n,s):
    seen = [0]*26
    r =  0 
    occ = 0
    for i in range(len(s)):
        idx = ord(s[i]) - ord('A')
        if seen[idx] == 0:
            seen[idx] = 1 
            if occ < n:
                occ += 1
                seen[idx] = 2 
            else:
                r += 1
        else:
            if seen[idx] == 2:
                occ -= 1 
            seen[idx] = 0
    return r 
n = int(input())
s  = input()
print(without_using_comp(n,s))
    