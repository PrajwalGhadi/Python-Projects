#Program for Health Manangement

# Steps to do - 1 Create 6 files which will contain Exercise and FoodEated
# 2 6 files must be of Three different peoples
# 3 Get the input from the  user to update the Exercise or FoodEated file
# 4 Take input as 1, 2, 3 for Three different peoples
# 5 Write the contain in respected files

def getDate():
    import datetime
    return datetime.datetime.now()

def getData(k):
    if k == 1:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c == 1:
            n = input("Enter the name of Exercise : ")

            with open("PratikExc.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the Exercise  of Pratik ...")
        elif c == 2:
            n = input("Enter the name of Food : ")

            with open("PratikFood.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the FoodDetail of Pratik ...")
        else:
            print("Please Enter 1(Exercise) and 2(FoodDetail)")
    elif k == 2:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c== 1:
            n = input("Enter the name of Exercise : ")

            with open("PrajwalExc.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the Exercise of Prajwal ...")
        elif c == 2:
            n = input("Enter the name of Food : ")

            with open("PrajwalFood.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the FoodDetail of Prajwal ...")
    elif k == 3:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c == 1:
            n = input("Enter the name of Exercise : ")

            with open("RutujaExc.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the Exercise of Rutuja ...")
        elif c == 2:
            n = input("Enter the name of Food : ")

            with open("RutujaFood.txt", "a") as op:
                op.write("["+ str(getDate()) + "]" + " " +n)
                op.write("\n")
                print("Successfully Added to the FoodDetail of Rutuja ...")
    else:
        print("Please enter 1(Pratik), 2(Prajwal), 3(Rutuja) : " )
    return


def retrive_Data(k):
    if k == 1:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c == 1:
            with open("PratikExc.txt") as op:
                print("\nHello Your Reading the Pratik Exercise ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
        elif c == 2:
            with open("PratikFood.txt") as op:
                print("\nHello Your Reading the Pratik Food ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
        else:
            print("Please Enter 1(Exercise) and 2(FoodDetail)")
    elif k == 2:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c == 1:
            with open("PrajwalExc.txt") as op:
                print("\nHello Your Reading the Prajwal Exercise ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
        elif c == 2:
            with open("PrajwalFood.txt") as op:
                print("\nHello Your Reading the Prajwal Food ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
    elif k == 3:
        c = int(input("Enter (1 for Exercise )and (2 for Food) : "))
        if c == 1:
            with open("RutujaExc.txt") as op:
                print("\nHello Your Reading the Rutuja Exercise ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
        elif c == 2:
            with open("RutujaFood.txt") as op:
                print("\nHello Your Reading the Rutuja Food ...\n")
                print(op.read())
                print("Thanks for Reading Hope you enjoyed it ...")
    else:
        print("Please enter 1(Pratik), 2(Prajwal), 3(Rutuja) : ")
    return

print(''' Hello Welcome to Health Management
        If you want to Add Exercise or FoodDetail in file just enter 1, 2 or 3
        1 is to Enter the details in Pratik's ...
        2 is to Enter the details in Prajwal's ...
        3 is to Enter the details in Rutuja's ... ''')

k = int(input("Enter Pratik(1), Prajwal(2), Rutuja(3) : "))

a = input("To Add Data(add) Or Read The Data(read) : ")

if a == "add":
    getData(k)
elif a == "read":
    print(retrive_Data(k))




