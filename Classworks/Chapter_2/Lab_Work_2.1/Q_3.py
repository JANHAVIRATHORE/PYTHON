'''Implement a program that:
  -Takes three integers as input.
  -Uses an 'if-elif-else' statements to find and print the largest number.'''

print("\nLet's find largest number of the three number!\n");
num1=int(input("Enter a number:"));
num2=int(input("Enter a number:"));
num3=int(input("Enter a number:"));

if num1>num2 and num1>num3:
    print("The largest number is:",num1);
elif num2>num1 and num2>num3:
    print("The largest number is:",num2);
elif num3>num1 and num3>num2:
    print("The largest number is:",num3);
else:
    print("All the number are same.");