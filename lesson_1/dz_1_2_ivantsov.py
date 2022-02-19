my_list = [i**3 for i in range(1, 1001, 2)]
new_my_list = []
for i in my_list:
    result = 0
    a = i
    while a > 0:
        digit = a % 10
        result = result + digit
        a = a // 10
    if result % 7 == 0:
        new_my_list.append(i)

print(sum(new_my_list))

new_my_list_2 = []
for i in my_list:
    result = 0
    a = i + 17
    while a > 0:
        digit = a % 10
        result = result + digit
        a = a // 10
    if result % 7 == 0:
        new_my_list_2.append(i+17)

print(sum(new_my_list_2))