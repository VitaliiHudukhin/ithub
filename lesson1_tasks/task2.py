from math import sqrt
def is_number(strg):
    try:
        float(strg)
        if float(strg) > 0:
            return float(strg)
        else:
            print("The number is < or == 0, try again")
            return False
    except ValueError:
        print("Entered data isn't the number, try again")
        return False

print("Please, enter a radius for first planet: ")
radius1 = is_number(input())
print("Please, enter a rotation period for first planet: ")
period1 = is_number(input())
print("Please, enter a radius for second planet: ")
radius2 = is_number(input())
while radius1 == False or period1 == False or radius2 == False:
    print("Please, enter a correct radius for first planet: ")
    radius1 = is_number(input())
    print("Please, enter a correct rotation period for first planet: ")
    period1 = is_number(input())
    print("Please, enter a correct radius for second planet: ")
    radius2 = is_number(input())

period2 = sqrt(period1**2 * radius2**3 / radius1**3)
print('Rotation period for second planet = '+str(period2))