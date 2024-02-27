
import time
import string

# mot_de_passe = input("Veuillez passez votre mot de passe à trouver : ")  # le mot de passe à trouver

mot_de_passe = "Maman Lafia12345" 

def mot_aleatoire():
    # lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6']
    lettres = string.printable
    suivi= ""
    result = ""
    for i in range(len(mot_de_passe)):
        ii= 0
        while mot_de_passe[i] != suivi:
            print(result + suivi)
            time.sleep(0.05)
            suivi = lettres[ii]
            ii+=1
            if ii >= len(lettres):
                ii=0
            # suivi = random.choice(lettres)
        result += suivi
    return result

debut = time.time()
print(mot_aleatoire())
print("Durée : " + str(time.time() - debut) + "secondes")

