n = int(input())
rope_weights = []
for _ in range(n):
    rope_weights.append(int(input()))
rope_weights.sort(reverse=True)

maximum = 0
for i in range(n):
    if maximum <= rope_weights[i] * (i+1) :
        maximum = rope_weights[i] * (i+1)
print(maximum)