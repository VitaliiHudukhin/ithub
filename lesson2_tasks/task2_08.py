
import math
print('Please, enter whole positive number, more than 1:')

def is_prime(n):
    or_prime = 'Prime'
    if n < 2:
        print("A number must be 2 and more")
        or_prime = 'Composite'

    elif n == 2:
        pass
    i = 2
    limit = n//2 #int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            or_prime = 'Composite'
        i += 1
    return or_prime, n

n = is_prime(int(input()))

if n[0] == 'Composite':
    print('You entered composite number')
else:
    for i in range (n[1],1, -1):
        if is_prime(i) == ('Prime',i):
            print(i)