

def fibonacci(n):
    fib1 = 0
    fib2 = 1
    if n == 1:
        return 0
    elif n < 1:
        print('Sorry, program checks only positive Fibonacci sequence numbers')
        return False
    counter = 1
    while counter < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        counter += 1
    return fib_sum

number = int(input())
fib_value = fibonacci(number)
print(str(number)+'th Fibonacci number is '+str(fib_value))