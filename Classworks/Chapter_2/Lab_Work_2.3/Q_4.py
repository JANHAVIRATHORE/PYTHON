'''Write a program to:
  -Use a 'range()' function to generate a sequence of
   numbers from 1 to 20.
  -Print only the odd numbers using a 'for' loop.'''

print("\nLet's print odd number in between 1 to 20!")
for i in range(1,20+1):
    if i%2==1:
        print(i,"is odd number.\n");
    