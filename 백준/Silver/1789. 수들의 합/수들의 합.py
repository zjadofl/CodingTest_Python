import math
n = int(input())
a = int(math.sqrt(n*2))

expect = a * (a + 1) / 2
if (expect > n) and (n > 1):
    result = a-1
else:
    result = a
print(result)