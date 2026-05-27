'''Write a Program where the user inputs a floating-point number.
  -Convert this number into an integer using int() and print
   both values with a message explaining the difference.'''

print("\nLet's convert float to int!\n");
user=float(input("Enter any float number:"));
print("\nYou enter a floating value:",user,"of data type",type(user));
user1=int(user);

print("\nYou enter value is than converted into integer type:",user1,",of data type",type(user1),"due to which it looses its precision value and converted into floor division.");