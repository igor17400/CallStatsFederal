
# use ipython magic command %%writefile to create a python script file and write below script content to it.
# import two python standard module. 
import sys
import os

# set dir_name value to current directory by default.
dir_name = '.'

# if user input an argument.
if len(sys.argv) > 1:
    # give the first argument value to a local variable, the argument value should be a directory name.
    dir_name = sys.argv[1]

    
# get all the dir_name directory contained files in a list
files_list = os.listdir(dir_name)
    
# loop in the files_list.
for file in files_list:
    # print out file name in the standard output.
    print(file)
