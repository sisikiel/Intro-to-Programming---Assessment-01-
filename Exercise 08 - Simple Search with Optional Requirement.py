#declare the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#declare the defaulted input
search_default = "Sam"

#ask if the user wants to input the user default search:
user_input = input("(yes/no) Would you like to enter a search term? ")

if user_input.casefold() == "yes": #.casefold() is for case sensitivity.
    new_search_default = input("Enter the name that you are looking for: ")
else:
   new_search_default = search_default

#we then print out the desired outcomes:
if new_search_default in names:
    print(f"The name {new_search_default} was found on the list!")
else:
    print(f"the name {new_search_default} was not found on the list.")