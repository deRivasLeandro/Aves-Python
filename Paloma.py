from Ave import *
from Logger import Logger

class Paloma(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def defecar(self):
        if self.energia >= 1:
            self.energia -= 1
            self.distanciaRecorrida += 1
            Logger.getInstance().showWarn(self.nombre + " defecó y perdió energía.")
        else:
            Logger.getInstance().showError(self.nombre + " no tiene energía suficiente para defecar.")