def hanoi(disks):

    if disks == 1:
        return 1
    return hanoi(disks-1) + hanoi(disks-1)+1


print(hanoi(1), 1)
print(hanoi(2), 3)
print(hanoi(3), 7)
print(hanoi(5), 31)
print(hanoi(10), 1023)
print(hanoi(20), 1048575)