
def is_int(strg):
    try:
        int(strg)
        return int(strg)
    except ValueError:
        print("Entered data isn't int")

print("Please, enter an int number: ")
number = is_int(input())
while number == None:
    print("Please, enter correct number: ")
    number = is_int(input())

isPositive = True if number >= 0 else False
if isPositive == True:
    start = 0
    end = number
else:
    start = number
    end = 0

listOfPaired = []
for i in range(start,end):
    if i % 2 == 0:
        listOfPaired.append(i)
sumOfPaired = sum(listOfPaired)
print('You entered number '+str(number))
print('')
print('Sum of paired numbers, which < '+str(number)+' is '+str(sumOfPaired))