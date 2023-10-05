a = int(input("valeur de a : "))
b = int(input("valeur de b : "))

ma = a*2
mb = b*2

ia = 2
ib = 2
while ma != mb:
    if ma < mb:
        ia += 1
        ma = a*ia
    else:
        ib += 1
        mb = b*ib
print(ma)
