students=[];
while True:
    print("\nWelcome!!\n");
    print("1.To Create Student.");
    print("2.To View Student.");
    print("3.To Update Student.");
    print("4.To Delete Student.");
    print("0.To Exit.");

    choice=int(input("Enter Your Choice:"));
    if choice==1:
        st={
            "stid":len(students)+1,
            "name":input("Enter Student name:"),
            "age":int(input("Enter Student age:"))
        }
        students.append(st);
        print("\nStudent Added Successfully!");

    elif choice==2:
        stid=int(input("Enter Student id to View:"));
        found=False;
        for st in students:
            if st["stid"]==stid:
                print(st);
                found=True;
        if found==False:
            print("\nStudent not exit!\n");

    elif choice==3:
        stid=int(input("Enter Student id to View:"));
        found=False;
        for st in students:
            if st["stid"]==stid:
                st['name']=input("Enter the new name:");
                st['age']=int(input("Enter the new age:"));

                print("\nStudent Updated Successfully!\n");
                found=True;
        if found==False:
            print("\nStudent not exit!\n");

    elif choice==4:
        stid=int(input("Enter Student id to View:"));
        found=False;
        for st in students:
            if st["stid"]==stid:
                students.remove(st);
                print("\nStudent Deleted Successfully!\n");
                found=True;
        if found==False:
            print("\nStudent not exit!\n");

    elif choice==0:
        print("\nThank you!\n");
        break;

    else:
        print("\nInvalid choice!\n");