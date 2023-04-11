class Ave():
    def __init__(self, logger):
        self.energia = 2
        self.logger = logger
    
    def volar(self, kms):
        if self.energia >= kms*3:
            self.energia -= kms*3
            self.logger.showInfo("El ave viajó " + str(kms) + " kms.")
        else:
            self.logger.showError("El ave no tiene energía suficiente para volar esos kms.")

    def comer(self, grs):
        self.energia += grs
        self.logger.showInfo("El ave ingirió " + str(grs) + " grs de comida.")

    def getEnergia(self):
        return self.energia