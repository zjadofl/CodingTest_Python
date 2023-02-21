n = int(input())
cnt = 0
for i in range(1, n+1):
    if i <= 99:
        cnt += 1
    else:
        array = list(map(int, str(i)))
        if array[0] - array[1] == array[1] - array[2]:
            cnt += 1
print(cnt)