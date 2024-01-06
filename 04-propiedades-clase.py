class Perro:
    # propiedad de clase (aplica para todas las instancias)
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} con edad {self.edad} dice: Guau!")


# Perro es la clase, la clase es el plano de construcción, con los cuales se crean múltiples objetos (o instancias) en python
# habla es un método, un método es como una función asociada a una clase
# nombre es una propiedad (o atributo)
# añadiendo propiedas a una clase
# patas es una propiedad transversal a todas las instancias de clase (objetos) que se creen, para cambiar el valor de una
# propiedad de clase se debe cambiar globalmente
Perro.patas = 3
mi_perro = Perro("Chanchito", 1)
print(Perro.patas)

mi_perro2 = Perro("Felipe", 1)
print(mi_perro2.patas)
