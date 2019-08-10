print('Enter \'exit\' to exit the program')
while True:
    strg = input("Please, enter one of existent signs (+,-,*,/): ")
    if strg.upper() == 'EXIT':
        break
    elif strg in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if strg == '+':
            print("Result = " + str(x + y))
        elif strg == '-':
            print("Result = " + str(x - y))
        elif strg == '*':
            print("Result = " + str(x * y))
        elif strg == '/':
            print("Result = " + str(x / y))
    else:
        print("Please, add a correct sign")