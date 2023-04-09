from Ave import *

class Paloma(Ave):
    def __init__(self):
        super().__init__()
    
    def defecar(self):
        if self.energia >= 1:
            self.energia -= 1