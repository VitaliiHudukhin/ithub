#*****************************#

def is_int(strg):
    try:
        int(strg)
        if int(strg) > 0:
            return int(strg)
    except ValueError:
        print("Entered data isn't int")

print("Please, enter an int number (rows): ")

rows = is_int(input())
while rows == None:
    print("Please, enter correct number: ")
    rows = is_int(input())

print("Please, enter an int number (columns): ")
columns = is_int(input())
while columns == None:
    print("Please, enter correct number: ")
    columns = is_int(input())

arr = []
for i in range(rows):
    row = [int(j) for j in input('Enter only int numbers').split()]
    while len(row) != columns:
        row = [int(j) for j in input('Enter correct row with '+str(columns)+' elements').split()]
    arr.append(row)

checkList = []
for i in range(len(arr)):
    lenOfArr = len(arr[i])
    for j in range(lenOfArr // 2):
        checkList.append(arr[i][j] == arr[i][lenOfArr-1-j])

if False in checkList:
    print('Entered array isn\'t vertical symmetric')
else:
    print('Entered array is vertical symmetric')
