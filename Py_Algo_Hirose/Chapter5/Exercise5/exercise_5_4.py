import random
n = 30
data = [0]*n
for i in range(n):
    data[i] = random.randint(0, 50)

for i in range(n-1):
    m = i
    for j in range(i+1, n):
        if data[j] > data[m]:
            m = j
    data[i], data[m] = data[m], data[i]
print(data, "選択ソート：降順")
