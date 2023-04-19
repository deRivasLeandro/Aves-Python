from Logger import Logger
from Paloma import Paloma
from Golondrina import Golondrina
from Mariposa import Mariposa


logger = Logger("INFO")
twinkle = Mariposa("Twinkle")
pepita = Golondrina("Pepita", 2)
pepon = Golondrina("Pepón", 1)
bombon = Paloma("Bombón")
lista = [twinkle, pepita, pepon, bombon]
for i in range(0, len(lista)):
    lista[i].comer(20)
for i in range(0, len(lista)):
    lista[i].volar(2)
for i in range(0, len(lista)):
    lista[i].comer(10)
for i in range(0, len(lista)):
    lista[i].volar(3)
for i in range(0, len(lista)):
    Logger.getInstance().showInfo(lista[i].getDistanciaRecorrida())