def tableMulti(base, start, end):
    n = start
    print("Fragment de la table de",n)
    while n <= end:
        print(base,"x",n,"=",base*n)
        n+=1
tableMulti(8,13,17)
