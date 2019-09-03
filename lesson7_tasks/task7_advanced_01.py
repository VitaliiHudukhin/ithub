'''Задача 1
Відкрийте файл Queen.txt. Проведіть аналіз тексту.
1. Розрахуйте кількість куплетів(куплети відрізняються знаком \n).
2. Визначте кількість рядків у кожному куплеті.
3. Порахуйте кількість слів у тексті.
5. Виведіть статистику найбільш уживаних слів тексту.
6. Передбачте розробку текстового інтерфейсу для виконання перших 5 завдань.'''

ddir = 'D:\\GVV_Viseven\\ITHUB\\lesson7_tasks\\'
fileName = 'Queen.txt'
file1 = open(ddir+fileName,'r+')

data = file1.read()
strings = data.count('\n')

counter = 0
strInCouplets = {}
for line in data.split('\n'):
    if line != '':

    if line == '':
        counter+=1


for i in range(counter):
