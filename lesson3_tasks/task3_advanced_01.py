def NSD(first, second):
    while first != second:
        if first>second:
            first-=second
        else:
            second-=first
    nsd = first
    return nsd

print('Please, enter two positive whole numbers to find the greatest common divisor')
print('First number:')
first = int(input())
print('Second number:')
second = int(input())
nsd = NSD(first, second)
print(str(nsd))
