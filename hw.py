#Задание №1
from datetime import date, time, datetime, timedelta
k = datetime.strptime("19901204", "%Y%m%d")
print(k)
#Задание №3
date = "24.02.2001 17:05:00"
p = datetime.strptime("24.02.2001 17:05:00", "%d.%m.%Y %H:%M:%S")
print(p)
print(type(p))
#Задание №4
day = int(input("Введите количество дней: "))
amount = date.fromordinal(day)
#Задание #7
