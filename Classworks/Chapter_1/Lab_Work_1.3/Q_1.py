'''Write a python program to demonstrate the use of type casting
   constructors (int(),float(),str(),bool()):
  -Take input from the user as a string.
  -Convert the string into an integers,a float, and a boolean.
  -Print the converted values along with their types.'''

print("\nConvert the string into different data types!\n");
user=input("Enter Anything String:");
print("you entered:",user,type(user));
user1=int(user);
print(user1,type(user1));
user2=float(user);
print(user2,type(user2));
user3=bool(user);
print(user3,type(user3));