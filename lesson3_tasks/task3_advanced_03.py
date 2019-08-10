def NSD(first, second):
    while first != second:
        if first == 0 or second == 0:
            break
        elif first > second:
            first -= second
        else:
            second -= first
    nsd = first
    return nsd

print('Please, enter two positive whole numbers to find the greatest common divisor')
print('First number:')
dividend = int(input())
print('Second number:')
divisor = int(input())

nsd = NSD(dividend, divisor)

print('Fraction = '+str(dividend)+' / '+str(divisor))
if nsd == 1:
    print('Irreducible fraction')
elif nsd == 0:
    print('Dividend = 0')
else:
    new_div = dividend/nsd
    new_divis = divisor/nsd
    print('New fraction = '+str(int(new_div))+' / '+str(int(new_divis)))
