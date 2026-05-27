'''Create a program that:
  -Accepts a user's age as input.
  -Use nested 'if-else' statement to categorize the user into age groups:
         -Child(0-12)
         -Teenager(13-19)
         -Adult(20-59)
         -Senior(60+).'''

print("\nLet's find the user eligibility \n");
age=int(input("Enter your age:"));

if age<=12:
    print("User is a child.");
elif age>=13 and age<=19:
    print("user is a teenager.");
elif age>=20 and age<=59:
    print("user is an adult.");
else:
    print("user is a senior.");