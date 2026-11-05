import os

PATH = r'c:\users\clcoding \Downloads'

files = 0
dirs = 0

for root ,dirnames,filenames in  os.walk(PATH):
    dirs += len(dirnames)
    files += len(filenames)

    print('Files:',files)
    print('Directories:',dirs)
    print('Total:',files + dirs)