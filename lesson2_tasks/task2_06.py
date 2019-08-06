
def station_select(strg):
    checker = True
    stationsList = ['A', 'B', 'C', 'D', 'E']
    if strg in stationsList:
        print('You have chosen \''+strg+'\' station')
        checker = True
    elif strg == 'EXIT':
        print('You have left the station selection')
        checker = True
    else:
        print('Please, choose a correct station')
        checker = False
    return checker

print('Please, choose a station (A-E). For exit the program, please type \'EXIT\'')
station = station_select(input().upper())
while station == False:
    print('For exit the program, please type \'EXIT\'')
    station = station_select(input().upper())