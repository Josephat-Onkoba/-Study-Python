
#creating a grading system using python if..elif condition
Unit1 = float(input("Enter your score in Distributed Systems : "))
Unit2 =  float(input("Enter your score in Python : "))
Unit3 =  float(input("Enter your score in Telecommunications : "))
totalScore = Unit1+Unit2+Unit3
average = totalScore/3
if(average >=70 and average <=100):
    print("Grade ", "A")
elif(average>=60 and average<=69):
    print("Grade", "B")
elif(average>=50 and average<=59):
    print("Grade ", "C")
elif(average>=40 and average<=49):
    print("Grade ", " D")
elif(average<=39):
    print("Grade ", "Fail")  


