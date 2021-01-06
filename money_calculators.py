def calc_money():
    print("Welcome to the most simple retirement calculator you'll ever use!")
    user_choice = ""
    
    while user_choice != "q":
        print("\n[1] Enter 1 to check when you'll retire based on investing monthly savings.")
        print("[2] Enter 2 to see how much money you can earn in ten years by investing a luxury expense (like coffee or eating out).")
        print("[q] Enter q to quit")

        user_choice = input("\nWhat would you like to do? ")

        user_choice = user_choice.lower()

        if user_choice == "q":
            print("\nHave a great life!")

        elif user_choice == "1":

            while True:              
                
                try:
                    monthly_income = int(input("What is your monthly income (whole numbers only)? "))
                except:
                    print("Please enter a valid whole number")
                else:
                    break

            while True:
                
                try:
                    monthly_spend = int(input("what is your monthy spend (whole numbers only)? "))
                except:
                    print("Please enter a valid whole number")
                else:
                    break
            
            if monthly_spend > monthly_income:
                print("\nYour spend is greater than your income, you'll never retire at this rate.")

            else:
                savings_percent = int(100 - ((monthly_spend / monthly_income) * 100))

                if savings_percent <= 5:
                    print("\nYou'll retire in 66 years, you need to start saving more money.")
                elif 5 < savings_percent <= 10:
                    print("\nYou'll retire in 51 to 66 years, you need to start saving more money.")
                elif 10 < savings_percent <= 15:
                    print("\nYou'll retire in 43 to 50 years, you need to start saving more money.")
                elif 15 < savings_percent <= 20:
                    print("\nYou'll retire in 37 to 42 years, you need to start saving more money.")
                elif 20 < savings_percent <= 25:
                    print("\nYou'll retire in 32 to 36 years, you need to start saving more money.")
                elif 25 < savings_percent <= 30:
                    print("\nYou'll retire in 28 to 31 years, you need to start saving more money.")
                elif 30 < savings_percent <= 35:
                    print("\nYou'll retire in 25 to 27 years, not bad, but you can do better.")
                elif 35 < savings_percent <= 40:
                    print("\nYou'll retire in 22 to 25 years, not bad, but you can do better!")
                elif 40 < savings_percent <= 45:
                    print("\nYou'll retire in 19 to 21 years, not bad, but you can do better!")
                elif 45 < savings_percent <= 50:
                    print("\nYou'll retire in 17 to 18 years, not bad, but you can do better!")
                elif 50 < savings_percent <= 55:
                    print("\nYou'll retire in 14.5 to 16 years, you're doing pretty good! But I think you can do better!")
                elif 55 < savings_percent <= 60:
                    print("\nYou'll retire in 12.5 to 14.5 years, you're doing pretty good! But I think you can do better!")
                elif 60 < savings_percent <= 65:
                    print("\nYou'll retire in 10.5 to 12.5 years, you're doing pretty good! But I think you can do better!")
                elif 65 < savings_percent <= 70:
                    print("\nYou'll retire in 8.5 to 10.5 years, great, you're ahead of most people!")
                elif 70 < savings_percent <= 75:
                    print("\nYou'll retire in 7 to 8.5 years, great, you're ahead of most people!")
                elif 75 < savings_percent <= 80:
                    print("\nYou'll retire in 5.5 to 7 years, great, you're ahead of most people!")
                elif 80 < savings_percent <= 85:
                    print("\nYou'll retire in 4 to 5.5 years, you're killing it!")
                elif 85 < savings_percent <= 90:
                    print("\nYou'll retire in 3 to 4 years, great work, retirement is right around the corner!")
                elif 90 < savings_percent <= 95:
                    print("\nYou'll retire in less than 2 to 3 years, great work, retirement is right around the corner!")
                elif 95 < savings_percent <= 100:
                    print("\nIf you're not already retired, you'll retire any day now! You made it to the end-game, enjoy retirement!")

        elif user_choice == "2":
            print("\n[1] Enter 1 for a weekly expense.")
            print("[2] Enter 2 for a monthly expense.")

            user_selection = input("\nWould you like to calculate a monthly or weekly expense? ")

            if user_selection == "1":
                while True:      
                    try:
                        weekly_expense = int(input("What is your weekly expense (whole numbers only)? "))
                    except:
                        print("Please enter a valid whole number")
                    else:
                        break
                
                investment_total = weekly_expense * 752

                print(f"\nIn 10 years your weekly expense of ${weekly_expense} will be worth about ${investment_total} if invested instead!")

            if user_selection == "2":
                while True:              
                    try:
                        monthly_expense = int(input("What is your monthly expense (whole numbers only)? "))
                    except:
                        print("Please enter a valid whole number")
                    else:
                        break
                
                investment_total2 = monthly_expense * 173

                print(f"\nIn 10 years your monthly expense of ${monthly_expense} will be worth about ${investment_total2} if invested instead!")        
            
        elif user_choice != "1" or user_choice != "2":
            print("\nYou must enter 1 or 2 to continue.")

calc_money()

