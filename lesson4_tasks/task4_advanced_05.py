'''
Відомості про автомобіль складаються із назви марки, унікального номера авто та прізвища власника.
Словник формується наступним чином:
ключ - номер авто та значення - список із двох елементів [марка, прізвище власника].
Реалізуйте алгоритм пошуку прізвища власника за допомогою номера та виведіть статистику унікальних марок.
'''

autoBase = {
    'ST4423OA': ['BMV', 'Stinson'],
    'MB44231A': ['Mercedes', 'Mosby'],
    'IG44232A': ['Skoda', 'Scherbatsky'],
    'VG44233A': ['Honda', 'Aldrin'],
    'AK44234LT': ['Hundai', 'Eriksen'],
    'ME44235CK': ['BMV', 'Scherbatsky'],
    'VK44236Z': ['Skoda', 'Zinman'],
    'RS44237A': ['Skoda', 'Stinson'],
    'BS44238A': ['Mercedes', 'Stinson'],
    'RO44239A': ['Suzuki', 'Mosby'],
}

print('List of cars identify numbers:')
print('')
for i in autoBase:
    print(i, end ='\n')
while True:
    selected = input('Please, choose one of the list ')
    if selected in autoBase:
        print('Last name of car owner is '+autoBase[selected][1])
        break
    else:
        print('There is no car with this identify number')
        break
print('List of unique car brands:')

autoBrand = []
for i in autoBase:
    autoBrand.append(autoBase[i][0])
uniqueAutoBrand = set(autoBrand)
for i in uniqueAutoBrand:
    print(i)
