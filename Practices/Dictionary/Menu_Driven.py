student={};
while True:
    print("\nWelcome to Student Management System!\n");
    print("Enter 1 To Add Student Details.");
    print("Enter 2 To View Student Details.");
    print("Enter 3 To Update Student Details.");
    print("Enter 4 To Delete Student Details.");
    print("Enter 0 To Exit.");
    choice=int(input("\nEnter Your Choice:"));
    
    if choice==1:
        num=int(input("Enter How Many Details To Add:"));
        for i in range(num):
            key=input("Enter Key:");
            value=input(f"Enter Value for {key}:");
            student[key]=value;
        print("\nStudent Detail Added Successfully!!\n");
    if choice==2:
        for k,v in student.items():
            print(f"{k}:{v}");
        print("\nThe End Of Student Detail!!\n")
    if choice==3:
            for k,v in student.items():
                print(f"Keys are:{k}",end=" ");
            stud=input("\nEnter Student Key Whose Value To Update:");
            found=False;
            for k,v in student.items():
                if stud==k:
                    n_value=input(f"Old value:{v} \nEnter New Value for {k}:");
                    student[k]=n_value;
                    found=True;
                    print("\nStudent Updated Successfully!!\n");
            if found==False:
                 print("\nstudent not found\n");
    if choice==4:
            for k,v in student.items():
                print(f"Keys are:{k}",end=" ");
            stud=input("\nEnter Student Key Which To Delete:");
            found=False;
            for k,v in student.items():
                if stud==k:
                    student.pop(k);
                   
                    found=True;
                    break;
                print("\nStudent Detail Deleted Successfully!!\n");
            if found==False:
                 print("\nstudent not found\n");
                    
    if choice==0:
        print("\nThank You!!\n");
        break;
