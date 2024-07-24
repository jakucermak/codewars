def high_and_low(numbers):
    nums = numbers.split()
    result = ""
    
    for n in range(0, len(nums)):
        nums[n] = int(nums[n])

    nums.sort(reverse=True)
    return '{} {}'.format(nums[0], nums[len(nums)-1])

print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"