class add:
    def __init__(self,dt,tm,ent):
        self.date=dt
        self.time=tm
        self.entry=ent

        file= open("Personal_Journal.txt","+a");    
        file.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------\n");
        file.write(''' Date    \t  Time \t\t\tEntry''')
        file.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------\n");
        file.write(" [");
        file.write(self.date);
        file.write("]");
        file.write("\t")
        file.write("[");
        file.write(self.time);
        file.write("]");
        file.write("\t\t");
        file.write(self.entry);
        file.close();
    
    def get_info(self):
        print("\nEntry added Successfully!\n");

class read:
    def __init__(self):
        try:
            file= open("Personal_Journal.txt","r");
            content=file.read();
            # file= open("Personal.txt","r");
            if content=="":
                raise IndexError("\nThe Journal File Does not Exist.Please add a new Entry.\n");   
            else:
                print("\nYour Journal Entries:");
                # content=file.read(); 
                print(content)   
                file.close(); 
        except IndexError:
            print("\nThe Journal File Does not Exist.Please add a new Entry.\n");
        except FileNotFoundError:
            print("\nNo Journal Entries Found. Start By adding a new entry!\n");

class search:
    def search_info(self,find):
        self.find=find
        found=False
        try:
            file= open("Personal_Journal.txt","r");
            content=file.readlines();
            file.close();

            for line in content:
                if self.find in line:
                    print("\nMatching Entries:");
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------\n");
                    print("Date \t\t Time \t\t\t Entry");
                    print(line,end="");
                    found=True
            if found==False: 
                print(f"\nNo Entries were found for the keyword: {self.find}\n"); 
        except Exception:
            print(f"\nError Occur!\n");
       
class delete:
    def __init__(self,ans):
        self.answer=ans
        try:
            if self.answer=="yes":
                file=open("Personal_Journal.txt","+w");
                journal.clear();
                file.close();
                print("\nAll the Journal Entries have been Deleted.\n")
        except FileNotFoundError:
            print("\nNo Journal Entries to Delete.\n");
        except Exception:
            print("\nError No Journal Found\n")


journal=[];
while True:
    print("\nWelcome To Personal Journal Manager!");
    print("Please select an option:");
    print("\n1.Add a New Entry");
    print("2.View All Entries");
    print("3.Serach for an Entry");
    print("4.Delete All Entries");
    print("5.Exit");

    try:
        choice=int(input("\nUser Input:"));
        
        if choice==1:        
            date=input("\nEnter Date of Journal Entry (YYYY-MM-DD):");
            time=input("Enter Time of Journal Entry (HH-MM-SS):");    
            entry= input("Enter Your Journal Entry:");  

            journal.append(date);
            journal.append(time);
            journal.append(entry);
            addobj=add(date,time,entry)
            addobj.get_info();
        
        elif choice==2:
            viewobj=read()
            
        elif choice==3:
            word=input("\nEnter a keyword or Date to Search:");
            sobj=search();
            sobj.search_info(word);
        
        elif choice==4:  
            choose=input("\nAre you sure you want to delete all Entries? (Yes/No):\n").lower();    
            delobj=delete(choose);  
        
        elif choice==5:
            print("\nThank You for using Personal Journal Manager. GoodBye!\n")
            break
    except ValueError:
        print("\nInvalid Option! Please select a valid option from the menu.\n");