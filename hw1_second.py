print("Общество в начале XXI века")
age = int(input("Enter your age:"))
if 0<age<=7:
	print("Вам в детский сад")
elif 7<age<=18:
	print("Вам в школу")
elif 18<age<=25:
	print("Вам в профессиональное учебное заведение")
elif 25<age<=60:
	print('Вам на работу')
elif 60<age<=120:
	print("Вам предоставляется выбор")
elif age<0 or age>120:
	print("Эта программа для людей!\n"*5)
