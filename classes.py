# -- coding: utf-8 --
from package import module1
class Homework:
	def __init__(self,x):
		self.x = x
		if 1<=x<=3:
			module1.one_three(x)
		elif 4<=x<=6:
			module1.four_six(x)
		elif 7<=x<=9:
			module1.seven_nine(x)
		else:
			print("Incorrect number")
number = Homework()
number = int(input('Enter the number from 1 to 9'))

