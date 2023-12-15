def reversebyword(s):
    new_s = s.split()
    new_s.reverse()
    return " ".join(new_s)


s = input()
print(reversebyword(s))