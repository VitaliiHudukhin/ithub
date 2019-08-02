import math

#-------------------------- check the numeric values  -----------------------------------------------#
def is_number(strg):
    try:
        float(strg)
        return float(strg)
    except ValueError:
        print("Entered data isn't the number, try again")
        return False
#-------------------------- enter a correct coordinates ----------------------------------------------#
while True:
    print("Please, enter a coordinates of A point: ")
    print("Ax:")
    Ax = is_number(input())
    print("Ay:")
    Ay = is_number(input())
    while Ax == False or Ay == False:
        print("Please, enter a correct Ax coordinate: ")
        Ax = is_number(input())
        print("Please, enter a correct Ay coordinate: ")
        Ay = is_number(input())
    A = [Ax, Ay]
    print("Please, enter a coordinates of B point: ")
    print("Bx:")
    Bx = is_number(input())
    print("By:")
    By = is_number(input())
    while Bx == False or By == False:
        print("Please, enter a correct Bx coordinate: ")
        Bx = is_number(input())
        print("Please, enter a correct By coordinate: ")
        By = is_number(input())
    B = [Bx, By]
    print("Please, enter a coordinates of C point: ")
    print("Cx:")
    Cx = is_number(input())
    print("Cy:")
    Cy = is_number(input())
    while Cx == False or Cy == False:
        print("Please, enter a correct Cx coordinate: ")
        Cx = is_number(input())
        print("Please, enter a correct Cy coordinate: ")
        Cy = is_number(input())
    C = [Cx, Cy]
    if Ay == By == Cy or Ax == Bx == Cx:
        print('Your X or Y coordinates is on one line, please enter another coordinates')
        True
    else:
        break
points_coords = {'A':A, 'B':B, 'C':C}


#-------------------------- find length of potential diagonal  -----------------------------------------------#
diagonalAB = diagonalBA = math.sqrt(pow((Ax-Bx),2) + pow((Ay-By),2))
diagonalAC = diagonalCA = math.sqrt(pow((Ax-Cx),2) + pow((Ay-Cy),2))
diagonalBC = diagonalCB = math.sqrt(pow((Bx-Cx),2) + pow((By-Cy),2))

#-------------------------- find square of parallelogramm -----------------------#
S = abs((Bx-Ax)*(Cy-Ay) - (Cx-Ax)*(By-Ay))
#print('Square of parallelogramm = '+ str(S))

#-------------------------- choose a diagonal of the parallelogramm -------------#
print('Select a diagonal of parallelogramm. Please, enter AB or BA, AC or CA, BC or CB only: ')

def diagonal_check(diagonal):
    if diagonal == 'AB' or diagonal == 'BA':
        diagonal_len = diagonalAB
        diagonal_name = diagonal
    elif diagonal == 'AC' or diagonal == 'CA':
        diagonal_len = diagonalAC
        diagonal_name = diagonal
    elif diagonal == 'BC' or diagonal == 'CB':
        diagonal_len = diagonalBC
        diagonal_name = diagonal
    else:
        diagonal_name = False
        diagonal_len = False
    return diagonal_len, diagonal_name

diagonal1 = diagonal_check(input())
while diagonal1 == (False, False):
    print("Please, enter a correct diagonal (AB or BA, AC or CA, BC or CB): ")
    diagonal1 = diagonal_check(input())
diagonal_name = diagonal1[1]

print('Diagonal is '+diagonal_name)
print('')

#-------------------------- find intersection point - middle of diagonals ----------------------------#

for i in points_coords:
    if diagonal1[1][0] == i:
        point1_x = points_coords[i][0]
        point1_y = points_coords[i][1]
        break
    else:
        False

for j in points_coords:
    if diagonal1[1][1] == j:
        point2_x = points_coords[j][0]
        point2_y = points_coords[j][1]
        break
    else:
        False

Mx = (point1_x+point2_x)/2
My = (point1_y+point2_y)/2

print('M (intersection) point has coordinates: X = ' +str(Mx)+' and coordinate Y = '+str(My))

find_help_point = points_coords.copy()
del find_help_point[diagonal1[1][0]]
del find_help_point[diagonal1[1][1]]
help_point = list(find_help_point)[0]

#-------------------------- find coords of 4th point -----------------------------------------------#
Dx = 2*Mx-find_help_point[help_point][0]
Dy = 2*My-find_help_point[help_point][1]

print('4th point of parallelogramm (D point) has coordinate X = ' +str(Dx)+' and coordinate Y = '+str(Dy))

#-------------------------- find the lengths of another sides of parallelogramm --------------------#
diagonalAD = diagonalDA = math.sqrt(pow((Ax-Dx),2) + pow((Ay-Dy),2))
diagonalBD = diagonalDB = math.sqrt(pow((Bx-Dx),2) + pow((By-Dy),2))
diagonalCD = diagonalDC = math.sqrt(pow((Cx-Dx),2) + pow((Cy-Dy),2))

#-------------------------- determine the second diagonal (accords to the first diagonal) ----------#
def diagonals_length(diagonal_name):
    if diagonal_name == 'AB' or diagonal_name == 'BA':
        diagonal_len2 = diagonalCD
        diagonal_name2 = 'CD'
    elif diagonal_name == 'AC' or diagonal_name == 'CA':
        diagonal_len2 = diagonalBD
        diagonal_name2 = 'BD'
    elif diagonal_name == 'BC' or diagonal_name == 'CB':
        diagonal_len2 = diagonalAD
        diagonal_name2 = 'AD'
    else:
        diagonal_name2 = False
        diagonal_len2 = False
    return diagonal_len2, diagonal_name2

diagonal2 = diagonals_length(diagonal_name)

#-------------------------- result block -----------------------------------------------#
print('Square of parallelogramm = '+ str(S)+' (sm²)')
print('Diagonal_1 is '+diagonal1[1]+' with length = '+str(round(diagonal1[0],3))+' (sm)')
print('Diagonal_2 is '+diagonal2[1]+' with length = '+str(round(diagonal2[0],3))+' (sm)')