def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []

    for i in range(a,b+1):
        string_num = f"{i}"
        string_num_length = len(string_num)
        if string_num_length == 1:
            result.append(i)
        else:
            temp_values = []
            valid = False
            for j in range(0,string_num_length):
                temp_values.append(int(string_num[j])**(j+1))
            if i == sum(temp_values):
                result.append(i)
    return result

print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89),  [89])
print(sum_dig_pow(10, 100),  [89])
print(sum_dig_pow(90, 100), [])
print(sum_dig_pow(89, 135), [89, 135])