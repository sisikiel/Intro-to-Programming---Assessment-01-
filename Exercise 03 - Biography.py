#For exersice 3, we are tasked to create a program that displays my name, hometown, and age while using dictionary.
#Dictionaries are quite similar to lists, except it uses key-value pairs and curly braces instead of brackets.

#start the code by declaring the dictionary.
person_data = {"name" : "Sassykiel", "age" : 17, "Hometown" : "Camarines Sur"}
print(f"My name: {person_data["name"]}\nMy age: {person_data["age"]}\nMy Hometown: {person_data["Hometown"]} ")
    #the \n is used to separate multiple lines in one string.


print() #This is used to separate codes while running the program


#for advanced requirement, I have to ask the user for their datas (name, age, hometown).
user_name = input("Enter your name: ")
user_town = input("Enter your hometown: ")

while True: #while loop to ensure that the user inputs integer value (numbers).
    try:
        user_age = int(input("Enter your age: "))
        break
        #if the user types "eighteen" instead of 18, this will print out:
    except ValueError:
        print("Please enter a numerical value!")


#declare another dictionary that contains the user inputted data:
user_data = {"name" : user_name, "hometown" : user_town, "age" : user_age}
print(f"Your name: {user_data["name"]}\nYour hometown: {user_data["hometown"]}\nYour age: {user_data["age"]}")