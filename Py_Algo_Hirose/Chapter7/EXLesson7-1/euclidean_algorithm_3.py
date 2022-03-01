n = 0
def euclid(a, b):
    global n
    n += 1
    print("再帰関数の実行", n, "回目")
    print("a=", a)
    print("b=", b)
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

print("a≧bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
print("それらの数の最大公約数は", euclid(a, b))
