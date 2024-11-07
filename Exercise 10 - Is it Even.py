#declare the function for checking the numbers if it is odd or even:
def odd_or_even(number):
    if number % 2 == 0:
        return f"the {number} is even."
    else:
        return f"the {number} is odd."

#now proceed to making another function that asks for user input:
def main():
    number = int(input("Enter your number: "))
        #declare for the result so it can process in the odd_or_even function:
    result = odd_or_even(number)
        #then we print out the results
    print(result)

#lastly, run the main function
if __name__ == "__main__":
    main()