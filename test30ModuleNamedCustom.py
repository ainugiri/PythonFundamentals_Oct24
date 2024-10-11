import test28Module as t28
import platform
import datetime
import math

t  = datetime.datetime.now()

print(t)
print(t.year)
print(dir(math))
print(getattr(math, "log10"))
dob = datetime.datetime(1984, 10, 6)
print(dob)
print(dob.strftime("%y"))

x  = platform.system()
#x = dir(platform) # list of attributes of platform module

print(x)

area = t28.c_pi * 10 * 10
print(area)