print("CREATE YOUR ACCOUNT BELOW ")
Username = input("Enter Username: ")
Password = input("Enter Password: ") 
confirmPassword = input("Confirm your Password: ")

if(Password == confirmPassword):
    print("Acoount created successfully, login below.")
else:
    print("Passwords do not match")
    exit()
print("LOGIN HERE:")
Username1 = input("Enter your Username:")
Password1 = input("Enter Password: ")
if(Username1==Username and Password1==Password):
    print("Login successfull")
else:
    print("Invalid Credentials")

