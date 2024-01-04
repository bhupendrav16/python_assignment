def unique_elements(arr1):
    return list(set(arr1))

arr1 = list(map(int, input().split()))
print(unique_elements(arr1))
