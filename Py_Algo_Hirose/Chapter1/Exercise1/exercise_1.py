# 問1-(2)
a = 10 + 5 * 8
b = 20 - 9 / 2
print("aの値は", a)
print("bの値は", b)

# 問1-(3)
x =  4 ** 3
y = 35 // 9
z = x % y
print("xの値は", x)
print("yの値は", y)
print("zの値は", z)

# 問1-(4)
total = 0
for i in range(5):
    if i == 4:
        total = total * 2
    else:
        total = total + i
print("totalの値は", total)

# 問1-(5)
a = [
    [  7, 11,  3, 67, 55,  1],
    [ 21,  2, 14, 48, 16,  0],
    [ 41, 77, 98, -1,  5, 15],
    [ -6,  9, 32, 87, 20,  8]
]
print("a[0][0]の値は", a[0][0])
print("a[2][4]の値は", a[2][4])
print("a[3][5]の値は", a[3][5])
