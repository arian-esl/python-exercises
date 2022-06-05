# This programme will get Hour and Rate per hour from user 
# and calculate Monthly income and salary after 10 percent tax 

def income(hour, per_hour): # Calculator function
    if hour > 8: # Check for standard working hour
        print('Error, Too much work!')
    elif per_hour < 15: # Check for standard rate per hour 
        print('Error, Your income is very low!')
    else: # Calculate income and salary if hour and rate were standard 
        total_income = (hour * per_hour) * 20 # Calculate total income for 20 days (standard working days)
        disposable_income = total_income - total_income * 0.1 # Calculate disposable income (10% tax)
        salary = disposable_income * 12 # Calculate salary
        print('Your monthly income is: %i after 10 percent tax' %disposable_income) # Print monthly income
        print('Your salary is: %i Dollars after 10 percent tax' %salary) # Print salary

# Get input from user 
h = int(input('How many hour you are working per day? '))
p = int(input('How much you earn per hour? '))

# Calculator function apply on inputs
income(h , p)

# This is for keep running python file in windows OS
input("Press enter to exit ;)")