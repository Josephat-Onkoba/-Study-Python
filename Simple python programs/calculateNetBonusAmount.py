'''Exercise
A company decided to give bonus to employee according to following
criteria:
Time period of Service
Bonus
More than 10 years
10%
>=6 and <=10
8%
Less than 6 years
5%
Ask user for their salary and years of service and print the net
bonus amount.'''

salary = float(input("Enter salary per month: "))
yearsOfService = int(input("Time period of service: "))
annualSalary = salary*12

if(yearsOfService>10):
    print("Total net bonus Amount in ",yearsOfService,"years of service = ",(annualSalary*0.1)*yearsOfService)
elif(yearsOfService>=6 and yearsOfService<=10):
    print(" Total net bonus Amount in ", yearsOfService,"years of service = ",(annualSalary*0.08)*yearsOfService )
elif (yearsOfService<6):
    print(" Total net bonus Amount in ", yearsOfService,"years of service = ",(annualSalary*0.05)*yearsOfService)