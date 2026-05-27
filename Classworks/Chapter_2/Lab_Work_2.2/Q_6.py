'''Write a Program in Python to create a menu-driven telecom calling system 
   using the 'match-case' feature.
  -For example:
         -Press 1 for English
         -Press 2 for Hindi
         -Press 3 for Gujarati
  -Extend this program by adding a nested match case for each menu item's
   appropriate subtype selection by the user.'''

while True:
    print("\nWelcome to the Telecom Calling System\n");
    print("1.For Service in English");
    print("2.For Service in Hindi");
    print("3.For Service in Gujarati");
    print("4.To Exit");
    choice=int(input("Choose A Language:"));
    match choice:
        case 1:
         while True:
            print("\nWelcome to the Telecom Calling System\n");
            print("1.For Recharge");
            print("2.For Internet Data Pack");
            print("3.For Customer Care");
            print("4.To Exit");
            choice=int(input("Choose What you Want to do:"));
            match choice:
                case 1:
                 while True:
                    print("\nFor Recharge!\n");
                    print("1.PrePaid Plan");
                    print("2.PostPaid Plan");
                    print("3.To Exit");
                    choice=int(input("Choose Your Plan:"));
                    match choice:
                        case 1:
                            print("You now have a prepaid Plan");
                        case 2:
                            print("You now have a Postpaid Plan");
                        case 3:
                            break;
                        case _:
                            print("Invalid Choice!");
                case 2:
                 while True:
                    print("\nFor Internet Data Pack!\n");
                    print("1.Daily Pack");
                    print("2.Unlimited Pack");
                    print("3.To Exit");
                    choice=int(input("Choose Your Plan:"));
                    match choice:
                        case 1:
                            print("You now have a Daily Pack of 2GB.");
                        case 2:
                            print("You now have a Unlimited Data Pack.");
                        case 3:
                            break;
                        case _:
                            print("Invalid Choice!");
                case 3:
                 while True:
                    print("\nFor Customer Care!\n");
                    print("1.Technical Issue");
                    print("2.Network Issue");
                    print("3.To Exit");
                    choice=int(input("Choose Your Plan:"));
                    match choice:
                        case 1:
                            print("Type Your Issue Here:");
                            print("We Get your Issue,We will Work on it.");
                        case 2:
                            print("Type Your Issue Here:");
                            print("We Get your Issue,We will Work on it.");
                        case 3:
                            break;
                        case _:
                            print("Invalid Choice!");
                case 4:
                    break;
                case _:
                    print("Invalid Choice!");
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Thank you for your visit!");
            break;
        case _:
            print("Invalid Choice!");