# # Task 1 Complete the function to return the current working directory

# import os


# Complete the function to return the current working directory
# def getCurrentDirectory():
#     current_dirc = os.getcwd()
#     return current_dirc
#
#
# # expected output: /tmp
# # if using PyFiddle.io otherwise it varies
# print(getCurrentDirectory())
#
# # Task 2 Complete the function to return the directory name only from the given file name
# #
# import os
#
#
# # Complete the function to return the directory name only from the given file name
# def getDirectoryName(fileName):
#     return os.path.dirname(fileName)
#
#
# # Student code goes here
#
# # expected output: /var/www
# print(getDirectoryName("/var/www/test.html"))
#
# # expected output: /var/www/apple
# print(getDirectoryName("/var/www/apple/test.html"))
# #
# # Task 3 Complete the function to return the file name part only from the given file name
# #
# import os
#
#
# # Complete the function to return the file name part only from the given file name
# def getFileName(fileName):
#     return os.path.basename(fileName)
#
# # Student code goes here
#
# # expected output: test.html
# print(getFileName("/var/www/test.html"))
#
# # expected output: names.txt
# print(getFileName("/var/www/apple/names.txt"))
# #
# # Task 4 Complete the function to create the specified file from the given file name
#
# import os
#
#
# # Complete the function to create the specified file and return the file name
# def createFile(filename):
#     with open(filename, 'w') as file:
#         pass
#     return os.path.basename(filename)
#
# # expected output: True
# createFile("test.txt")
# print(os.path.exists("test.txt"))
#

# # Task 5 Complete the function to print all files in the given directory
#
# import os
#
#
# # Complete the function to print all files in the given directory
# def printFiles(someDirectory):
#     files = os.listdir(someDirectory)
#
#     for file in files:
#         file_path = os.path.join(someDirectory, file)
#         if os.path.isfile(file_path):  # Check if it's a file (not a directory)
#             print(file_path)
#
# # expected output: main.py
# # if using PyFiddle.io otherwise it varies
# printFiles(os.getcwd())
# #
# # Task 6 Complete the function to return FILE if the given path is a file or return DIRECTORY if the given path is a directory or return NEITHER is it 's not a file or directory
#
# import os
#
#
# # Complete the function to return FILE if the given path is a file
# # or return DIRECTORY if the given path is a directory
# # or return NEITHER is it's not a file or directory
# def whatIsIt(somePath):
#     if os.path.isfile(somePath):
#         return "FILE"
#     elif os.path.isdir(somePath):
#         return "DIRECTORY"
#     else:
#         return "NEITHER"
# # Student code goes here
#
#
# # expected output: DIRECTORY
# print(whatIsIt(os.getcwd()))
#
# # expected output: FILE
# print(whatIsIt(os.listdir(os.getcwd())[0]))
#
# # expected output: NEITHER
# print(whatIsIt('apple.pie.123.txt'))
# #
# # Task 7 Complete the function to read the contents of the specified file and print the contents
#
# import os
#
#
# # Complete the function to read the contents of the specified file and print the contents
# def printFileContents(filename):
#     with open(filename, 'r') as file:
#         file_contents = file.read()
#         print(file_contents)
#
#
# # expected output: Hello
# with open("test.txt", 'w') as f:
#     f.write("Hello")
# printFileContents("test.txt")
#
# # Task 8 Complete the function to append the given new data to the specified file then print the contents of the file
#
# import os
#
#
# # Complete the function to append the given new data to the specified file then print the contents of the file
# def appendAndPrint(filename, newData):
#     with open(filename, 'a') as file:
#         file.write(newData + '\n')
#
#     # Read and print the updated contents of the file
#     with open(filename, 'r') as file:
#         file_contents = file.read()
#         print(file_contents)
#
#
# # Student code goes here
#
# # expected output: Hello World
# with open("test.txt", 'w') as f:
#     f.write("Hello ")
# appendAndPrint("test.txt", "World")
