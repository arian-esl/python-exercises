# The user will guess a number between 0 and 99 until the computer's random number find
import random

javab = random.randint(0, 100)

hads = int(input("What is your hads?"))

while hads != javab:
    if hads > javab:
        print("Mine is smaller!")
    else:
        print("Mine is bigger!")
    hads = int(input("What is your hads?"))

print("Wooooow you did it ...!, hads is %i" %hads)

input("Press enter to exit ;)")
