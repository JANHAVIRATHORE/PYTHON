'''Write a Program in Python to create a menu-driven fast-food order system 
   using the 'match-case' feature.
  -For example:
         -Press 1 to order a sandwich
         -Press 2 to order a Pizza
         -Press 3 to order a Burger
  -Extend this program by adding a nested match case for each menu item's
   subtype selection by the user.
  -For example:
         -Press 1 for Thin Crust Pizza
         -Press 2 for Cheese Burst Pizza
         -Press 3 for Fresh Dough Pizza'''
while True:
    print("\nWelcome to fast food court!\n");
    print("1.To Order Sandwich.");
    print("2.To Order Pizza.");
    print("3.To Order burger.");
    print("4.To Exit");

    order=int(input("\nEnter your preferred order:"));
    match order:
        case 1:
         while True:
            print("\nYou Want a Sandwich with!\n");
            print("1.veg. Sandwich.");
            print("2.Cheese burst Sandwich.");
            print("3.Grilled Sandwich.");
            print("4.To Exit");

            order=int(input("\nEnter your preferred order:"));
            match order:
                case 1:
                    print("\nyou have order veg. Sandwich.!");
                case 2:
                    print("\nyou have order Cheese burst Sandwich.!");
                case 3:
                    print("\nyou have order Grilled Sandwich.!");
                case 4:
                    break;
                case _:
                    print("Invalid Choice!");
        case 2:
         while True:
            print("\nYou Want a Pizza with!\n");
            print("1.Thin crust Pizza.");
            print("2.Cheese burst Pizza.");
            print("3.Fresh Dough Pizza.");
            print("4.To Exit");

            order=int(input("\nEnter your preferred order:"));
            match order:
                case 1:
                    print("\nyou have order Thin crust Pizza.!");
                case 2:
                    print("\nyou have order Cheese burst Pizza.!");
                case 3:
                    print("\nyou have order Fresh Dough Pizza.!");
                case 4:
                    break;
                case _:
                    print("Invalid Choice!");
        case 3:
         while True:
            print("\nYou Want a Burger with!\n");
            print("1.Regular Burger.");
            print("2.Cheese burst Burger.");
            print("3.Double Layer Burger.");
            print("4.To Exit");

            order=int(input("\nEnter your preferred order:"));
            match order:
                case 1:
                    print("\nyou have order Regular Burger.!");
                case 2:
                    print("\nyou have order Cheese burst Burger.!");
                case 3:
                    print("\nyou have order Double Layer Burger.!");
                case 4:
                    break;
                case _:
                    print("Invalid Choice!");
        case 4:
            print("\nThank You for your order!!");
            break;
        case _:
            print("Invalid Choice!");
 