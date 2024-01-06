class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
# en ocasiones, requerimos definir ciertas acciones en nuestro código, como mostrar o editar propiedades de los objetos
# python tiene una forma de convertir métodos en propiedades del objeto
# esto es útil cuando queremos hacer una acción sobre una propiedad sin legar a sobrecargar el código con métodos def nombre_metodo(self, attributos)
# es como crear acciones una tras otra sobre la misma propiedad del objeto

    @property
    def nombre(self):
        print("pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
