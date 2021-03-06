import os
import datetime
os.remove('test.txt')# to remove file
os.path.exists('test.txt')#ro check path
os.rename('test.txt', 'hello.py')#rename file
os.path.getsize('test.txt')#get file size
timestamp = os.path.getmtime('test.txt')#get time in seconds since unix was created
datetime.datetime.fromtimestamp(timestamp).date().fromtimestamp()#to get timestamp when the file created
os.isfile('test.txt')#true if file exists, false otherwise
os.path.abspath('test.txt')#get the absolute path from the disk

print(os.getcwd())#ger the path of the directory of this file
os.mkdir('/motasem')#create directory with relative path or absolute like C:\users\...
os.chdir('new_dir')#relative or absolute, change current working directory
os.rmdir('dir_name')#remove directory
os.listdir()#relative or absolute
os.path.join('dir_path', 'dir_or_file_path')#relative or absolute, good for cross platforms id relative

parent = os.path.join(os.getcwd(), os.pardir)# go up to parent directory