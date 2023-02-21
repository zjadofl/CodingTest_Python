def d(n):
    result = n + sum(list(map(int, str(n))))
    return result
array = []
for i in range(1, 10001):
    array.append(d(i))
    
for i in range(1, 10001):
    if i in array:
        continue
    print(i)