# This code sort 10 given names in the standard format 
x = []

for i in range(1, 11):
    name = input("Enter a name:")
    name = name.lower()
    name = name.title()
    x.append(name)

for n in x:
    print(n)
