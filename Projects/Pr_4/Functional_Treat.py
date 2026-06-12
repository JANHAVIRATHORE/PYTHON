arr=[];
def create():
    """This function is used to create and store data in the 1-D array.Of type without parameter and without return."""
    arr1=[int(i) for i in input("Enter Data for your Array (Separator by spaces):").split()];
    arr.extend(arr1);

def built_in():
    """This function is used to display the summary of the dataset using built-in functions like len(), min(), max(), sum().Of type without parameter and without return."""
    print(f"Total elements:{len(arr)}");
    print(f"Minimum element:{min(arr)}");
    print(f"Maximum Element:{max(arr)}");
    print(f"Sum of All element:{sum(arr)}");
    print(f"Average Value:{sum(arr)/len(arr)}");
    
def fact(no):
    """This function is used to calculate the factorial of a number using recursion.Of type with parameter and with return."""
    if no==1:
        return 1;
    return no*fact(no-1);

def above(value):
    """This function is used to filter data above a given threshold.Of type with parameter and without return."""
    print(f"Filtered Data:(Value>={value}){[i for i in arr if i>=value]}: ");

def below(value):
    """This function is used to filter data below a given threshold.Of type with parameter and without return."""
    print(f"Filtered Data:(Value<={value}){[i for i in arr if i<=value]}: ");

def ascen():
    """This function is used to sort data in ascending order.Of type without parameter and with return."""
    return sorted(arr);

def decen():
    """This function is used to sort data in descending order.Of type without parameter and with return."""
    return sorted(arr,reverse=True);

def statis():
    """This function is used to display the statistics of the dataset like length, minimum, maximum, sum, and average.Of type without parameter and with multiple value return."""
    length=[len(arr)];
    minimum=[min(arr)];
    maximum=[max(arr)];
    sum_all=[sum(arr)];
    avg=[sum(arr)/len(arr)];
    return length,minimum,maximum,sum_all,avg;

while True:
    print("\nWelcome to the Data Analyzer and Transformer Program\n");
    print("Main Menu:");
    print("1. Input Data,Read Data");
    print("2. Display Data Summary (Built-in Functions)");
    print("3. calculate Factorial (Recursion)");
    print("4. Filter Data by Threshold (Lambda Function)");
    print("5. Sort Data");
    print("6. Display Dataset Statistics (Return Multiple Values)");
    print("7. Exit Program");

    choice=int(input("\nEnter Your Choice:"));
    
    if choice==1:
     while True:
        print("1.To Input Data");
        print("2.To Read Data");
        print("3.To Remove Duplicate Value");
        print("4.Exit");

        choice=int(input("\nEnter Your Choice:"));

        if choice==1:
            print("\nData Input Selected");
            print(f"\nfunction name:create()={create.__doc__}\n");
            create();
            print("\nData has been stored successfully!!\n");
        elif choice==2:
            print(arr);
        elif choice==3:
            arr=list(set(arr));
            print("\nDuplicate value has been removed successfully,you can view it again!!\n");
        elif choice==4:
            print("\nYou are Exiting to the main menu!!\n");
            break;
        else:
            print("\nInvalid choice!!\n");
    
    elif choice==2:
        print("\nData Summary Selected\n");
        print(f"\nfunction name:built_in()={built_in.__doc__}\n");
        built_in();
    
    elif choice==3:
        print("\nFactorial is selected\n");
        print(f"\nfunction name:fact()={fact.__doc__}\n");
        num=int(input("Enter a number to calculate its Factorial:"));
        print(f"Factorial of {num} is:{fact(num)}");
    
    elif choice==4:
     while True:
        print("\nFilter Data by Threshold is selected\n");
        print("1.For Filter out value,above your enter value");
        print("2.For Filter out value,below your enter value");
        print("3.Exit");

        choice=int(input("\nEnter your choice:"));
        if choice==1:
            print(f"\nfunction name:above()={above.__doc__}\n");
            value=int(input("Enter your Threshold Value:"));
            above(value);     
        elif choice==2:
            print(f"\nfunction name:below()={below.__doc__}\n");
            value=int(input("Enter your Threshold Value:"));
            below(value);
        elif choice==3:
            print("\nYou are Exiting to the main menu!!\n");
            break;
        else:
            print("\nInvalid choice!!\n");
    
    elif choice==5:
        print("\nSort Data is selected\n");
        print("1.Ascending order");
        print("2.Decending order");
        print("3.Exit");
        choice=int(input("Enter your choice:"));
        if choice==1:
            print("\nSorted data in ascending order:");
            print(f"\nfunction name:ascen()={ascen.__doc__}\n");
            print(f"{ascen()}");
        elif choice==2:
            print("\nSorted data in decending order:");
            print(f"\nfunction name:decen()={decen.__doc__}\n");
            print(f"{decen()}");
        elif choice==3:
            print("\nYou are Exiting to the main menu!!\n");
            break;
        else:
            print("\nInvalid choice!!\n");
    
    elif choice==6:
        print("\nDataset Statistics is selected\n");
        print(f"function name:statis()={statis.__doc__}\n");
        a,b,c,d,e=statis();
        print(f"Total Length:{a}");
        print(f"Minimum Value:{b}");
        print(f"Maximum value:{c}");
        print(f"Sum all value:{d}");
        print(f"Average value:{e}");

    elif choice==7:
        print("\nThank you for using the Data Analyzer and Transformer Program!!\nGoodBye (^-^)\n");
        break;

    else:
        print("\nPlease enter a valid choice!\n");
