import random
from Ave import *

class Golondrina(Ave):
    def __init__(self, logger, energiaAlPescar):
        super().__init__(logger)
        self.energiaAlPescar = energiaAlPescar
        
    def pescar(self):
        if self.energia >= self.energiaAlPescar:
            self.energia -= self.energiaAlPescar
            prob = random.randint(1, 10)
            if prob == 10:
                self.energia += 10
                self.logger.showInfo("La Golondrina logró pescar y recuperó energía.")
            else:
                self.logger.showWarn("La Golondrina no logró pescar y perdió energía.")
        else:
            self.logger.showError("La Golondrina no tiene energía suficiente para pescar.")
