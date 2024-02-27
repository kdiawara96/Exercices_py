#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Voiture import Voiture

def main():
    objetVoiture = Voiture("Peugeot", "206", 5, "AA-123-AA")
    objetVoiture.marque_de_la_voiture()
    Voiture.demarrer_voiture()
    print(objetVoiture.immat)


if __name__ == "__main__":
    main()