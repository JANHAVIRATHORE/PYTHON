student=[];
subjects=set();
while True:
    print("\nWelcome to the Student Data Organizer!");
    print('''
This program will help you organize your student data efficiently.
In this you can:
 -Add new student's details.
 -View all available records.
 -Update a record.
 -Delete a record. 
 -View available subject provided to students.
''');
    
    print("\nSelete an Option!!\n");
    print("1.Add Student");
    print("2.Display All Students");
    print("3.Update Student Information");
    print("4.Delete Student");
    print("5.Display Subject Offered");
    print("6.Exit\n");

    choice=int(input("Enter Your Choice:"));
    
    if choice==1:
        print("\nEnter Student Details:\n\n(Once Id and Subjects enter can not be altered)\nRead Before Enter....\n");
        st_id=int(input("Id: "));
        stu_name=input("Name: ");
        stu_age=int(input("Age: "));
        stu_grade=input("Grade: ");
        stu_dob=input("Date Of Birth (YYYY-MM-DD): ");
        stu_sub=input("Subjects (Comma-separated): ");
        
        stu_id=(st_id,);
        subject=set(stu_sub.split(","));
        
        stu_info={
            "id":stu_id,
            "name":stu_name,
            "age":stu_age,
            "grade":stu_grade,
            "dob":stu_dob,
            "subject":subject
        }
        subjects.update(subject);
        student.append(stu_info);
        print("\nStudent Added Successfully!!\n");
        
    elif choice==2:
        print("\n--- Display All Students ---\n");
        if student==[]:
            print("\nNo student records available!!\n");
            continue;
        else:
            student.sort(key=lambda x:x["id"],reverse=False);
            for detail in student:
                print(f"\nStudent Id: {detail["id"]} | Name: {detail["name"]} | Age: {detail["age"]} | Grade: {detail["grade"]} | Date Of Birth: {detail["dob"]} | Subjects: ",end=" ");            
                for sub in detail["subject"]:
                    print(sub,end=",");
            print("\n\nThe End Of Student Record...\n");

    elif choice==3:
        print("\n--- Update Student Information ---\n");
        upd_id=int(input("Enter Student Id Whose Record To Update: "));
        found=False;   
        for detail in student:
            if detail["id"]==(upd_id,):
                print("\nOld Detail:\n",detail);
                detail["name"]=input("Enter New Name: ");
                detail["age"]=int(input("Enter New Age: "));
                detail["grade"]=input("Enter New grade: ");
                detail["dob"]=input("Enter New Date Of Birth: ");
                found=True;
                print("\nNew Detail:\n",detail);
                print("\nStudent detail updated successfully!!\n");
        if found==False:
            print("\nStudent does not exist!!\n")
    elif choice==4:
        print("\n--- Delete Student ---\n");
        del_id=int(input("Enter Student Id To Delete: "));
        found=False;      
        for detail in student:
            if detail["id"]==(del_id,):
                del student[student.index(detail)];
                found=True;
                print("\nStudent detail deleted successfully!!\n");
        if found==False:
            print("\nStudent does not exist!!\n")

    elif choice==5:
        print("\n--- Display Subjects Offered ---\n");
        if student==[]:
            print("\nNo subject's records available!!\n");
            continue;
        else :
            for sub in subjects:
                print(sub,end="\n");
    elif choice==6:
        print("\nThank you for visiting Student Data Organizer!!\nGoodBye (^-^)\n");
        break;
    else:
        print("\nPlease enter a valid choice!\n");

    
