import math

if __name__=="__main__":
    pass

def main():
    print("\nMathematical Operations:");
    while True:
        print("1.Calculate Factorial");
        print("2.Solve Compound Interest");
        print("3.Trigonometric Calculations");
        print("4.Area of Geometric Shapes");
        print("5.Back to Main Menu");

        try:
            choice=int(input("\nEnter Your Choice:"));

            if choice==1:
                num=int(input("\nEnter a number:"));
                print(f"Factorial:{math.factorial(num)}");
                print("="*50,"\n");

            elif choice==2:
                amount=int(input("\nEnter Principle amount: "));
                rate=int(input("Enter rate of interest (in %): "));
                time=int(input("Enter Time (in years): "));
                compound_interest=amount*math.pow((1+rate/100),time);
                print(f"Compound Interest: {compound_interest}");
                print("="*50,"\n");

            elif choice==3:    
             while True:
                print("\nTrigonometric Calculator");
                print("1.Sine");
                print("2.Cosine");
                print("3.Tangent");
                print("4.Exit");

                choice=int(input("\nEnter your choice: "));
                
                if choice==1:
                    angle=float(input("\nEnter angle (in degrees): "))
                    radian=math.radians(angle)
                    print(f"sin({angle})= {math.sin(radian):.4f}");

                elif choice==2:
                    angle=float(input("\nEnter angle (in degrees): "))
                    radian=math.radians(angle)
                    print(f"cos({angle})= {math.cos(radian):.4f}");

                elif choice==3:
                    angle=float(input("\nEnter angle (in degrees): "))
                    radian=math.radians(angle)
                    print(f"tan({angle})= {math.tan(radian):.4f}");

                elif choice==4:
                    break;

                else:
                    print("Invalid Choice!");

                print("="*50,"\n");

            elif choice==4:
             while True:
                print("\nArea of Geometric Shapes");
                print("1.Circle");
                print("2.Rectangle");
                print("3.Square");
                print("4.Triangle");
                print("5.Exit");

                choice=int(input("Enter your choice: "));

                if choice==1:
                    radius=float(input("Enter the radius: "));
                    area=math.pi*radius**2;
                    print(f"Area of Circle: {area:.2f}");

                elif choice==2:
                    length=float(input("Enter the length: "));
                    breadth=float(input("Enter the breadth: "));
                    area=length*breadth;
                    print(f"Area of Rectangle: {area:.2f}");

                elif choice==3:
                    side=float(input("Enter the side: "));
                    area=side**2;
                    print(f"Area of Square: {area:.2f}");

                elif choice==4:
                    base=float(input("Enter the base: "));
                    height=float(input("Enter the height: "));
                    area=0.5*base*height;
                    print(f"Area of Triangle: {area:.2f}");

                elif choice==5:
                    break;
                
                else:
                    print("Invalid Choice!");

                print("="*50,"\n");

            elif choice==5:
                print("="*50,"\n");
                break;

        except ValueError:
            print("\nInvalid Option! Please select a valid option from the menu.\n");
            print("="*50);