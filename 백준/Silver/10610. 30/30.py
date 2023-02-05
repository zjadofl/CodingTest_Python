n = list(input())
n = list(map(int, n))

if (0 in n) and (sum(n) % 3 == 0):
    n.sort(reverse=True)
    result = ''.join(map(str, n))
else:
    result = -1
print(result)