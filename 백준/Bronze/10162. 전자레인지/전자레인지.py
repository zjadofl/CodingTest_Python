t = int(input())
units = [300, 60, 10]
result = []
if t % 10:
    print(-1)
else: 
    for unit in units:
        result.append(t//unit)
        t %= unit
    print(' '.join(map(str, result)))