from random import randint

petroNum = randint(1, 100)
print('Petro set number = '+str(petroNum))
print('')

dictionary = {"message": "Hello, World!"}

data = dictionary.get("ds")

olenaNums = {}
olenaAttempt = 1
goodAttempts = []

while True:
    print('Please, input whole numbers, separated with comma or type \'Exit\' to exit the program')
    numbers = input()
    numbers_list = numbers.split(',')
    if numbers.upper() == "HELP":
        for i in goodAttempts:
            print('You guessed the number in your ' +str(i)+' attempt with numbers: ')
            print(olenaNums[i])
        continue
    if numbers.upper() == "EXIT":
        False
        break
    if str(petroNum) in numbers_list:
        print('Yes')
        olenaNums[olenaAttempt]=numbers_list
        goodAttempts.append(olenaAttempt)
        olenaAttempt+=1
    else:
        print('No')
        olenaAttempt += 1
    continue