#!/usr/bin/env python3

# i) Making a whole line uppercase
with open("Document.rtf") as file:
    for line in file:
        print(line.upper())

# ii) Removing white spaces including tabs and new lines
with open("Document.rtf") as file:
    for line in file:
        print(line.strip().upper())

# iii) Reading the files into a list
file = open("Document1.rtf")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
