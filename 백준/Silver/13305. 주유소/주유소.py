n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
for i in range(len(prices)):
    if prices[i] == min(prices):
        result += sum(distances[i:])
        break
    result = prices[i] * distances[i]   
print(result)