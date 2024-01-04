def userdata(s):
    new_s = s.split('0')
    l = [ele for ele in new_s if len(ele)!=0]
    if l[2].isdigit():
        return  {"first_name":l[0],"second_name": l[1], 'id':l[2]}
    return {}
s = input()
print(userdata(s))

