def suiteU(n):
    v1 = 1
    v2 = 2
    if n == 0:
        return [v1]
    elif n == 1:
        return [v1, v2]
    v = [v1, v2]
    for i in range(2, n + 1):
        v.append(5 * v[i - 1] + 10 * v[i - 2])
    return v


n = int(input("n : "))
print(suiteU(n))
