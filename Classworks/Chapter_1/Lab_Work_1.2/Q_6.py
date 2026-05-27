'''Implement a program to demonstrate logical operators(and,or,not) by asking
   the user for boolean inputs(e.g.,true/false values).'''

print("\nAnswer only in True or False!\n");

first=input("Enter first value:");
second=input("Enter second value:");
first = first.lower() == "true"
second = second.lower() == "true"

print("\nResults:")
print("AND Operator (a and b):", first and second)
print("OR Operator (a or b):", first or second)
print("NOT Operator (not a):", not first)
print("NOT Operator (not b):", not second)