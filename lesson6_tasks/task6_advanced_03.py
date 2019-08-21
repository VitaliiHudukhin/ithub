from pathlib import Path

ddir_home = str(Path.home())

#file = open(ddir_home+'\\user_info.txt')
with open(ddir_home+'\\user_info.txt') as reader:
    file = reader.read()
    print(file)
lst = file.split('\n')
lst_lst = []
for i in lst:
    lst_lst.append(i.split())

print('Valuable commands in this program: ')
valuableCommands = ['find user','exit']
for i in valuableCommands:
    print(i)
inputData = ""
while inputData.lower() != 'exit':
    inputData = input('Please, enter one of the valuable command: ')
    if inputData == 'find user':
        phone = input('Please input phone in format: +79998887766')
        flag = 0
        for i in lst_lst:
            if phone in i:
                flag = phone
                print(i[0])
        if flag == 0:
            print('Phone not in list')
    else:
        print("You inputed unknown command.")
    continue