import random
from Ave import *

class Golondrina(Ave):
    def __init__(self, energiaAlPescar):
        super().__init__()
        self.energiaAlPescar = energiaAlPescar
        
    def pescar(self):
        if self.energia >= self.energiaAlPescar:
            self.energia -= self.energiaAlPescar
            prob = random.randint(1, 10)
            if prob == 10:
                self.energia += 10
