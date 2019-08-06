
import math
print('Please, enter whole positive number, more than 1:')

def is_prime(n):
    if n < 2:
        print("A number must be 2 and more")
        quit()
    elif n == 2:
        print("It's prime number")
        quit()
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            print("This is composite number")
            quit()
        i += 1
    print("It's prime number")


n = is_prime(int(input()))