x = input("Enter some string to know the longest word")
xspl = x.split(";")
count = 0
for i in xspl:
	if len(i)>count:
		count = len(i)
		word = i
print('The longest word is ',word)