my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(my_list)):
    if my_list[i].isdigit():
        my_list[i] = (f'"{int(my_list[i]):02}"')
    elif my_list[i].startswith('+' or '-') and my_list[i][1:].isdigit():
        my_list[i] = (f'"{int(my_list[i]):02}"')

message = ' '.join(f'{i}' for i in my_list)
print(message)