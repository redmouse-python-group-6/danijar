import os,time
import os.path
path = input("Enter the path of your folder:\n")
obj = input("Enter the name of your file:\n")
while os.path.exists(path):
    files = os.listdir(path)
    if obj in files:
    	print("File directory: ",path)
    	print(os.path.getsize(obj))
    	print("File created:", time.asctime(time.localtime))
else:
	print("There is no such a directory!")

