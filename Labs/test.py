# def selectAnimal(listAnimals):
#     true = True
#     while true:
#         ani = int(input("Please select an animal from the list (enter the 1-5): "))
#         if ani == 1:
#             return listAnimals[0]
#         elif ani == 2:
#             return listAnimals[1]
#         elif ani == 3:
#             return listAnimals[2]
#         elif ani == 4:
#             return listAnimals[3]
#         elif ani == 5:
#             return listAnimals[4]
#         print("Invalid input, please try again!")
#
# def selectAnimal(listAnimals):
#     true = True
#     index = 0
#     while true:
#         ani = int(input("Please select an animal from the list (enter the 1-5): "))
#         if ani == 1:
#             true = False
#         elif ani == 2:
#             index = 1
#             true = False
#         elif ani == 3:
#             index = 1
#             true = False
#         elif ani == 4:
#             index = 1
#             true = False
#         elif ani == 5:
#             index = 1
#             true = False
#         print("Invalid input, please try again!")
#
#     return listAnimals[index]

listAnimals = ["Bunny","French Bulldog","Cat","Turtle","Labrador"]
true = True
index = 0
while true:
    ani = int(input("Please select an animal from the list (enter the 1-5): "))
    if ani == "1":
        true = False
    elif ani == "2":
        index = 1
        true = False
    elif ani == "3":
        index = 2
        true = False
    elif ani == "4":
        index = 3
        true = False
    elif ani == "5":
        index = 4
        true = False
    else:
        print("Invalid input, please try again!")

print(listAnimals[index])