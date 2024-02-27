import time
import hashlib
import sys


mot_de_passe = input("Veuillez passez votre mot de passe à trouver : ")  # le mot de passe à trouver
# mot_de_passe = "MamanLafia"

password = "Maman Lafia12345"
password_md5 = hashlib.md5(password.encode("utf-8")).hexdigest()


def hash_crack():
    try:
        dictionnaire = open("/home/diawara/Desktop/dev/CyberIni/files/rockyou.txt", "r")
        trouver = False
        for mots in dictionnaire.readlines():
            #  Nous allons retirer l'espace entre entre les mots créé par le realines
            mots = mots.strip("\n").encode("utf-8")
            mots_md5 = hashlib.md5(mots).hexdigest()
            if mots_md5 == password_md5:
                print("Le mot de passe est : " + str(mots) +" <=> et le hash est :"+ str(mots_md5))
                trouver = True
        if not trouver:
            print("Le mot de passe n'a pas été trouvé")
    except FileNotFoundError:
        print("Fichier introuvable")
        # Ceux sont des manière pour quitter le programme avec des statuts code
        sys.exit(1)
    except Exception as err:
        print("Erreur => " + str(err))
        sys.exit(2)
    dictionnaire.close()



debut = time.time()
print(hash_crack())
print("Durée : " + str(time.time() - debut) + "secondes")
