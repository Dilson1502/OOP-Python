def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()
        print("despues de llamar a la funcion")
    return funcion_modificada

def saludo():
    print("Hola Dalto")

saludo_modificado = decorador(saludo)
saludo_modificado()

# con decoradores
@decorador
def saludo():
    print("Hola dalto")