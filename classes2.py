from package import module2
class Society:
	def __init__(self,age):
		self.age = age
		if 0 <= self.age <= 6:
			zero_six()
		elif 7 <= self.age <= 17:
			seven_nineteen()
		elif 18 <= self.age <= 26:
			eighteen_twentysix()
		elif 27 <= self.age <=60:
			twentyfive_sixty()
		elif 61 <= self.age <= 120:
			sixty_hundredtwenty()
		elif 0 < self.age >120:
			zero_hundredtwenty()

print("Общество в начале XXI века")
k = Society(int(input("Введите возраст:\n")))

