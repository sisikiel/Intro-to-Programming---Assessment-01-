#this exercise focuses on the days of the months. The first thing we have to do is to ask the user for the month number.
#then the user value will print out specific days in a month.
#advanced requirement: include leap years.

#make a dictionary that contains the months with days.
days_months = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

#start coding using while loop.
while True:
    try:
        selected_month = int(input("Enter your month number (from 1 to 12): ")) #ask for user input
        if selected_month in days_months:
            if selected_month == 2: #for february/leap year:

                leap = input("(Yes or no) Is it a leap year? ")
                if leap.casefold() == "yes".casefold(): #.casefold() is used to avoid case sensitivity.
                    print("Your selected month number [2] has 29 days")
                else:
                    print("Your selected month number [2] has 28 days")

            else:
                print(f"Your selected month number {selected_month} has {days_months[selected_month]} days.")

        else: #if the user inputted numbers above 12.
            print("You inputted an invalid number. Try again")

    except ValueError: #this is if the user inputs "twelve" instead of 12.
        print("Please enter a numerical value. Try agin")