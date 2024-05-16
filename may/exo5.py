def pgcd(a, b):
    r = a % b
    if r == 0:
        return b
    return pgcd(b, r)


print(pgcd(15, 4))
print(pgcd(45, 33))
print(pgcd(0x31cb62f77684737f,
           0x7d9cdba126e0097d))  # ce sont des nombres en hexadécimal (3588070343115567999 et 9051350836296288637)
