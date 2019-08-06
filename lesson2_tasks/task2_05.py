print('Please, enter whole positive number in range 1-7, which equals to number of color in the rainbow')
print('Red = 1\nOrange = 2\nYellow = 3\nGreen = 4\nLightBlue = 5\nBlue = 6\nViolet = 7')
def is_number(strg):
    try:
        float(strg)
        return float(strg)
    except ValueError:
        print("Entered data isn't the number, try again")
        return False

color = is_number(input())
while color == False:
    print("Please, enter the number: ")
    color = is_number(input())

rainbow_dict = {
    1: 'Red',
    2: 'Orange',
    3: 'Yellow',
    4: 'Green',
    5: 'LightBlue',
    6: 'Blue',
    7: 'Violet'
}

if color in rainbow_dict:
    print('Entered number = '+str(color)+', which equals to '+rainbow_dict[color]+' color')
else:
    print('Error: entered number is not in range 1-7')