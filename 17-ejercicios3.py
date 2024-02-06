class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})"
    
    def __add__(self,otro):
        nuevo_nombre = self.nombre + "-" + otro.nombre
        nueva_fuerza = round(((self.fuerza + otro.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otro.velocidad)/2)**2)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
goku = Personaje("goku",100,100)
vegeta = Personaje("vegeta",99,99)
jiren = Personaje("jiren",130,130)

jigogeta= goku+vegeta+jiren
print(jigogeta.fuerza)