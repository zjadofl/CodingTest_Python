n = input()
cnt = 0
for i in range(1, int(n)+1):
    array = list(map(int, list(str(i))))
    diff_array = []
    if len(array) >= 2:
        for j in range(len(array)-1):
            diff_array.append(array[j+1] - array[j])
        if diff_array.count(diff_array[0]) == len(diff_array):
            cnt += 1
    else:
        cnt += 1
print(cnt)