# Function which check inputs and calculate income and salary after 10% tax
def income(hour, per_hour): 
    if hour > 8: 
        print('Error, Too much work!')
    elif per_hour < 15: 
        print('Error, Your income is very low!')
    else: 
        total_income = (hour * per_hour) * 20 
        disposable_income = total_income - total_income * 0.1 
        salary = disposable_income * 12 
        print('Your monthly income is: %i after 10 percent tax' %disposable_income) 
        print('Your salary is: %i Dollars after 10 percent tax' %salary) 

# Driver code
h = int(input('How many hour you are working per day? '))
p = int(input('How much you earn per hour? '))

income(h , p)

input("Press enter to exit ;)")