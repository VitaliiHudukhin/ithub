from random import random,randint
school = {
    '1A': 30,
    '1B': 30,
    '2B': 25,
    '6B': 31,
    '7C': 33,
}
print('Valuable commands in this program: ')
valuableCommands = ['change number','new class','delete class','total amount','exit']
for i in valuableCommands:
    print(i)
inputData = ""
#пока не введено exit программа продолжается
while inputData.lower() != 'exit':
    inputData = input('Please, enter one of the valuable command: ')
    if inputData == 'change number':
        #рэндомный класс из school
        classRandSelect = randint(0,5)
        #рэндомное число которое прибавлю к количеству учеников
        classRandChange = randint(-5,5)
        # выбранный рэндомно класс прибавляю выбранное рэндомное число учеников
        school[list(school.keys())[classRandSelect]]+=classRandChange
        print('In '+list(school.keys())[classRandSelect]+' class now '
              +str(school[list(school.keys())[classRandSelect]])+' pupils')
        continue
    elif inputData == 'new class':
        newClassName = input('Please, add a new class name ')
        if newClassName not in school:
            newClassPupilsCount = randint(25,36)
            school.update({newClassName:newClassPupilsCount})
            print(newClassName+' class with '+str(newClassPupilsCount)
                  +' pupils was added to school')
        continue
    elif inputData == 'delete class':
        print(school.keys())
        delClassName = input('Please, delete class by name ')
        if delClassName in school:
            del school[delClassName]
            print(delClassName + ' class was deleted')
        continue
    elif inputData == 'total amount':
        print('Total amount of school pupils is '+ str(sum(list(school.values()))))
    else:
        print("You inputed unknown command.")
    continue

print('Thanks for your attention!')