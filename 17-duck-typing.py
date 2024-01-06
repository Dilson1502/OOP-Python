class Usuario():
    def guardar(self):
        print("guardando en BBDD")

# una sesión es una forma de identificar cuando un usuario se conecta al servidor


class Sesion():
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

# el código se sigue ejecutando porque python tiene tipado dinámico, es decir, va a iterar con el for sobre la lista de objetos sin importarle si proviene/existe de una clase Modelo
