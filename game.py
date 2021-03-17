#Program to Snake, Water, Gun

"""
Logic to implement is -
step1 - Create a list containing Snake, Water, Gun
Step2 - Create the Chance given to user
step3 - create counter to calculate
"""
import random


print('''You are Playing Snake, Water or Gun Game !!!
         RULES : 
         1. If you and Computer are same then its tie ...
         2. In fight of Snake and Water --  Snake wins 
         3. In fight of Snake and Gun -- Gun wins
         4. In fight of Water and Gun -- Water wins \n''')


lst = ['s', 'w', 'g']   #This list is used to Take randomly snake water or gun

chances = 5
Computer_Points = 0  #This is an counter for calculate Computer points
User_Points = 0   #This is an counter for Calculate User points


def game():
    user_name = input('Enter Your Name: ')
    for i in range(chances):

        User = input("Enter the Values : \n 's' for Snake \n 'w' for water \n 'g' for gun \n")
        Computer = random.choice(lst)

        if User == Computer:
            print("OOPS, That was Tie !!")

    # This loop is use for calculating The comparison of Snake with Water & Gun
        elif User == "s" and Computer == "w":
            User_Points = User_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")
        elif User == "s" and Computer == "g":
            Computer_Points = Computer_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")

    # This loop is use for calculating The comparison of Water with Gun & Snake
        elif User == "w" and Computer == "g":
            User_Points = User_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")
        elif User == "w" and Computer == "s":
            Computer_Points = Computer_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")

        # This loop is use for calculating The Comparison of Gun with Water & Snake
        elif User == "g" and Computer == "s":
            User_Points = User_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")
        elif User == "g" and Computer == "w":
            Computer_Points = Computer_Points + 1
            print(f"Hey {user_name}, You won this one...")
            print(f"{user_name} your Current Score is : {User_Points}")
        else:
            print("Please Enter Proper Values : ")


print("\nGame Over !!!\n")

# This if statement are use for showing full result of game
if Computer_Points < User_Points:
    print(f"{user_name} Your Score is : {User_Points} \n Computer Score is : {Computer_Points} \n ")
    print("You Won This Game!! ")
elif Computer_Points > User_Points:
    print(f"Computer Score is : {Computer_Points} \n {user_name} Your Score is : {User_Points}")
    print("You Lose This Game Try again !!!")

for_continue = input('Do You Want to Continue please Select Y/N :')

if for_continue == 'Y':

    game()

elif for_continue == 'N':
    print('Thanks for Coming !!!')

else:
    print("Value Error")

