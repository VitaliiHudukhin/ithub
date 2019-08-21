S = 'st\'st'
S1 = 'st\"'
S2 = 'str1\nstr2'  #аналогично с табуляцией в строке покажется как текст, но при принте - учтется перенос/табуляция
S_ct = 'str1'+'str2'
SS = S[0:3]

for i in S_ct:
    print(i, end =' ') # полезно

S_ct.find('s') # -1 вернет если какая-то ошибка, index и rindex возвращает вместо -1 исключение ValueError

# ord() и chr() - коды ASCII таблицы

lst_num = list(map(int,(input("Введіть список чисел:").split(' '))))
print(lst_num)

print("=============EOF==============")

lst_num1 = [int(i) for i in input("Введіть список чисел \n").split()]
print(lst_num1)

