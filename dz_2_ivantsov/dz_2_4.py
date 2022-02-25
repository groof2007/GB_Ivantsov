my_list = [57.8, 46.51, 97, 13.65, 90, 87.65, 98.54, 100.1, 32.43, 9]
my_list.sort()
for i in my_list:
    rr = int(i)
    kk = (i - int(i)) * 100
    print(f'{rr} руб. {kk:02.0f} коп.')

