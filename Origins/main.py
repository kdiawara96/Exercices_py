#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import hashlib
import time
import atexit
import multiprocessing

from crack import *
from utils import *


def display_name():
    print("FINISHED IN " + str(time.time() - debut) + "secondes")

"""
    -f : Path of dictionary file
    -g : Generate MD5 hash of pass
    -md5 : Hashed password (MD5)
    -l : Password length
    -o : Cherche le hash en ligne (google)

si le fichier est executer en tant que fonction main il va rentrer dans le if si non ...
"""
if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Password Cracker!")
    parse.add_argument("-f", "--file", dest="file", help="Path of dictionary file", required= False)
    parse.add_argument("-g", "--gen", dest="gen", help="Generate MD5 hash of pass", required= False )
    parse.add_argument("-md5", "--md5", dest="md5", help="Hashed password (MD5)", required= False )
    parse.add_argument("-l", "--length", dest="length", help="Password length", required= False, type= int)
    parse.add_argument("-o", "--online", dest="online", help="Cherche le hash en ligne (google)", required= False )

    args = parse.parse_args()
    processuss =[]
    work_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()
    cracker = Cracker()
    debut = time.time() 
    # atexit.register(lambda: print("FINISHED IN " + str(time.time() - debut) + "secondes"))  # Ou encore
    atexit.register(display_name)

    if args.md5:
        print("[*] [CRACKING HASH " + args.md5 + "]")
        if args.file and not args.length:
            print("[*] USING DICTIONNARY FILE " + args.file)
            # Cracker.crack_dict(args.md5, args.file)
            p1 = multiprocessing.Process(target= Cracker.work, args= (work_queue, done_queue, args.md5, args.file, False))
            processuss.append(p1)
            work_queue.put(cracker)
            p1.start()

            p2 = multiprocessing.Process(target= Cracker.work, args= (work_queue, done_queue, args.md5, args.file, True))
            processuss.append(p2)
            work_queue.put(cracker)
            p2.start()

            nonTrouve = 0
            while True:
                data = done_queue.get()
                if data == "TROUVE":
                    p1.kill()
                    p2.kill()
                    break
                elif data == "NON TROUVE":
                    nonTrouve += 1

                if nonTrouve == len(processuss):
                    print("AUCUN PROCESSUS N'A TROUVÉ LE MDP")
                    p1.kill()
                    p2.kill()
                    break

        elif args.length and not args.file:
            print("[*] USING LENGTH " + str(args.length))
            Cracker.crack_incr(args.md5, args.length)
        elif args.online:
            print("[*] USING ONLINE")
            Cracker.crack_online(args.md5)   
        else:
            print("[*] CHOSE FILE (-f) OR LENGTH (-l)")
    else:
        print("[*] MD5 HASH NOT PROVIDED!")   
    if args.gen:
        print("[*]  [GENERATING HASH " + args.gen + "]")
        print(hashlib.md5(args.gen.encode("utf-8")).hexdigest())