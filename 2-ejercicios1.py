class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado= input("Digame su grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
        DATOS DEL ESTUDIANTE: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
       Grado: {estudiante.grado}
        """
        )

validation = False
while not validation:
    estudiar = input("¿Que estás haciendo?: ")
    if (estudiar.lower()=="estudiar"):
        validation = True
        estudiante.estudiar()