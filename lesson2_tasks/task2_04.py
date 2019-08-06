print('Please, enter whole positive number, which equals to number of day of week to see the schedule')
print('Monday = 1\nTuesday = 2\nWednesday = 3\nThursday = 4\nFriday = 5\nSaturday = 6\nSunday = 7')
def is_number(strg):
    try:
        int(strg)
        if int(strg) > 0 and int(strg) <=7:
            return int(strg)
        else:
            print("The number is < 1 or > 7, try again")
            return False
    except ValueError:
        print("Entered data isn't the whole positive number, try again")
        return False

print("Please, enter a number which equals to day of week: ")
a = is_number(input())
while a == False:
    print("Please, enter correct number: ")
    a = is_number(input())

scheduleDict = {
    1: {'Monday': [
        'Breakfast',
        'Work',
        'Dinner',
        'Gym',
        'Supper',
        'Movie watching',
        'Sleep'
    ]},
    2: {'Tuesday': [
        'Breakfast',
        'Work',
        'Dinner',
        'Gym'
        'Supper',
        'Movie watching',
        'Sleep'
    ]},
    3: {'Wednesday': [
        'Breakfast',
        'Work',
        'Dinner',
        'Python courses',
        'Supper',
        'Sleep'
    ]},
    4: {'Thursday': [
        'Breakfast',
        'Work',
        'Dinner',
        'Work',
        'Supper',
        'Sleep'
    ]},
    5: {'Friday': [
        'Breakfast',
        'Work',
        'Dinner',
        'Work',
        'Supper',
        'Meet with friends',
        'Sleep'
    ]},
    6: {'Saturday': [
        'Breakfast',
        'Sleep',
        'Python courses',
        'Meet with friends'
    ]},
    7: {'Sunday': [
        'Breakfast',
        'Sleep',
        'Dinner',
        'Homework (python courses)',
        'Sleep'
    ]},
}

for k in scheduleDict:
    if k == a:
        for key in scheduleDict[k]:
            print(key+':')
            counter = 1
            for val in scheduleDict[k][key]:
                print(str(counter)+'. '+val )
                counter+=1
    else:
        pass