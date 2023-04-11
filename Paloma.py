from Ave import *

class Paloma(Ave):
    def __init__(self, logger):
        super().__init__(logger)
    
    def defecar(self):
        if self.energia >= 1:
            self.energia -= 1
            self.logger.showWarn("La Paloma defecó y perdió energía.")