print('Please, enter whole positive number, more than 1:')
def is_number(strg):
    try:
        int(strg)
        if int(strg) > 1:
            return int(strg)
        else:
            print("The number is < or == 1, try again")
            return False
    except ValueError:
        print("Entered data isn't the number, try again")
        return False

print("Please, enter \'a\' number: ")
a = is_number(input())
while a == False:
    print("Please, enter correct \'a\' number: ")
    a = is_number(input())
print('All paired integers from 1 to '+str(a)+' (include):')
for i in range(1, a+1):
    if i % 2 == 0:
        print(i)
    else:
        pass

