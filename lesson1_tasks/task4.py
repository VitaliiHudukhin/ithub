#import math

def is_number(strg):
    try:
        int(strg)
        if len(str(abs(int(strg)))) == 4:
            return int(strg)
        else:
            print("The number is float or isn't four-digit, try again")
            return False
    except ValueError:
        print("Entered data isn't the number, try again")
        return False

print("Please, enter a whole four-digit number: ")
number = is_number(input())

while number == False:
    print("Please, enter a correct (whole four-digit) number: ")
    number = is_number(input())
print("Entered number = "+str(number))
if number < 0:
    new_number = int(str(number)[1])%int(str(number)[4])
else:
    new_number = int(str(number)[0])%int(str(number)[3])
print("Remainder of division = "+str(new_number))
