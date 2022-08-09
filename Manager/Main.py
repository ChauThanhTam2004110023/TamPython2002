from method import *

option = '''1. AddStudent
\n 2. RemoveStudent
\n 3. FindStudent
\n 4. UpdateStudent
\n 5. ViewStudent
\n 6. Exit'''

actionOptional = dict()
actionOptional["1"] = addStudent
actionOptional["2"] = removeStudent
actionOptional["3"] = findStudent
actionOptional["4"] = updataStudent
actionOptional["5"] = viewStudent

print("Welcome to manager student program")
while True:
    print(option)
    print("Please enter your option: ", end=" ")
    option = input()
    if option == "6":
        print("Thanks for program")
        break
    if option not in actionOptional:
        print("No match with any action")
    else:
        actionOptional[option]()