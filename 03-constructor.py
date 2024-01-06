class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} con edad {self.edad} dice: Guau!")


# Perro es la clase, la clase es el plano de construcción, con los cuales se crean múltiples objetos (o instancias) en python
# habla es un método, un método es como una función asociada a una clase
# nombre es una propiedad
# añadiendo propiedas a una clase
mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
print(mi_perro.nombre)

mi_perro2 = Perro("Felipe", 5)
mi_perro2.habla()

print(mi_perro2.habla)
