duration = 4153

days = duration // 86400

days_tail = duration % 86400
hour = days_tail // 3600

hour_tail = (duration % 3600)
min = hour_tail // 60

sec = hour_tail % 60

print(' в вашем числе ', days, 'дн', hour, 'час', min, 'мин и', sec, 'сек')