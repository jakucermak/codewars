def union(arr1,arr2):
    return list(set(arr1+arr2))

print(union([1, 2, 3], [2, 3, 4]))
print(union([1,2],[3,4]))
print(union([],[]))
