import random
from Ave import *
from Logger import Logger

class Golondrina(Ave):
    def __init__(self, nombre, energiaAlPescar):
        super().__init__(nombre)
        self.energiaAlPescar = energiaAlPescar
        
    def pescar(self):
        if self.energia >= self.energiaAlPescar:
            self.energia -= self.energiaAlPescar
            self.distanciaRecorrida += 1
            prob = random.randint(1, 10)
            if prob == 10:
                self.energia += 10
                Logger.getInstance().showInfo(self.nombre + " logró pescar y recuperó energía.")
            else:
                Logger.getInstance().showWarn(self.nombre + " no logró pescar y perdió energía.")
        else:
            Logger.getInstance().showError(self.nombre + " no tiene energía suficiente para pescar.")
