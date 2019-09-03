print('Please, add a pupil and his mark to the gradebook:')
print('')
pupilsDict = {}
exitCommand=''

pupilID=0
while True:
    lst = []
    pupil = input("Enter pupil name or type \'quit\' to exit: ")
    while not (pupil.isalpha() or pupil.lower() != 'quit'):
        pupil = input("Add correct name: ")
    if pupil.lower() == 'quit':
        pupil = None
        break
    else:
        lst.append(pupil)
    mark = input("Enter pupil mark: ")
    while not (mark.isdigit() or mark.lower() != 'quit'):
        mark = input("Add correct mark: ")
    if mark.lower() == 'quit':
        mark = None
        break
    else:
        lst.append(mark)
        pupilsDict[pupilID] = lst
    pupilID+=1
    check = input('type \'quit\' to exit the program or another symbol to continue')
    if check.lower() == 'quit':
        break
    else:
        continue

with open('gradebook.txt','w') as out:
    for key,val in pupilsDict.items():
        out.write('{}:{}\n'.format(key,val))

print('')
print('Pupils with mark < 7: ')
for i,j in pupilsDict.items():
    if int(j[1])<7:
        print(j[0])

avg_lst = []
print('')
print('Avg mark for class: ')
for i,j in pupilsDict.items():
    avg_lst.append(int(j[1]))
avgValue = sum(avg_lst) / len(avg_lst)
print(str(avgValue))
print('')

print('Performance stat {mark: count of mark}: ')
dict((i, avg_lst.count(i)) for i in avg_lst)