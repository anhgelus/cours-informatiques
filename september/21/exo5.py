last_name = input("Quel est votre nom ?\n")
name = input("Quel est votre prénom ?\n")
city = input("Quel est votre ville de résidence ?\n")
year_old = int(input("Quel est votre âge ?\n"))
birth_city = input("Quel est votre ville de naissance ?\n")
while True: # Je fais une loop pour éviter les pbs des mauvais code postaux, c'est pas important
    birth_city_post = int(input("Quel est le code postal de votre département de naissance ?\n"))
    if (birth_city_post >= 1 and birth_city_post <= 95) or (birth_city_post >= 971 and birth_city_post <= 974) or birth_city_post == 976:
        print("Vous êtes",name,last_name,"de",city,"et vous avez",year_old,"ans.")
        print("Vous êtes né.es à",birth_city,"("+str(birth_city_post)+")")
        break # ici aussi c'est en lien avec les loops
    else:
        print("Votre numéro de département est éronné !")

