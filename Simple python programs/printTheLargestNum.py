# program to print the largest of three numbers
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
num3 = float(input("Enter the third Number: "))

if (num1>num2 and num1>num3):
    print(num1)
elif(num2>num1 and num2>num3):
    print(num2)
else:
    print(num3)
