#!/usr/bin/env python3
#Reading files using python

# i)
file = open("Document.rtf")

print(file.readline())  #This will print a single line from the start of the file

print(file.read()) #This will print the wole contents of your file from the start of your single line

file.close() # This script will close your file

# ii) using the WITH block

with open("Document.rtf") as file:
    print(file.read())
# When using a with block python will automatically close the file. You will not need the .close() function
