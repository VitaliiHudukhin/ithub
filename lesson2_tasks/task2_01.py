print('Let\'s try to find a max number of three given')
#проверяем число на float
#проверяем число на nan, если ошибка - False
def is_number(strg):
    is_number = True
    try:
        num = float(strg)
        is_number = num == num
    except ValueError:
        is_number = False
        num = False
    return is_number, num

print("Please, enter a first number: ")
first = is_number(input())
while first[0] == False:
    print("Please, enter a correct first number: ")
    first = is_number(input())
print("Please, enter a second number: ")
second = is_number(input())
while second[0] == False:
    print("Please, enter a correct second number: ")
    second = is_number(input())
print("Please, enter a third number: ")
third = is_number(input())
while third[0] == False:
    print("Please, enter a correct third number: ")
    third = is_number(input())

print('The max number = '+str(max(first[1],second[1], third[1])))
