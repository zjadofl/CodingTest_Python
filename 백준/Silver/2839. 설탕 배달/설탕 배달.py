n = int(input())
value = -1

if n % 5 == 0:
    value = n // 5
else :
    for i in range(n // 5, 0, -1):
        q = n - 5 * i
        if q % 3 == 0:
            value = i + q // 3
            break
if (value == -1) and (n % 3 == 0) :
    value = n // 3

print(value)