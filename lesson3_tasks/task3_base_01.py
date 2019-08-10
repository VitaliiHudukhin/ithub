
year = int(input())

if year % 4 != 0:
    print("Simple year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Intercalary year")
    else:
        print("Simple year")
else:
    print("Intercalary year")