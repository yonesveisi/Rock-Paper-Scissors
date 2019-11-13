# programmer : younes veisi
import random
Points = 0
while 1:
    System_choice = random.randint(1, 3)
    System_choice_random = ""
    print("Points : ", +Points)
    print("System_choice_random : ", System_choice_random)
    Choice = int(input("1- Rock \n2- Paper \n3- Scissors \n""Please enter your guess: "))
    if Choice == 0:
        break
    elif (Choice != 1) and (Choice != 2) and (Choice != 3):
        print("Your Choice Is Wrong")
        break
    if System_choice == 1:
        System_choice_random = "Rock"
    elif System_choice == 2:
        System_choice_random = "Paper"
    elif System_choice == 3:
        System_choice_random = "Scissors"
    if (System_choice == 1 and Choice == 2) or (System_choice == 2 and Choice == 3) or (System_choice == 3 and Choice == 1):
        print("You Win !!!")
        Points += 1
    elif System_choice == Choice:
        print("You are Equal !!!")
    else:
        print("You lost !!!")
        Points -= 1
        print("----------------------------------------------")
