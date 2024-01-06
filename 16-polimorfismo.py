from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")

# una sesión es una forma de identificar cuando un usuario se conecta al servidor


class Sesion(Model):
    def guardar(self):
        print("guardando en archivo")

# polimorfismo


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


# creando instancias (objetos)
usuario = Usuario()
sesion = Sesion()
# polimorfirsmo, llamar métodos de diferentes objetos en simultáneo
guardar([sesion, usuario])
