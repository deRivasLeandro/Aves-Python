from Logger import Logger
class Mariposa():
    def __init__(self, nombre):
        self.nombre = nombre
        self.peso = 0
        self.grsIngeridos = 0
        self.distanciaRecorrida = 0

    def volar(self, kms):
        self.distanciaRecorrida += kms
        Logger.getInstance("INFO").showInfo(self.nombre + " recorrió " + str(kms) + " kms.")

    def comer(self, grs):
        self.grsIngeridos += grs
        Logger.getInstance("INFO").showInfo(self.nombre + " ingirió " + str(grs) + " grs.")
        if (self.grsIngeridos>=5):
            self.peso += self.grsIngeridos/5
            self.grsIngeridos = self.grsIngeridos%5
        

    def getPeso(self):
        return self.peso
    

    def getDistanciaRecorrida(self):
        return self.nombre + " recorrió " + str(self.distanciaRecorrida) + " kms."