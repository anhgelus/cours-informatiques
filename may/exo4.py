def replaceOccu(x, ch, y, i=0):
    if i == len(ch):
        return ch
    if ch[i] == x:
        if i == len(ch) - 1:
            ch = ch[:i] + y
        else:
            ch = ch[:i] + y + ch[i + 1:]
    return replaceOccu(x, ch, y, i + 1)


print(replaceOccu('a', 'papa', 'e'))
