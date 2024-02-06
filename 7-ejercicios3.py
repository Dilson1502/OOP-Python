class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave:
    def comer(self):
        print("El animal está volando")

class Mamifero:
    def comer(self):
        print("El animal está amamantando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()