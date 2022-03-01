def quick_sort(left, right):
    i = left
    j = right
    p = data[(left+right)//2]
    print("i={},j={},pivot={}".format(i,j,p))
    for k in range(left, right+1):
        print(data[k], end=",")
    while True:
        while data[i] < p:
            i = i + 1
        while data[j] > p:
            j = j - 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
        i = i + 1
        j = j - 1
    print("")
    for k in range(left, right+1):
        print(data[k], end=",")
    print("\n-----------------")
    if left < i-1:
        quick_sort(left, i-1)
    if right > j+1:
        quick_sort(j+1, right)

data = [8, 5, 1, 6, 4, 7, 3, 2]
print(data, "元のデータ")
print("-----------------")
quick_sort(0, len(data)-1)
print(data, "ソート後のデータ")
