print("Общество в начале XXI века")
age = int(input("Enter your age:"))
if age>0 and age<8:
	print("Вам в детский сад")
elif age>7 and age<19:
	print("Вам в школу")
elif age>18 and age<26:
	print("Вам в профессиональное учебное заведение")
elif age>25 and age<=60:
	print('Вам на работу')
elif age>=60 and age<=120:
	print("Вам предоставляется выбор")
elif age<0 or age>120:
	print("Эта программа для людей!\n"*5)