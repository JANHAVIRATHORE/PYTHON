'''Create a program that:
  -Declares two variables with the same value.
  -Prints their memory addresses using id() and checks if
   they are the same.
  -Modifies one of the variables and checks the memory 
   addresses again.'''

print("\n****\n");
var1=123;
var2=123;
print("\nMemory Address of variable 1:",id(var1),"Memory Address of variable 2:",id(var2));

var1=456;
print("\nMemory Address after value change:",id(var1),"Memory Address same as previous",id(var2));
