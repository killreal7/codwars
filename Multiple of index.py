def multiple_of_index(arr):
    res = []; i = 0
    for elem in arr:
        if i > 0 and elem % i == 0:
            res.append(elem)
        i += 1
    return res