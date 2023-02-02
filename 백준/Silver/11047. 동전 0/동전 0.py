n, k = map(int, input().split())

money_units = [] 
for _ in range(n):
    money_units.append(int(input()))

money_units.sort(reverse=True)

cnt = 0
for money_unit in money_units:
    if money_unit <= k:
        cnt += k // money_unit
        k = k % money_unit
print(cnt)