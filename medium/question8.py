def vowel(s):
    if (s =='a'or s =='e'or s =='i'or s =='o' or s =='u') or ( s == 'A' or s == 'E' or s== 'I' or s=='O' or s =='U'):
        return True 
    return False
def cntvowel( s):
    cnt = 0
    for ele in s:
        if (vowel(ele)) :
            cnt +=1 
    return cnt 

s = input()
print(cntvowel(s))