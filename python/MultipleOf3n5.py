def solution(number):
    result = []
    
    for n in range(1,number):
        if n % 3 == 0 or n % 5 == 0:
            if result.count(n) == 0:
                result.append(n)
    return sum(result)

print(solution(4))
