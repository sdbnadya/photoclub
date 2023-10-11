import math

x = -2
a = 2.86

if x >= a:
    result = math.exp(x) + math.exp(a)
else:
    result = x ** a
print(result)
