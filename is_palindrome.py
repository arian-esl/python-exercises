# Function which return reverse of a string
def is_palindrome(x):
    return x == x[::-1]

# Driver code
s = input("Enter a string: ")

ans = is_palindrome(s)
if ans:
    print("palindrome")
else: 
    print("not palindrome")

input("Press Enter to exit")