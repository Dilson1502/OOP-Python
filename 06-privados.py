# Una propiedad privada permita bloquear el acceso para que no pueda ser modificada
class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


# creemos un objeto aprovechando el factory method
perro1 = Perro.factory()
perro1.habla()
# las propiedades de clase solo pueden accederse desde la clase misma, no desde los objetos
# la siguiente línea retorna un error
# print(perro1.__nombre)
# ejecutemos el método get_nombre(), con este método si podremos retornar el nombre, esto se conoce como getters
print(perro1.get_nombre())
# de igual manera, existen los setters, creando un método de clase podemos cambiar el valor de una propiedad privada
perro1.set_nombre("Balto")
perro1.habla()
# el metodo __dict__ nos devuelve un dicionario así : {nombre clase: propiedad del objeto}
print(perro1.__dict__)
print(perro1._Perro__nombre)
print(dir(perro1))
