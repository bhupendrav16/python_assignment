def rotate(arr,d):
    size = len(arr)-d
    ans = []
    for i in range(size,len(arr)):
        ans.append(arr[i])
    for i in range(size ):
        ans.append(arr[i])
    return ans


arr =list( map( int,input().split()))
d = int(input())
print(rotate(arr,d))