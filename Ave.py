class Ave():
    def __init__(self):
        self.energia = 2
    
    def volar(self, kms):
        if self.energia >= kms*3:
            self.energia -= kms*3
    
    def comer(self, grs):
        self.energia += grs

    def getEnergia(self):
        return self.energia