'''Write a program in python to find the minimum number from the given three
   numbers using a nested if statements.'''

print("\nLet's Find the minimum number from Three values!\n");
num1=int(input("Enter a number:"));
num2=int(input("Enter a number:"));
num3=int(input("Enter a number:"));

if num1<num2 and num1<num3:
    print("The minimum number is:",num1);
elif num2<num1 and num2<num3:
    print("The minimum number is:",num2);
elif num3<num1 and num3<num2:
    print("The minimum number is:",num3);
else:
    print("All the number are same.");