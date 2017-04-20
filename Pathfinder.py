import os,datetime
path = input("Enter the path of your folder:\n")
obj = input("Enter the name of your file:\n")
if os.path.exists(path):
    files = os.listdir(path)
    if obj in files:
    	print("File directory: ",path)
    	print('File size: ',os.stat(obj).st_size)
    	time = os.stat(obj).st_ctime
    	print('File created: ',datetime.datetime.fromtimestamp(time))
    	modtime = os.stat(obj).st_mtime
    	print('Last modified: ',datetime.datetime.fromtimestamp(time)) 
else:
	print("There is no such a directory!")

