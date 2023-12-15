def common(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return list(arr1.intersection(arr2))


arr1 = list(map(int,input().split()))
arr2 = list( map(int,input().split()))
print(common(arr1,arr2))