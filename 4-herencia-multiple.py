class Persona:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre = nombre
        self.edad=edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco desde persona")

class Empleado(Persona):
    def __init__(self,nombre,edad, nacionalidad,trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    # los metodos se pueden sobreescribir
    def hablar(self):
        print("Hola, estoy hablando un poco desde empleado")


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return(f"mi habilidad es {self.habilidad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y {super().mostrar_habilidad()}")




# empleado1 = Empleado("roberto",43,"AR","programador",100000)
# empleado1.hablar()
    
roberto = EmpleadoArtista("roberto",43,"argentino","cantar",100000,"google")
roberto.presentarse()