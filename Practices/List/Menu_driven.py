li=[];
while True:
    print("\nLet's work with List[]!\n");
    print("1.To Create a List.");
    print("2.To View the List.");
    print("3.To Update the List.");
    print("4.To Delete the List.");
    print("5.To Sort the List Order");
    print("6.To Reverse the List Order");
    print("7.To Exit");
    choice=int(input("Enter Your Choice:"));
    match choice:
        case 1:
            num=int(input("How many Element you want to Add in List:"));
            for i in range(1,num+1):
                value=int(input(f"Enter the Value for {i}:"));
                li.append(value);
            print("List Created successfully!");
        case 2:
            if li==[]:
                print("List is Empty!");
            else:
                print("The List Contain Values as:");
                for i in range(1,num+1):
                    print(f"The {i} Element is: {li[i-1]}");
                print("The End of List!");
        case 3:
            if li==[]:
                print("List is Empty!");
            else:
                index=int(input("Enter the Index, you want to Update:"));
                for i in range(1,num+1):
                    if i==index:
                        print(f"Old value for index {i} is {li[i-1]}");
                        new_value=int(input(f"Enter New Value for index {i}:"));
                        li[i-1]=new_value;
                print("Value Updated successfully!");
        case 4:
            if li==[]:
                print("List is Empty!");
            else:
                index2=int(input("Enter the Index, you want to Delete:"));
                for i in range(1,num+1):
                    if i==index2:
                        print(f"value for index {i} is {li[i-1]}");
                        del li[i-1];
                print("Value Deleted successfully!");
                num-=1;
        case 5:
            if li==[]:
                print("List is Empty!");
            else: 
                print("Element after Sorting are:");
                li.sort();
                for i in range(1,num+1):
                    print(f"The {i} Element now become: {li[i-1]}");
        case 6:
            if li==[]:
                print("List is Empty!");
            else:
                print("Element after Sorting are:");
                li.reverse();
                for i in range(1,num+1):
                    print(f"The {i} Element now become: {li[i-1]}");
        case 7:
            print("Thank for your visit!");
            break;
        case _:
            print("Invalid Choice!");