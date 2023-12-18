def temp_analysis(arr):
    maxi = -1000
    mini = 1000
    s = 0
    for i in range(len(arr)):
        if maxi < arr[i]:
            maxi =arr[i]
        if mini > arr[i]:
            mini = arr[i]
        s += arr[i]
    avg = s/len(arr)
    return avg,maxi,mini 

temp = list( map( int ,input().split()))
avg ,maxi,mini = temp_analysis(temp)
print("Average Temperature:",avg)
print("Highest Temperature:",maxi)
print("Lowest Temperature:",mini)
