
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

l = [1,23,4,5,66,22,17,13,9,10]

ret = bubbleSort(l)
print(ret)