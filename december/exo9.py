def test2(a: str, b: str) -> int:
    n = 0
    c = ""
    while len(c) < len(a):
        c += b
        n += 1
    if c == a:
        return n
    return 0


a = input("ch1 : ")
b = input("ch2 : ")
n = test2(a, b)
if n == 0:
    print("non")
else:
    print(n)
