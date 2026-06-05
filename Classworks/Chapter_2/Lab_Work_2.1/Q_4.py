'''Write a python program to:
  -Take a number as input from the user and check whether it is neutral
   number or not using a ladder if statement.'''

print("\nLet's find the neutral number!\n");
num=int(input("Enter a number"));

if num>0:
    print("Your number is positive.");
elif num<0:
    print("your number is negative.");
else:
    print("It is a neutral number.");