def median(arr):
    arr.sort()
    mid = len(arr)//2 
    median = 0
    if len(arr) % 2== 0:
        median = (arr[mid] + arr[mid- 1])/2
    else:
        median = arr[mid] 
    return median

arr = list( map ( int , input().split()))
print("Median", median(arr))