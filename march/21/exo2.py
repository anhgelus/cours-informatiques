L = [3, 4, 2, 0, 0, 8, 5]

pos = -1
while pos < 1 or pos > len(L):
    pos = int(input("Donner une position : "))
val = int(input("Donner une valeur : "))
L[pos - 1] = val
