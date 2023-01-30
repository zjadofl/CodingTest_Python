n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
cnt = 1
start = holes[0]
for hole in holes:
    if start + l - 1 < hole:
        cnt += 1
        start = hole
print(cnt)