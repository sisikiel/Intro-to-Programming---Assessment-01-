#In exercise 4, I have to declare a question asking "what is the capital of france?" then wait for the user to answer.
#Advanced requirement: ignores the user's capitalization and extends the program with 10 more questions.

#the questions are placed within a dictionary along with its defined answer.
questions = { "What is the capital of France?" : "Paris", "What is the capital of Sweden?" : "Stockholm",
    "What is the capital of Italy?" : "Rome", "What is the capital of Switzerland?" : "Bern",
    "What is the capital of Spain?" : "Madrid", "What is the capital of Austria?" : "Vienna",
    "What is the capital of Belgium?" : "Brussels", "What is the capital of Portugal?" : "Lisbon",
    "What is the capital of Netherlands?" : "Amsterdam", "What is the capital of Germany?" : "Berlin"
}

#declaring quiz score by assuming the score is zero.
quiz_score = 0

#begin the coding for displaying the question by using the for loop.
for question, answer in questions.items(): #.items() is used to read all items within the dictionary.
    user = input(question + " ").strip() #.strip() is used to remove unnecessary whitespaces within codes.

    if user.casefold() == answer.casefold(): #.casefold() is used to avoid case sensitivity.
        print("Your answer is correct!")
        quiz_score += 1 #adds score when the user got the answer right.
    else:
        print("Your answer is incorrect. The correct answer is: ", answer)

#declare the final quiz score using f string:
print(f"You got {quiz_score} out of 10 correct!")
