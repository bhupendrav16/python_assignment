def unique(arr1):
    d = {}
    for ele in arr1:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    ans = []
    for ele in d:
        if ( d[ele] == 1):
            ans.append(ele)
    return ans
arr1 = list(map(int,input().split()))
print(unique(arr1))