'''Write a Program in Python to create a menu-driven telecom calling system 
   using the 'match-case' feature.
  -For example:
         -Press 1 for English
         -Press 2 for Gujarati
         -Press 3 for Hindi
  -Extend this program by adding a nested match case for each menu item's
   appropriate subtype selection by the user.'''

while True:
    print("\nWelcome to the Telecom Calling System\n");
    print("1.For Service in English");
    print("2.For Service in Gujarati");
    print("3.For Service in Hindi");
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
         while True:
            print("\nટેલિકોમ કોલિંગ સિસ્ટમમાં આપનું સ્વાગત છે\n")
            print("1. રિચાર્જ માટે")
            print("2. ઇન્ટરનેટ ડેટા પેક માટે")
            print("3. ગ્રાહક સેવા માટે")
            print("4. બહાર નીકળવા માટે")

            choice = int(input("તમારે શું કરવું છે તે પસંદ કરો: "))

            match choice:
                case 1:
                    while True:
                        print("\nરિચાર્જ માટે!\n")
                        print("1. પ્રીપેઇડ પ્લાન")
                        print("2. પોસ્ટપેઇડ પ્લાન")
                        print("3. બહાર નીકળવા માટે")

                        choice = int(input("તમારો પ્લાન પસંદ કરો: "))

                        match choice:
                            case 1:
                                print("હવે તમારી પાસે પ્રીપેઇડ પ્લાન છે.")
                            case 2:
                                print("હવે તમારી પાસે પોસ્ટપેઇડ પ્લાન છે.")
                            case 3:
                                break
                            case _:
                                print("અમાન્ય પસંદગી!")

                case 2:
                    while True:
                        print("\nઇન્ટરનેટ ડેટા પેક માટે!\n")
                        print("1. દૈનિક પેક")
                        print("2. અનલિમિટેડ પેક")
                        print("3. બહાર નીકળવા માટે")

                        choice = int(input("તમારો પ્લાન પસંદ કરો: "))

                        match choice:
                            case 1:
                                print("હવે તમારી પાસે દરરોજ 2GB ડેટા પેક છે.")
                            case 2:
                                print("હવે તમારી પાસે અનલિમિટેડ ડેટા પેક છે.")
                            case 3:
                                break
                            case _:
                                print("અમાન્ય પસંદગી!")

                case 3:
                    while True:
                        print("\nગ્રાહક સેવા માટે!\n");
                        print("1. ટેક્નિકલ સમસ્યા");
                        print("2. નેટવર્ક સમસ્યા");
                        print("3. બહાર નીકળવા માટે");

                        choice = int(input("તમારો વિકલ્પ પસંદ કરો: "));

                        match choice:
                            case 1:
                                print("તમારી સમસ્યા અહીં લખો:");
                                print("અમને તમારી સમસ્યા મળી ગઈ છે, અમે તેના પર કામ કરીશું.");
                            case 2:
                                print("તમારી સમસ્યા અહીં લખો:");
                                print("અમને તમારી સમસ્યા મળી ગઈ છે, અમે તેના પર કામ કરીશું.");
                            case 3:
                                break;
                            case _:
                                print("અમાન્ય પસંદગી!");

                case 4:
                    print("સિસ્ટમ બંધ થઈ રહી છે...");
                    break

                case _:
                    print("અમાન્ય પસંદગી!");
        case 3:
         while True:
            print("\nटेलीकॉम कॉलिंग सिस्टम में आपका स्वागत है\n")
            print("1. रिचार्ज के लिए")
            print("2. इंटरनेट डेटा पैक के लिए")
            print("3. ग्राहक सेवा के लिए")
            print("4. बाहर निकलने के लिए")

            choice = int(input("आप क्या करना चाहते हैं चुनें: "))

            match choice:
                case 1:
                    while True:
                        print("\nरिचार्ज के लिए!\n")
                        print("1. प्रीपेड प्लान")
                        print("2. पोस्टपेड प्लान")
                        print("3. बाहर निकलने के लिए")

                        choice = int(input("अपना प्लान चुनें: "))

                        match choice:
                            case 1:
                                print("अब आपके पास प्रीपेड प्लान है।")
                            case 2:
                                print("अब आपके पास पोस्टपेड प्लान है।")
                            case 3:
                                break
                            case _:
                                print("अमान्य विकल्प!")

                case 2:
                    while True:
                        print("\nइंटरनेट डेटा पैक के लिए!\n")
                        print("1. दैनिक पैक")
                        print("2. अनलिमिटेड पैक")
                        print("3. बाहर निकलने के लिए")

                        choice = int(input("अपना प्लान चुनें: "))

                        match choice:
                            case 1:
                                print("अब आपके पास प्रतिदिन 2GB डेटा पैक है।")
                            case 2:
                                print("अब आपके पास अनलिमिटेड डेटा पैक है।")
                            case 3:
                                break
                            case _:
                                print("अमान्य विकल्प!")

                case 3:
                    while True:
                        print("\nग्राहक सेवा के लिए!\n")
                        print("1. तकनीकी समस्या")
                        print("2. नेटवर्क समस्या")
                        print("3. बाहर निकलने के लिए")

                        choice = int(input("अपना विकल्प चुनें: "))

                        match choice:
                            case 1:
                                print("अपनी समस्या यहाँ लिखें:")
                                print("हमें आपकी समस्या मिल गई है, हम इस पर काम करेंगे।")
                            case 2:
                                print("अपनी समस्या यहाँ लिखें:")
                                print("हमें आपकी समस्या मिल गई है, हम इस पर काम करेंगे।")
                            case 3:
                                break
                            case _:
                                print("अमान्य विकल्प!")

                case 4:
                    print("सिस्टम बंद किया जा रहा है...")
                    break

                case _:
                    print("अमान्य विकल्प!")
        case 4:
            print("Thank you for your visit!");
            break;
        case _:
            print("Invalid Choice!");