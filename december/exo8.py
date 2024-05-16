def test(n: int, a: str, b: str) -> bool:
    t = a.replace(b, "", n)
    if len(t) != len(a) - len(b) * n:
        return False
    l = ""
    for c in b:
        if c == l:
            return False
        l = c
    return True


a = input("ch1 : ")
b = input("ch2 : ")
n = int(input("n : "))

print(test(n, a, b))
