
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

print("Please, enter a triangle square: ")
triangleSquare = is_number(input())
print("Please, enter a triangle base: ")
triangleBase = is_number(input())
while triangleSquare == False or triangleBase == False:
    print("Please, enter a correct triangle square: ")
    triangleSquare = is_number(input())
    print("Please, enter a correct triangle base: ")
    triangleBase = is_number(input())

'''
h: int()
H = 2*triangleSquare/(h+triangleBase)
quadraticEquation = 0
quadraticEquation = H**2+triangleBase*H-2*triangleSquare
'''
a = 1
b = triangleBase
c = -2*triangleSquare
print('a = '+str(a))
print('b = '+str(b))
print('c = '+str(c))

D = b**2-4*a*c
print('Discriminant = ' + str(D))
if D < 0:
    print('No roots')
elif D == 0:
    x = round(-b / (2 * a),2)
    print('x = ' + str(x))
else:
    x1 = round((-b + D ** 0.5) / (2 * a),2)
    x2 = round((-b - D ** 0.5) / (2 * a),2)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))

