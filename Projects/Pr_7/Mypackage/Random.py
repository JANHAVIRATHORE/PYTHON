import random

if __name__=="__main__":
    pass

class number:
    def __init__(self,num1,num2):
        self.start=num1;
        self.last=num2;
        print(f"\nRandom Number between {self.start} to {self.last}: {random.randint(self.start,self.last)}");
        print("="*50,"\n");

class List:
    def __init__(self,num):
        self.lst=num;
        print(f"Random List value: {random.choice(self.lst)}");
        print("="*50,"\n");

class password:
    def __init__(self,length):
        self.length=length;
        char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*";
        print("\nGenerated Password:",end="");
        for i in range(length):
            print(random.choice(char),end="");

class otp:
    def __init__(self):
        print(f"\nGenerated OTP:",end="");
        for i in range(0,6):
            print(random.randint(0,9),end="");

def main():
    print("\nRandom Data Generation:");
    while True:
        print("\n1.Generate Random Number");
        print("2.Generate Random List");
        print("3.Create Random Password");
        print("4.Generate Random OTP");
        print("5.Back to Main Menu");

        choice=int(input("\nEnter Your Choice:"));

        if choice==1:
            num1=int(input("\nEnter First number:"));
            num2=int(input("Enter Last number:"));
            num_obj=number(num1,num2);

        elif choice==2:
            num=[int(i) for i in input("Enter number (comma-separated):").split(",")];
            list_obj=List(num);

        elif choice==3:
            length=int(input("\nEnter Length of Password: "));
            pass_obj=password(length);
            print();
            print("="*50,"\n");

        elif choice==4:
            otp_obj=otp();
            print();
            print("="*50,"\n");

        elif choice==5:
            print("="*50,"\n");
            break;

        else:
            print("Invalid choice!!");