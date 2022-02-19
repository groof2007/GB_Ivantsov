procent = [i for i in range(1, 101)]
nums = (11, 12, 13, 14)
for i in procent:
    if i in nums:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 > 1 and i % 10 < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
