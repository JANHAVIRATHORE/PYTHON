import Mypackage
import uuid

if __name__=="__main__":
    pass

print("="*50);
print("Welcome to Multi-Utility Toolkit");
print("="*50,"\n");
while True:
    print("choose an option:");
    print("1.Datetime and time Operations");
    print("2.Mathematical Operations");
    print("3.Random Data Generation");
    print("4.Generate Unique Identifiers (UUId)");
    print("5.File Operations (Custom Module)");
    print("6.Explore Module Attributes (dir())");
    print("7.Exit");
    print("="*50);

    try:
        choice=int(input("\nEnter Your Choice:"));

        if choice==1:
            import Mypackage.Date_Time;

        elif choice==2:
            import Mypackage.Mathematical_ope;

        elif choice==3:
            import Mypackage.Random;

        elif choice==4:
            print("\nGenerate Unique Identifiers:\n")
            id=uuid.uuid4()
            print(f"Generated UUId: {id}\n")
            print("="*50);

        elif choice==5:
            import Mypackage.File_Operator;

        elif choice==6:
            import Mypackage.Explore_module;

        elif choice==7:
            print("="*50);
            print("Thank You for using the Multi-Utility Toolkit!");
            print("="*50,"\n");
            break;
    
    except ValueError:
        print("\nInvalid Option! Please select a valid option from the menu.\n");
        print("="*50);
