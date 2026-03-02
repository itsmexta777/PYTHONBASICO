from Enemigo import *
import random
class Zombie(Enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia,ataque=ataque)

    def habla(seif):
        print("Hummmmm. . .*")

    def propagador_enfermedad(self):
        print("El Zombie esta tratando de propogar la enfermedad")

        def ataque_especial(self):
            print ("zombie ataque especial")
            funciona_ataque_especial = random.random() < 0.50
            if funciona_ataque_especial:
                self.puntos_energia += 2
                print("zombie ha regenerado  su energia con 2 hp")