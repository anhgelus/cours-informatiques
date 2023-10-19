n = int(input("Entier : "))
arr = []

while len(arr) < n:
    arr.append(int(input("Valeur : ")))

i = 0
val = True
while i != len(arr)-1:
    if arr[i] >= arr[i+1]:
        print("les",n,"valeurs ne sont pas triées")
        val = False
        break
    i += 1
if val : print("les",n,"valeurs sont triées de façon croissante.")

