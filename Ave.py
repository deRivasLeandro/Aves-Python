from Logger import Logger
class Ave():
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 2
        self.nombre = nombre
        self.distanciaRecorrida = 0
    
    def volar(self, kms):
        if self.energia >= kms*3:
            self.energia -= kms*3
            self.distanciaRecorrida += kms
            Logger.getInstance().showInfo(self.nombre + " viajó " + str(kms) + " kms.")
        else:
            Logger.getInstance().showError(self.nombre + " no tiene energía suficiente para volar esos kms.")

    def comer(self, grs):
        self.energia += grs
        Logger.getInstance().showInfo(self.nombre + " ingirió " + str(grs) + " grs de comida.")

    def getEnergia(self):
        return self.energia
    
    def getDistanciaRecorrida(self):
        return self.nombre + " recorrió " + str(self.distanciaRecorrida) + " kms."