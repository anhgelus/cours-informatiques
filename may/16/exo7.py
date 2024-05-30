def power(a, n, b=-1):
    global c
    c += 1
    if b == -1:
        b = a
    if n == 1:
        return b
    elif n == 0:
        return 1
    # a * a * a * ... * a (n fois)
    return power(a, n - 1, b * a)


def better_power(a, n):
    global c
    c += 1
    if n == 0:
        return 1
    elif n == 1:
        return a
    if n % 2 == 0:
        tmp = better_power(a, n / 2)
        return tmp * tmp
    tmp = better_power(a, (n - 1) / 2)
    return tmp * tmp * a


for i in range(31):
    c = 0
    v = power(2, i)
    if v != 2 ** i:
        raise ValueError(f"power is not valid: {v} (power) vs {2 ** i} (valid)")
    print(f"Nombre d'appel de power : {c}")
    c = 0
    v = better_power(2, i)
    if v != 2 ** i:
        raise ValueError(f"better_power is not valid: {v} (power) vs {2 ** i} (valid)")
    print(f"Nombre d'appel de better_power : {c}")
