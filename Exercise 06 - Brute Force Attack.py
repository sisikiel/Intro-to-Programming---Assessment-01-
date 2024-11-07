#Exercise 6 needs the user to place a correct password. In order to do that we have to use the while loop.
#Advance requirement: limit the user to only have 5 attempts in putting the password.

#declare the amount of max attempts.
maximum_attempts = 5

#assume the amount of attempts.
attempts = 0

#start the coding
while attempts < maximum_attempts: #declare while loop
    #ask the user to enter their password.
    correctPIN = int(input("Enter your numerical password: "))

    if correctPIN == 12345: #12345 is the correct default password.
        print("Your PIN is correct!")
        break #stops the code once it met the desired answer.
    else:
        attempts +=1 #if the user got the answer wrong, it reduces the amount of attempts they have left.
        remaining_attempts = maximum_attempts - attempts
        if remaining_attempts < 5:
            print(f"Incorrect password. You have {remaining_attempts} remaining.")

#if the user reached the maximum amount of attempts, it will display the following:
else:
    print(f"You have entered the maximum amount of attempts. The authorities have been contacted. ")