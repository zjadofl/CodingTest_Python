n = input().split('-')
for i in range(len(n)):
    if i == 0:
        result = sum(list(map(int, n[i].split('+'))))
        continue
    l = list(map(int, n[i].split('+')))
    result -= sum(l)
print(result)