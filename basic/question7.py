def anagram ( s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

s1 = input()
s2  =input()
if ( anagram(s1,s2)):
    print("anagram")
else:
    print("not a anagram")