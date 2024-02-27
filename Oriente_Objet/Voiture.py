
class Voiture:
    def __init__(self, marque, model, cv, immat):
        self._marque = marque
        self._model = model
        self._cv = cv
        self.immat = immat
    

    @staticmethod
    def demarrer_voiture():
        print("Je demarre la voiture ")
    

    def marque_de_la_voiture(self):
        print(self._marque)