n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x: (x[1], x[0]))    
cnt = 1
meeting = times[0]
for i in range(1, len(times)):
    if meeting[1] <= times[i][0]:
        cnt += 1
        meeting = times[i]
print(cnt)