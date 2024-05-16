def plural(w: str):
    l = w[len(w) - 1]
    if l == 's' or l == 'z' or l == 'z':
        return w
    if w.endswith("al"):
        return w[:len(w) - 1] + "ux"
    return w + "s"


print(plural("souris"))
print(plural("livre"))
print(plural("gaz"))
print(plural("cheval"))
