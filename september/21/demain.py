year = int(input("Année courante : "))
month = int(input("Mois courant : "))
day = int(input("Jour courant : "))

# Ici je définis une fonction qui va me simplifier la vie car comme tout bon développeur, je suis un flemmard
def show(nextMonth: bool):
    """
    Parameters
    ----------
    nextMonth: bool, optionnal
        Change de mois
    """
    print("Année courante :",year)
    print("Mois courant :",month)
    print("Jour :",day)
    if nextMonth:
        print("Demain, nous serons le",1)
        return
    print("Demain, nous serons le",day+1)

if month <= 7:
    if month % 2 == 0 and month != 2:
        show(day == 30)
    elif month % 2 == 1:
        show(day == 31)
    else:
        if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
            show(day == 29)
        else:
            show(day == 28)
else:
    if month % 2 == 0:
        show(day == 31)
    else:
        show(day == 30)
