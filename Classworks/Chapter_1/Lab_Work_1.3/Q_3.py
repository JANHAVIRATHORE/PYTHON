'''Create a Program that:
  -Takes a boolean value(True or False) as input.
  -Converts the boolean to an integers and a string, and 
   prints all three values.'''

print("\nConvert bool value into int!\n");
user=bool(input("Enter only boolean value(True/False(empty)):"));
print("\nyou entered:",user,type(user));

user1=int(user);
print("\nvalue after converting to integer:",user1,type(user1));

user2=str(user);
print("\nvalue after converting to integer:",user2,type(user2));