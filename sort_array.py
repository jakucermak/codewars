def sort_array(source_array):

    for i in range(0, len(source_array)):
            for j in range(0,len(source_array)):
                if source_array[j] %2 !=0 and source_array[i] %2 !=0 and source_array[i] < source_array[j]:
                    source_array[i], source_array[j] = source_array[j], source_array[i]
    return source_array
print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))