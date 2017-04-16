x = input("Enter some string to know the shortest word:\n")
xspl = x.split( )
print("The shortest word is: ",min(xspl,key = len))