def cnt_freq(arr):
    dic = {}
    for ele in arr:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic 
arr = list( map(int,input().split()))
print(cnt_freq(arr))