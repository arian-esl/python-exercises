# This program takes input until you enter the number -1 and calculates the average of the entered numbers
x = int(input('Enter an integer:'))
count = 0
sum = 0
while x != -1:
    count += 1 
    sum = sum + x 
    x = int(input('Enter another integer:'))
    if x == -1: 
        count += 1 
        sum = sum + x
        break
    
mean = sum / count
print('The average numbers entered is', mean)
