# created a Welcome message and asked user for input on hours worked
print('Welcome to my Python Program!')
hour = input("How many hours did you work this week?")
# Converted input to float and calculated monthly hours
hours = float(hour)
monthly_hours = hours * 4
# Printed out the total monthly hours that the user is on track to work
print(f' You are on track to work {monthly_hours} hours this month!')
# Created a simple error handling if a valid number is not entered
 try:
    hours = float
except ValueError:
    print("Please enter a valid number")
    exit()