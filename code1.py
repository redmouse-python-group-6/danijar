x = int(input("Enter an integer from 1 to 9:"))
if 1<=x<=3:
    s = input("Enter some string:")
    n = int(input("Enter the number of iterations:"))
    for i in range(1,n+1):
        print(s)
elif 4<=x<=6:
    m = int(input("Enter the power of your number:"))
    print(x**m)
elif 7<=x<=9:
    for x in range(x,x+x,1):
        print(x)
        x += 1
else:
    print("Error")
