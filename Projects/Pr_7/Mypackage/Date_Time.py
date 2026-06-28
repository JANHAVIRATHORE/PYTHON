import datetime
import time

if __name__=="__main__":
    pass

class date_time:
    def __init__(self):
        now=datetime.datetime.now();
        print(f"\nCurrent Date and Time:{now}");
        print("="*50,"\n");

class diff_date:

    def Date(self,dt1,dt2):
        self.date1 = datetime.datetime.strptime(dt1, "%Y-%m-%d");
        self.date2 = datetime.datetime.strptime(dt2, "%Y-%m-%d");
        difference=abs(self.date1-self.date2);
        print(f"\nDifference:{difference.days} days");
        print("="*50,"\n");

    def Time(self,t1,t2):
        self.time1 = datetime.datetime.strptime(t1, "%H:%M:%S");
        self.time2 = datetime.datetime.strptime(t2, "%H:%M:%S");
        difference=abs(self.time1-self.time2);
        print(f"\nDifference:{difference} time");
        print("="*50,"\n");

class format:
        def __init__(self):
            now = datetime.datetime.now();
            formatted_date = now.strftime("%d-%m-%Y %H:%M:%S");
            print("\nFormatted Date:", formatted_date);
            print("="*50,"\n");

class watch():
    def __init__(self,start,end):
        pass
        # print("\nStopwatch")
        # print("=" * 40)

        # input("Press Enter to Start the Stopwatch...")

        # start_time = datetime.datetime.now()

        # print("\nStopwatch Started!")
        # input("Press Enter to Stop the Stopwatch...")

        # end_time = datetime.datetime.now()

        # elapsed_time = end_time - start_time

        # print("\n" + "=" * 40)
        # print(f"Start Time   : {start_time.strftime('%H:%M:%S')}")
        # print(f"Stop Time    : {end_time.strftime('%H:%M:%S')}")
        # print(f"Elapsed Time : {elapsed_time}")
        # print("=" * 40)

class timer():
    def __init__(self,start):
        self.start=start;
        print("\nStarting CountDown....");
        for i in range(self.start,0-1,-1):
            print(i);
            time.sleep(1)
        print("Time's Up!!");
        print("="*50,"\n");

print("\nDatetime and Time Operations:");
while True:
    print("1.Display current date and time.");
    print("2.Calculate difference between two dates/times.");
    print("3.Format date into custom format.");
    print("4.Stopwatch.");
    print("5.Countdown Timer.");
    print("6.Back to Main Menu");

    try:
        choice=int(input("\nEnter Your Choice:"));

        if choice==1:
            date_obj=date_time();

        elif choice==2:
         while True:
            print("1.Calculate difference between two dates.");
            print("2.Calculate difference between two times.");
            print("3.Exit.");
            choice=int(input("\nEnter Your Choice:"));
        
            if choice==1:
                date1=input("Enter the first date (YYYY-MM-DD): ");
                date2=input("Enter the second date (YYYY-MM-DD): ");

                dateobj=diff_date();
                dateobj.Date(date1,date2);
                
            elif choice==2:
                time1=input("Enter the first time (HH:MM:SS): ");
                time2=input("Enter the second time (HH:MM:SS): ");

                timeobj=diff_date();
                timeobj.Time(time1,time2);

            elif choice==3:
                break; 

            else:
                print("Invalid choice!!");

        elif choice==3:
            formate_obj=format();

        elif choice==4:
            start=input("press enter to start watch:");
            end=input("press enter to stop watch:");
            watch_obj=watch(start,end);

        elif choice==5:
            start=int(input("Enter Starting Time (seconds):"));
            timer_obj=timer(start);

        elif choice==6:
            print("="*50,"\n");
            break;

    except ValueError:
        print("\nInvalid Option! Please select a valid option from the menu.\n");
        print("="*50);