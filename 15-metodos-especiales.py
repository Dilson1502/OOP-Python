class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"


dalto = Persona("Lucas", 21)
print(dalto.nombre)  # Output: Lucas

repre = repr(dalto)
resultado = eval(repre)  # Now `eval()` uses the string representation of `dalto`
print(resultado)  # Output: Persona(nombre='Lucas', edad=21)
