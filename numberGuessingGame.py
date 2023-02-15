# Number Guessing Game 
winning_number =int(input("GUESS A NUMBER BETWEEN 0 & 10 :  "))
if(winning_number==5):
    print("YOU WIN!!!")
elif(winning_number<5):
    print("Too low")
elif(winning_number>5):
    print("Too High")

