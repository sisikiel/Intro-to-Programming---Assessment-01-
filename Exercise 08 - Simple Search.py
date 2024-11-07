#exercise 08

#make a list for the names.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#the default search name:
search_default = "Sam"

#start the code for searching names
if search_default in names:
    print(f"The name {search_default} is on the list!")
else:
    print(f"The name {search_default} is not on the list")