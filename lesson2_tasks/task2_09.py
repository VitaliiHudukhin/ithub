def divisors(number):
    n = 1
    while(n < number):
        if(number % n==0):
            print(n)
        else:
            pass
        n += 1
    print(number)

a = 10
n = divisors(a)


