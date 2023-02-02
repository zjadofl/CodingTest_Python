n = int(input())
person = list(map(int, input().split()))

person.sort()

time_sum = 0
for i in range(1,len(person)+1):
    time_sum += sum(person[:i])

print(time_sum)