import datetime
import argparse
a = datetime.datetime.now()
b = datetime.datetime(2018, 3, 21)
c = a - b
print(c)

d = datetime.timedelta(days=2, hours=4)
print(a+d)
