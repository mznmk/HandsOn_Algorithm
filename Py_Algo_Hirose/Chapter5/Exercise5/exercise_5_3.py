data = [1, 3, 8, 2, 4, 6, 5, 9, 7, 10]
n = len(data)
for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if data[j-1] < data[j]:
            data[j], data[j-1] = data[j-1], data[j]
print(data, "バブルソート：降順")
