def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mitad = len(arr) // 2
        arr1 = merge_sort(arr[:mitad])
        arr2 = merge_sort(arr[mitad:])
        return merge(arr1, arr2)

arr = [1, 5, 2, 8, 3, 4, 5]
print(merge_sort(arr))
