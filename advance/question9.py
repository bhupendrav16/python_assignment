def runningl(s):
    cnt = 1 
    ans = ""
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            ans += s[i-1]
            ans += str(cnt)
            cnt = 1  
        else:
            cnt += 1
    ans += s[-1]
    ans += str(cnt) 
    return ans 

s= input()
print(runningl(s))
