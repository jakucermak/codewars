def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]



arr = [64, 34, 25,11, 12, 22, 11, 90,64]
bubble_sort(arr)
print(arr, [11, 12, 22, 25, 34, 64, 90])