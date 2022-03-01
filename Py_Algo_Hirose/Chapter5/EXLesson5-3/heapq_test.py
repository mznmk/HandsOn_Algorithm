import heapq
import random

n = 10
data = [0]*n
for i in range(n):
    data[i] = random.randint(1, 99)
print(data, "元のデータ")

heapq.heapify(data)
print(data, "ヒープ構造にしたデータ")

print("値を順に取り出す")
for i in range(n):
    v = heapq.heappop(data)
    print(v, end="→")
print(data)
