class employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
        
    def setInfo(self,__id__,__salary__=10000):
        self.__eid__=__id__
        self.__esalary__=__salary__

    def get_Info(self):
        print(f"\nName: {self.ename}\nAge: {self.eage}\nEmployee Id: {self.__eid__}\nSalary: ${self.__esalary__}");

    def __del__(self):
        pass

class manager(employee):
    def __init__(self, name, age,department):
        super().__init__(name, age)
        self.dep=department

    def setInfo(self, __id__, __salary__=30000):
        return super().setInfo(__id__, __salary__)
    
    def get_Info(self):
        print(f"\nName: {self.ename}\nAge: {self.eage}\nEmployee Id: {self.__eid__}\nSalary: ${self.__esalary__}\nDepartment: {self.dep}\n");

    def __del__(self):
        return super().__del__()
    
class developer(employee):
    def __init__(self, name, age,language):
        super().__init__(name, age)
        self.language=language

    def setInfo(self, __id__, __salary__=50000):
        return super().setInfo(__id__, __salary__)
    
    def get_Info(self):
        print(f"\nName: {self.ename}\nAge: {self.eage}\nEmployee Id: {self.__eid__}\nSalary: ${self.__esalary__}\nProgramming Language: {self.language}\n");

    def __del__(self):
        return super().__del__()
    
employees=[]
managers=[]
developers=[]

print("\n-- Python Oop Project: Employee Management System ---\n");
while True:
    print("\nChoose an Option:");
    print("1.Create a Developer");
    print("2.Create a Employee");
    print("3.Create a Manager");
    print("4.Show Details");
    print("5.Exit");

    choice=int(input("\nEnter Your choice:"));

    if choice==1:
        nm=input("Enter Name: ");
        age=int(input("Enter Age: "));
        id=input("Enter Employee Id: ");
        sal=int(input("Enter Salary: "));
        pro=input("Enter Programming Language: ");

        dobj=developer(nm,age,pro);
        dobj.setInfo(id,sal);
        developers.append(dobj);

    elif choice==2:
        nm=input("Enter Name: ");
        age=int(input("Enter Age: "));
        id=input("Enter Employee Id: ");
        sal=int(input("Enter Salary: "));
    
        eobj=employee(nm,age);
        eobj.setInfo(id,sal);
        employees.append(eobj);

    elif choice==3:
        nm=input("Enter Name: ");
        age=int(input("Enter Age: "));
        id=input("Enter Employee Id: ");
        sal=int(input("Enter Salary: "));
        dep=input("Enter Department: ");

        mobj=manager(nm,age,dep);
        mobj.setInfo(id,sal);
        managers.append(mobj);
        
    elif choice==4:
     while True:
        print("\nChoose detail to show:");
        print("1.Developer");
        print("2.Employee");
        print("3.Manager");
        print("4.Exit");

        choice=int(input("\nEnter Your choice:"));

        if choice==1:
            for d in developers:
                d.get_Info();

        elif choice==2:
            for e in employees: 
                e.get_Info();
        
        elif choice==3:
            for m in managers:
                m.get_Info();

        elif choice==4:
            print("\nExiting to main menu!!\n");
            break;

        else:
            print("\nPlease Enter A Valid choice!!\n");
        
    elif choice==5:
        print("\nExiting the system. All Resources have been freed.\n\nGoodBye!\n");
        print(f"\nIs manager class is derived from employee class:{issubclass(manager,employee)}");
        print(f"Is developer class is derived from employee class:{issubclass(developer,employee)}\n");

        break;

    else:
        print("\nPlease Enter A Valid choice!!\n");
    
    print("\n-- Choose another Operation --\n");