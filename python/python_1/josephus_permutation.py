'''
josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

'''

def josephus_survivor(n:list,k):
    arr = [x for x in range(1,n+1)]
    l = len(arr)
    c = 0
    i = 0
    j = 0
    while l > 1:
        if j == l and c != 3:
            i = 0
            j = 0
        if c == 3:

            arr.pop(i-1)
            l = len(arr)
            c = 0
        else:
            c += 1
            j += 1
            i += 1
    return arr




print(josephus_survivor(7,3),4)
print(josephus_survivor(11,19),10)
print(josephus_survivor(1,300),1)
print(josephus_survivor(14,2),13)
print(josephus_survivor(100,1),100)