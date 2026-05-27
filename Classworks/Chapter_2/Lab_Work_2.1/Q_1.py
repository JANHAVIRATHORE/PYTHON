'''Write a Python Program to:
  -Take a number as input from the user.
  -Use an 'if-else' statement to check if the number is even or odd and 
   print the result.'''

print("\nLet's find number is even/odd\n");
num=int(input("Enter Any number:"));
if num%2==0:
    print("your number",num,"is even number.");
else:
    print("your number",num,"is odd number.\n");