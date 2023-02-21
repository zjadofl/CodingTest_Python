total_set = set(range(1, 10001))
def d(n):
    result = n + sum(map(int, str(n)))
    return result

array = []
for i in range(1, 10001):
    array.append(d(i))
    
result_array = total_set - set(array)
    
for i in sorted(result_array):
    print(i)