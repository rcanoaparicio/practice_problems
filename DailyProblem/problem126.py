def rotate(list, k):
    list += list[0:k]
    i = 0
    j = k
    while i < len(list) - k:
        list[i] = list[j]
        i += 1
        j += 1
    return list[:len(list)-k]


print(rotate([1, 2, 3, 4, 5, 6], 2))
