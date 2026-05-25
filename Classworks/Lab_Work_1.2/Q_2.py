'''Create a program that asks the user for their name,age,and favourite hobby using the input()
   function,then displays a formatted message like:
   -"Hello, <name>! At <age>,enjoying <hobby> sounds fun!"'''

name=input("Enter your name:");
age=int(input("Enter your age:"));
hobby=input("Enter your hobby:");

print("\n-"," Hello, ",name,"! At ",age," enjoying ",hobby," sounds fun!",sep="");