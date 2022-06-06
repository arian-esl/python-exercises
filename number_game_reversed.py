# The computer will guess a number between 1 and 99 until it reaches the user's
import random

javab = int(input("Enter javab:"))

hads = random.randint(1, 100)

print("Hads is", hads)

question = input("Is hads bigger or smaller?")

while javab != hads: 
    if question == "bigger":
        hads -= 1
    else:
        hads += 1

print("Hads is", hads)

input("Press enter to exit ;)")


    

    


    