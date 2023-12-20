def replace(w: str, n: int) -> str:
    if n > len(w):
        raise ValueError("n is bigger than the length of w")
    ch = ""
    for i in range(len(w)):
        if i == n-1:
            ch += "?"
        else:
            ch += w[i]
    return ch

print(replace("bonjour", 2))
print(replace("patate au beurre", 5))
