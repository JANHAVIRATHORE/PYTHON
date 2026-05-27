'''Write a program using a 'while' loop to:
  -Take numbers as input from the user until they enter '0'.'''

print("\nLet's enter the number loop!\n");
while True:
    print("\nEnter 0 to exit the loop.");
    num=int(input("Enter Number:"));
    if num!=0:
        print("\nYour enter number is",num);
    else:
        print("\nYou enter 0\nThank you!");
        break;
