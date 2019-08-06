print('Let\'s try to find a solution to a quadratic equation of the form: ax²+bx+c = 0')
print('')
print('At first, please enter a coefficients of quadratic equation.\n'
      'Note, that \'a\' coefficient is not equal to 0 !')

def is_number(strg):
    is_number = True
    try:
        num = float(strg)
        is_number = num == num
    except ValueError:
        is_number = False
        num = False
    return is_number, num

print("Please, enter \'a\' coeff: ")
a = is_number(input())
while a[0] == False or a[1] == float(0):
    print("Please, enter correct \'a\' coeff: ")
    a = is_number(input())

print("Please, enter \'b\' coeff: ")
b = is_number(input())
while b[0] == False:
    print("Please, enter correct \'b\' coeff: ")
    b = is_number(input())

print("Please, enter \'c\' coeff: ")
c = is_number(input())
while c[0] == False:
    print("Please, enter correct \'c\' coeff: ")
    c = is_number(input())

b_help = '+'+str(b[1]) if b[1]>0 else str(b[1])
if c[1]==0:
    c_help = ''
elif c[1]<0:
    c_help = c[1]
else:
    c_help='+'+str(c[1])
print('Quadratic equation = '+str(a[1])+'x²'+b_help+'x'+c_help+'=0')

print('a = '+str(a[1]))
print('b = '+str(b[1]))
print('c = '+str(c[1]))

D = b[1]**2-4*a[1]*c[1]
print('Discriminant = ' + str(D))
if D < 0:
    print('No roots')
elif D == 0:
    x = round(-b[1] / (2 * a[1]),2)
    print('x = ' + str(x))
else:
    x1 = round((-b[1] + D ** 0.5) / (2 * a[1]),2)
    x2 = round((-b[1] - D ** 0.5) / (2 * a[1]),2)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))