#python program to dispaly file avialiable in current directory

import os
#get current working directory
current_directory = os.getcwd()
print(f"Current Directory :{current_directory}")

#List all files in the current directory
files = [ f for f in os.listdir(current_directory) if os.path.isfile(f)]
print("Files in current directory: ")
for file in files:
    print(file)