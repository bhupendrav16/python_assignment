def pair(arr,k):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if ( arr[i] + arr[j] == k):
                cnt += 1
    return cnt 


arr = list(map(int,input().split()))
k = int(input())
print(pair(arr,k))