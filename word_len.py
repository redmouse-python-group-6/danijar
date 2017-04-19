x = input("Enter some string:\n")
def word(x):
	global x
    for i in x.split( ) :
        return(i,"- {}".format(len(i)) )
print(word(x))