
import urllib.error
import string
import sys
import hashlib
import urllib.request
import urllib.response

from utils import *

class Cracker:
        
        @staticmethod 
        def crack_dict(md5, file):
            try:
                fileOpen = open(file, "r")
                trouver = False
                for mot in fileOpen.readlines():
                    mot = mot.strip("\n")
                    hashmd5 = hashlib.md5(mot.encore("utf-8")).hexdigest()
                    if hashmd5 == md5:
                        print(Couleur.VERT+ "[+] Mot de passe trouver : " +str(mot)+ "(" + hashmd5 + ")"+ Couleur.FIN)
                        trouver = True
                if not trouver:
                    print( Couleur.ROUGE + "[-] Mot de passe non trouvé :(" +Couleur.FIN)
                fileOpen.close()
            except FileNotFoundError:
                print(Couleur.ROUGE + "[-] File not found exception!" +Couleur.FIN)
                sys.exit(1)
            except Exception as err:
                print(Couleur.ROUGE + "[-] erreur "+str(err)+ "" +Couleur.FIN)
                sys.exit(2)

        @staticmethod
        def crack_incr(md5, length, currentpass = []):
            # lettres = string.ascii_letters
            lettres = string.printable
            if length >= 1:
                if len(currentpass) == 0:
                    currentpass = ['a' for _ in range(length)]
                    Cracker.crack_incr(md5, length, currentpass)
                else:
                    for c in lettres:
                        currentpass[length -1] = c
                        print("[*] Trying : " + "" .join(currentpass) )
                        if hashlib.md5("".join(currentpass).encode("utf-8")).hexdigest() == md5:
                            print( Couleur.VERT+ "[+] PASSWORD FOUND JACKPOT! " + "".join(currentpass) + "" + Couleur.FIN)
                            sys.exit(0)
                        else:
                            Cracker.crack_incr(md5, length - 1, currentpass)


        @staticmethod
        def crack_online(md5):
            try:
                agent_utilisateur = "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
                url = "https://www.google.fr/search?hl=fr&q=" +md5
                headers = {'User-Agent': agent_utilisateur}
                requet = urllib.request.Request(url, None, headers)
                reponse = urllib.request.urlopen(requet)
            except urllib.error.HTTPError as e:
                print("Error HTTPS"+ e) 
            except urllib.error.URLError as e:
                print("Error d'URL : " +e.reason)

            if "Aucun document" in reponse.read():
                print(Couleur.ROUGE + "[-] HASH NOT FOUND IN GOOGLE!" + Couleur.FIN)
            else:
                print(Couleur.VERT + "[+] HASH JACKPOT" +url+ Couleur.FIN)
