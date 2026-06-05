'''Write a program that:
  -Use a 'for' loop and 'range()' to iterate through numbers from 1 to 50.
  -Check if each number is divisible by 2, 3 or both using nested if-elif-else.
  -Print messages for each case: "is divisible by 2", "is divisible by 3", "is divisible by both", or "Not divisible!" accordingly.'''
for i in range(1,50+1):
    if i%2==0:
        if i%3==0:
            print(i,"is divisible by both.");
        else:    
            print(i,"is divisible by 2.");
    elif i%3==0:
        print(i,"is divisible by 3.")
    else:
        print(i,"Not divisible!")