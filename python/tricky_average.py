def tricky_average(arr):
    odds = []
    even = []

    for i in arr:
        if i%2 == 0:
            odds.append(i)

        if i%2 != 0:
            even.append(i)

    return (max(odds)+min(even)) / 2

print(tricky_average([1,2,3]))
print(tricky_average([3, 4, 5, 6]))
print(tricky_average([5,2,8,-1]))