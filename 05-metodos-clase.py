# Creemos una clase llamado Perro, la cuál nos permitirá crear distintos tipos de perros recibiendo un nombre y una edad como paramétros

class Perro:

    # en la clase anterior vimos que existen propiedades comunes a todos los objetos, como las patas en los perros, esto se llaman propiedades de clase
    patas = 4
# inicialicemos el constructor de nuestra clase, indicando el nombre y edad como parámetros para crear nuestro objeto

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# podemos crear métodos (funciones) propias de la clase, es decir, que se aplicarán directamente sobre la clase Perro y no sobre cada objeto independientemente
# para esto usaremos @classmethod y cls en lugar de self
    @classmethod
    def habla_global(cls):
        print("Guau! Esto es un método de clase")
# así se vería un método propio del objeto

    def habla_local(self):
        print("Guau! Esto es un método de objeto")
# también puedes generar métodos propios de la clase que te permitan fabricar objetos, esto se conoce como factory methods
# usaremos @classmethod junto a cls

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro("Balto", 2)
perro2 = Perro("Max", 3)
perro3 = Perro.factory()

perro2.habla_local()
print(f"Esto es un factory method: {perro3.edad}, {perro3.nombre}")
Perro.habla_global()
