class Animal:
    def Sonido(self):
        pass

class Gato(Animal):
    def Sonido(self):
        return "Miau"
    
class Perro(Animal):
    def Sonido(self):
        return "Guau"
    
gato = Gato()
perro = Perro()