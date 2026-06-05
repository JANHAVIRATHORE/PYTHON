'''Write a python Program using a 'Switch-Case' equivalent to:
  -Take an Operator(+,-,*,/) as input.
  -Perform the corresponding operation on two numbers entered by the user.'''

print("\nLet's Perform Arithmetic Operation with Operator's!\n");
num1=int(input("Enter a number:"));
num2=int(input("Enter a number:"));
operator=input("Enter an operator(+,-,*,/,%,**,//):");

match operator:
    case '+':
        print("Addition of",num1,"and",num2,"is:",num1+num2);
    case '-':
        print("Subtraction of",num1,"and",num2,"is:",num1-num2);
    case '*':
        print("Multiplication of",num1,"and",num2,"is:",num1*num2);
    case '/':
        print("Division of",num1,"and",num2,"is:",num1/num2);
    case '/':
        print("Modulus of",num1,"and",num2,"is:",num1%num2);
    case '**':
        print("Exponentiation of",num1,"and",num2,"is:",num1**num2);
    case '//':
        print("Floor Division of",num1,"and",num2,"is:",num1//num2);
    case _:
        print("Invalid Operator!");
