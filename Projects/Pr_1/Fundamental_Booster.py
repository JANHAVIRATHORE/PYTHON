print("Welcome to the Interactive Personal Data Collector!\n");
name=input("please enter your name:");
age=int(input("please enter your age:"));
height=float(input("please enter your height in meters:"));
no=int(input("please enter your favourite number:"));

print("\nThank you! Here is the Information we collected:");

print("\nName:",name,"(Type:",type(name),",Memory Addresss:",id(name),")");
print("Age:",age,"(Type:",type(age),",Memory Addresss:",id(age),")");
print("Height:",height,"(Type:",type(height),",Memory Addresss:",id(height),")");
print("Favourite Number:",no,"(Type:",type(no),",Memory Addresss:",id(no),")");

date=int(input("\nEnter Current year (YYYY):"));
print("\nyour Birth year is approximately:",date-age,"Based on your year your age is",age);
print("\nThank you for using the personal Data Collector.\n","Goodbye!\n");