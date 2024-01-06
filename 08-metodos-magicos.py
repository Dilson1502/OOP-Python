# Un método mágico se va a ejecutar cuando no lo llamemos directamente
# por ejemplo el constructor
# los métodos mágicos comienzan y terminan con __
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# así como existe el constructor, también existe el destructor, el método nágico __del__ define el comportamiento del método del (delete)
    def __del__(self):
        print(f"Chao perro {self.nombre}")
# los métodos mágicos se ejecutan automáticamente al llamar a nuestro objeto
# por ejemplo, el método mágico str permite definir el comportamiento del método str sobre nuestro objeto

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


# un método mágico se ejecuta solo, e inicia y terminan con __
perro = Perro("Chanchito", 7)
print(perro)
texto = str(perro)
print(texto)
del perro
