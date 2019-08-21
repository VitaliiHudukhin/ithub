import random
N = int(input('Please, add a length of country-city list'))
lst_lst = []
for i in range(N):
    lst = input('Please, add country at first and then add a cities of this country')
    lst_lst.append(lst.split())

M = int(input('Please, add a length of city list'))
city_values = []
for i in range(M):
    rnd_list = random.randint(0, len(lst_lst)-1)
    rnd_val = random.choice(lst_lst[rnd_list][1:])
    print(rnd_val)
    city_values.append(rnd_val)
print('')
for i in city_values:
    for j in lst_lst:
        result = 1 if i in j else 0
        if result == 1:
            print(j[0])
        else:
            pass