#This code sort the input from low to high
#Input: 1+2+3+3+2+1+2+2+3+2+1
#Output: 1+1+1+2+2+2+2+2+3+3+3
 
txt = input("Seri adad ra vared konid:")

result = txt.split('+')

result.sort()

result = "+".join(result)

print(result)