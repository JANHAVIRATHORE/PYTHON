from Mypackage import Date_Time
from Mypackage import Mathematical_ope
from Mypackage import Random
from Mypackage import File_Operator
from Mypackage import Explore_module
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
             Date_Time.main() 

        elif choice==2:
             Mathematical_ope.main()

        elif choice==3:
            Random.main()

        elif choice==4:
            print("\nGenerate Unique Identifiers:\n")
            id=uuid.uuid4()
            print(f"Generated UUId: {id}\n")
            print("="*50);

        elif choice==5:
            File_Operator.main()


        elif choice==6:
            Explore_module.main()

        elif choice==7:
            print("="*50);
            print("Thank You for using the Multi-Utility Toolkit!");
            print("="*50,"\n");
            break;
    
    except ValueError:
        print("\nInvalid Option! Please select a valid option from the menu.\n");
        print("="*50);
