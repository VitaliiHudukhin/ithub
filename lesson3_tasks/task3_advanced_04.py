import random

print('Game Stone, Scissors, Paper start')
print('')

humanChoiceNum = ''
humanCounter = 0
computerCounter = 0
drawCounter = 0
while humanChoiceNum.upper() != "EXIT":
    computerChoiceNum = random.randint(1, 3)
    if computerChoiceNum == 1:
        computerChoice = "Stone"
    elif computerChoiceNum == 2:
        computerChoice = "Scissors"
    else:
        computerChoice = "Paper"

    humanChoiceNum = input("Please, enter 1 for Stone, 2 for Scissors, 3 for Paper or \'exit\' to exit the program: ")
    while not (humanChoiceNum.upper() == 'EXIT' or humanChoiceNum.upper() == '1'
               or humanChoiceNum.upper() == '2' or humanChoiceNum.upper() == '3'):
        humanChoiceNum = input("Enter 1 for Stone, 2 for Scissors, 3 for Paper: ")
    if humanChoiceNum.upper() == 'EXIT':
        break
    elif humanChoiceNum == '1':
        print("")
        print("You choose Stone")
        print("Computer choose " + computerChoice)
        print("")
        if computerChoiceNum == 1:
            print("Draw")
            drawCounter+=1
        elif computerChoiceNum == 2:
            print("You win!")
            humanCounter+=1
        else:
            print("You Lose!")
            computerCounter+=1
            print("")

    elif humanChoiceNum == '2':
        print("")
        print("You choose Scissors")
        print("Computer choose " + computerChoice)
        print("")
        if computerChoiceNum == 1:
            print("You Lose!")
            computerCounter += 1
        elif computerChoiceNum == 2:
            print("Draw")
            drawCounter += 1
        else:
            print("You win!")
            humanCounter += 1
            print("")

    elif humanChoiceNum == '3':
        print("")
        print("You choose Paper")
        print("Computer choose " + computerChoice)
        print("")
        if computerChoiceNum == 1:
            print("You win!")
            humanCounter += 1
        elif computerChoiceNum == 2:
            print("You Lose!")
            computerCounter += 1
        else:
            print("Draw")
            drawCounter += 1
            print("")
    else:
        print("Please, add a correct sign")
print('Human won '+ str(humanCounter)+' times')
print('Computer won '+ str(computerCounter)+' times')
print('Draw was '+ str(drawCounter)+' times')
