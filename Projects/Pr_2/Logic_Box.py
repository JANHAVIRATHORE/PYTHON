print("\n\nWelcome to the Pattern Generator and Number Analyzer!");
while True:
    print("\nSelect an option:");
    print(" 1.Generate a Pattern.");
    print(" 2.Analyze a Range of number.");
    print(" 3.Exit.");

    choice=int(input("\nEnter Your Choice:"));
    match choice:
        case 1:
         while True:
            print("\nSelect an option:");
            print("1.star Patters.");   
            print("2.Number Patters."); 
            print("3.Exit."); 

            choice=int(input("\nEnter Your Choice:"));
            match choice:
                case 1:
                 while True:
                    print("\nSelect an option:");
                    print("1.Square Patters.");   
                    print("2.Triangle Patters."); 
                    print("3.Exit."); 

                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                            col=int(input("\nEnter the Number of Columns for the pattern:"));
                            row=int(input("Enter the Number of rows for the pattern:"));
                            print("\nPattern:");
                            for i in range(1,row+1):
                                for j in range(1,col+1):
                                    print("*",end=" ");
                                print();
                        case 2:
                         while True:
                            print("\nSelect an option:");
                            print("1.Simple right angle Patters.");   
                            print("2.Inverted right angle Patters."); 
                            print("3.Mirrored Right-Angled Triangle.");
                            print("4.Mirror Inverted Right-Angled Triangle.");
                            print("5.Exit."); 

                            choice=int(input("\nEnter Your Choice:"));
                            match choice:
                                case 1:
                                    row=int(input("\nEnter the number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(0,i):
                                            print("*",end=" ");
                                        print();  
                                case 2:
                                    col=int(input("\nEnter the number of Columns for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(col,0,-1):
                                        for j in range(i,0,-1):
                                            print("*",end=" ");
                                        print();  
                                case 3:
                                    row=int(input("\nEnter the number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for k in range(row-i,0,-1):
                                            print(" ",end=" ")
                                        for j in range(0,i):
                                            print("*",end=" ");   
                                        print(); 
                                case 4:
                                    row=int(input("\nEnter the number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(row,0,-1):
                                        for k in range(row-i,0,-1):
                                            print(" ",end=" ")
                                        for j in range(0,i):
                                            print("*",end=" ");   
                                        print(); 
                                case 5:
                                    print("\nExiting to Main Menu.");   
                                    break;
                                case _:
                                    print("Invalid Choice");
                        case 3:
                            print("\nExiting to Main Menu.");   
                            break;
                        case _:     
                            print("Invalid Choice");    
                case 2:
                 while True:
                    print("\nSelect an option:");
                    print("1.Simple Patters.");   
                    print("2.Increasing number Patters."); 
                    print("3.Continues number Patters.");
                    print("4.Exit."); 

                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                         while True:
                            print("\nSelect an option:");
                            print("1.Square Patters.");
                            print("2.Simple right angle Patters.");   
                            print("3.Exit.");
                        
                            choice=int(input("\nEnter Your Choice:"));
                            match choice:
                                case 1:
                                    col=int(input("\nEnter the Number of Columns for the pattern:"));
                                    row=int(input("Enter the Number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(1,col+1):
                                            print(i,end=" ");
                                        print();
                                case 2:
                                    row=int(input("\nEnetr the number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(0,i):
                                            print(i,end=" ");
                                        print(); 
                                case 3:
                                    print("\nExiting to Main Menu.");   
                                    break;
                                case _:
                                    print("Invalid Choice");
                        case 2:
                         while True:
                            print("\nSelect an option:");
                            print("1.Square Patters.");
                            print("2.Simple right angle Patters.");   
                            print("3.Exit.");
                        
                            choice=int(input("\nEnter Your Choice:"));
                            match choice:
                                case 1:
                                    col=int(input("\nEnter the Number of Columns for the pattern:"));
                                    row=int(input("Enter the Number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(1,col+1):
                                            print(j,end=" ");
                                        print();
                                case 2:
                                    row=int(input("\nEnetr the number of rows for the pattern:"));
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(1,i+1):
                                            print(j,end=" ");
                                        print(); 
                                case 3:
                                    print("\nExiting to Main Menu.");   
                                    break;
                                case _:
                                    print("Invalid Choice");
                        case 3:
                         while True:
                            print("\nSelect an option:");
                            print("1.Square Patters.");
                            print("2.Simple right angle Patters.");   
                            print("3.Exit.");
                        
                            choice=int(input("\nEnter Your Choice:"));
                            match choice:
                                case 1:
                                    col=int(input("\nEnter the Number of Columns for the pattern:"));
                                    row=int(input("Enter the Number of rows for the pattern:"));
                                    num=1;
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(1,col+1):
                                            print(num,end=" ");
                                            num+=1;
                                        print();
                                case 2:
                                    row=int(input("\nEnetr the number of rows for the pattern:"));
                                    num=1;
                                    print("\nPattern:");
                                    for i in range(1,row+1):
                                        for j in range(1,i+1):
                                            print(num,end=" ");
                                            num+=1; 
                                        print();  
                                case 3:
                                    print("\nExiting to Main Menu.");   
                                    break;
                                case _:
                                    print("Invalid Choice");
                        case 4:
                            print("\nExiting to Main Menu.");   
                            break;
                        case _:
                            print("Invalid Choice");
                case 3:
                    print("\nExiting to Main Menu.");
                    break;
                case _:
                    print("Invalid Choice");
        case 2:
         while True:
            print("\nSelect an option:");
            print("1.Print Number.");
            print("2.Mathematic Operation.");
            print("3.Series Program.");
            print("4.Statistics on Range.");
            print("5.Exit.");

            choice=int(input("\nEnter Your Choice:"));
            match choice:
                case 1:
                 while True:
                    print("\nSelect an option for Print Number:");
                    print("1.Print Numbers 1 to N.");
                    print("2.Print Even Numbers.");
                    print("3.Print Odd Numbers.");
                    print("4.Print Reverse Numbers.");
                    print("5.Exit.")
                   
                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                            end=int(input("Enter the End of the range:"));
                            for i in range(1,end+1):
                                print(i,end="\n");
                        case 2:
                            start=int(input("\nEnter the Start of the range:"));
                            end=int(input("Enter the End of the range:"));
                            print("\nEven Number from the range are:");
                            for i in range(start,end+1):
                                if i%2==0:
                                    print(i,end="\n");
                        case 3:
                            start=int(input("\nEnter the Start of the range:"));
                            end=int(input("Enter the End of the range:"));
                            print("\nOdd Number from the range are:");
                            for i in range(start,end+1):
                                if i%2!=0:
                                    print(i,end="\n");
                        case 4:
                            start=int(input("\nEnter the Start of the range:"));
                            end=int(input("Enter the End of the range:"));
                            for i in range(end,start-1,-1):
                                print(i,end="\n");
                        case 5:
                            print("\nExiting to Main Menu.");
                            break;
                        case _:
                            print("Invalid Choice");
                case 2:
                 while True:
                    print("\nSelect an option for Mathematic Operation:");
                    print("1.Sum of range.");
                    print("2.Multiplication Table.");
                    print("3.Floor Division.");
                    print("4.Power of a Number.");
                    print("5.Exit.")
                   
                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                            start=int(input("Enter the Start of the range:"));
                            end=int(input("Enter the End of the range:"));
                            sum=0;
                            for i in range(start,end+1):
                                sum+=i;
                            print("Sum of all numbers from",start,"to",end,"is:",sum);
                        case 2:
                            num=int(input("Enter the Table number:"));
                            print("Multiplication Table of",num,"is:\n");
                            for i in range(1,11):
                                print(num,"x",i,"=",num*i);
                        case 3:
                            num=int(input("Enter the Number for floor division:"));
                            den=int(input("Enter the Denominator:"));
                            result=num//den;
                            print("Floor Division of",num,"by",den,"is:",result);
                        case 4:
                            num=int(input("Enter the Base Number:"));
                            pow=int(input("Enter the Power:"));
                            result=num**pow;
                            print("Power of",num,"to the",pow,"is:",result);
                        case 5:
                            print("\nExiting to Main Menu.");
                            break;
                        case _:
                            print("Invalid Choice");
                case 3:
                 while True:
                    print("\nSelect an option for Series Program:");
                    print("1.Square of Number.");
                    print("2.Cubes of Number.");
                    print("3.Exit.");
                   
                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                            num=int(input("Enter Number:"));
                            print("Square of",num,"is:",num**2);
                        case 2:
                            num=int(input("Enter Number:"));
                            print("Cubes of",num,"is:",num**3);
                        case 3:
                            print("\nExiting to Main Menu.");
                            break;
                        case _:
                            print("Invalid Choice");       
                case 4:
                 while True:
                    print("\nSelect an option for Statistics on Range:");
                    print("1.Largest Number from 3 numbers.");
                    print("2.Smallest Number from 3 numbers.");
                    print("3.Average of range.");
                    print("4.Exit.");
                   
                    choice=int(input("\nEnter Your Choice:"));
                    match choice:
                        case 1:
                            num1=int(input("Enter First Number:"));
                            num2=int(input("Enter Second Number:"));
                            num3=int(input("Enter Third Number:"));
                            if num1>=num2 and num1>=num3:
                                print("Largest Number from the given 3 numbers is:",num1);
                            elif num2>=num1 and num2>=num3:
                                print("Largest Number from the given 3 numbers is:",num2);  
                            else:
                                print("Largest Number from the given 3 numbers is:",num3);
                        case 2:
                            num1=int(input("Enter First Number:"));
                            num2=int(input("Enter Second Number:"));
                            num3=int(input("Enter Third Number:"));
                            if num1<=num2 and num1<=num3:
                                print("Smallest Number from the given 3 numbers is:",num1);
                            elif num2<=num1 and num2<=num3:
                                print("Smallest Number from the given 3 numbers is:",num2);
                            else:
                                print("Smallest Number from the given 3 numbers is:",num3);
                        case 3:
                            start=int(input("Enter Start of Range:"));
                            end=int(input("Enter End of Range:"));
                            sum=0;
                            for i in range(start,end+1):
                                sum+=i;
                            print("Average of numbers from",start,"to",end,"is:",sum/end);
                        case 4:
                            print("\nExiting to Main Menu.");
                            break;
                        case _:
                             print("Invalid Choice");
                case 5:
                    print("\nExiting to Main Menu.");
                    break;
                case _:
                    print("Invalid Choice");       
        case 3:
            print("\nExiting the Program.Goodbye!");
            break;
        case _:
            print("Invalid Choice");