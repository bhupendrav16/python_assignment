def error( arr, index):
    try:
        res = arr[index]
        print(f"data at index {index}:")
        return res
    except IndexError:
        return "Index out of range"

arr = [1,2,3,4]
index = int(input())
print(error(arr,index))
