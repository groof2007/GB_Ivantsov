src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def num_check(src):
    result_unique = []
    for i in src:
        if i in result_unique:
            continue
        else:
            result_unique.append(i)
    return result_unique

print(num_check(src))