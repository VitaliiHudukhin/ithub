print('Let\'s find factorial of entered number')

def factor(n):
    factorial = 1
    if n == 1:
        return factorial
    elif n <1:
        factorial = 'Bad input data'
    else:
        for i in range(2, n + 1):
            factorial *= i
    return factorial
n = factor(int(input()))
print('Result is '+str(n))