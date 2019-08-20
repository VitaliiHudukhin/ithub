'''
Для кодування повідомлень Френсіс Бекон запропонував кожну літеру тексту замінювати на групу з п'яти символів
«А» або «B» (назвемо їх "ab-групами"). Для співставлення літер і кодуючих ab-груп
в даному завданні використовується ключ-ланцюжок aaaaabbbbbabbbaabbababbaaababaab,
в якому порядковий номер літери відповідає порядковому номеру початку ab-групи.

Наприклад: літера "а" - перша літера алфавіту; для визначення її коду беремо 5 символів з ключа,
починаючи з першого: aaaaa. Літера "c" - третя в алфавіті, отже для визначення її коду беремо 5 символів з ключа,
починаючи з третього: aaabb.

Наприклад, початкове повідомлення - Prometheus.
'''

import string
import re
mainKey = 'aaaaabbbbbabbbaabbababbaaababaab'
textData = input('Please input some text data')
#textData = textData.replace(' ','')
textData = re.sub("([^\w]|[\d_])+", " ", textData)
textData = textData.replace(' ','')
numOfSymb = 5
textDataDelim = [textData[i:i+numOfSymb] for i in range(0, len(textData), numOfSymb)]
for i in textDataDelim:
    if len(i) < 5:
        textDataDelim.remove(i)
print(textDataDelim)

textDataDelimConvert = []
indexOf = 0
workString = ''
for i, j in enumerate(textDataDelim):
    for l, k in enumerate(j):
        if k.isupper() == True:
            workString += 'a'
        else:
            workString += 'b'
        if l == 4:
            textDataDelimConvert.append(workString)
            workString = ''

for i in textDataDelimConvert:
    val = mainKey.find(i)
    letter = chr(val+96)
    print(letter)

