#import math

def is_number(strg):
    try:
        int(strg)
        if len(str(abs(int(strg)))) == 3:
            return int(strg)
        else:
            print("The number is float or isn't three-digit, try again")
            return False
    except ValueError:
        print("Entered data isn't the number, try again")
        return False

print("Please, enter a whole three-digit number: ")
number = is_number(input())

while number == False:
    print("Please, enter a correct (whole three-digit) number: ")
    number = is_number(input())
print("Entered number = "+str(number))
if number < 0:
    new_number = int('-'+str(abs(number))[::-1])
else:
    new_number = int(str(number)[::-1])
print("Result number = "+str(new_number))