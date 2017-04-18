def first(x):
	if x>=1 and x<=3:
		s = input("Enter some string:")
        n = int(input("Enter the number of iterations:"))
        for i in range(1,n+1):
            print(s)
	elif x>=4 and x<=6:
		power = int(input("Enter the power of your number:"))
        print(x**power)
	elif x in range(7,10):
		for x in range(x,x+x,1):
            print(x)
            x += 1
    else:
    	print("Error!")
