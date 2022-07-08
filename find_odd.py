def find_it(seq):
    
    for n in set(seq):
        if seq.count(n) % 2 != 0:
            return n
    

print(find_it([7]))
print(find_it([0]))
print(find_it([1,1,2]))
print(find_it([0,1,0,1,0]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
