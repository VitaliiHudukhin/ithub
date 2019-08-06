import math
print("Please, enter sides of triangle")

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

print("First side: ")
first = is_number(input())
while first == False:
    print("Please, enter a correct first number: ")
    first = is_number(input())
print("Second side: ")
second = is_number(input())
while second == False:
    print("Please, enter a correct second number: ")
    second = is_number(input())
print("Third side: ")
third = is_number(input())
while third == False:
    print("Please, enter a correct third number: ")
    third = is_number(input())

def triangle_exist(a, b, c):
    check = True
    if a + b > c and a + c > b and b + c > a:
        print("Triangle exists")
        check = True
    else:
        print("Triangle does not exist")
        check = False
        quit()
    return check
trianExistCheck = triangle_exist(first, second, third)
if trianExistCheck == True:
    PP = (first+second+third)/2
    print('Half of perimeter = '+str(PP))
    S = math.sqrt(PP*(PP-first)*(PP-second)*(PP-third))
    print('Square of triangle (by Geron) = ' + str(S))
    smallestSide = min(first, second, third)
    Hfirst = 2 * S / first
    Hsecond = 2 * S / second
    Hthird = 2 * S / third
    print('Height to first side = '+str(Hfirst))
    print('Height to second side = ' + str(Hsecond))
    print('Height to third side = ' + str(Hthird))
    H = 2*S/smallestSide
    print('Highest height = '+str(H))
else:
    print('Sorry, try another time')
