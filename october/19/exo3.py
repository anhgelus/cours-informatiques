from math import pi
def volume(r: int):
    return (4/3)*pi*(r**3)

r = int(input("Rayon du volume : "))
print(volume(r))
