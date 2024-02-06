class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible +=cantidad  

    def usar_combustible(self,cantidad):
        self.combustible -=cantidad

    def obtener_combustible(self):
        return self.combustible


class Auto:
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("has movido el auto")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

tanque1 = TanqueDeCombustible()
auto1 = Auto(tanque1)

print(auto1.obtener_posicion())
auto1.mover(10)
print(auto1.obtener_posicion())
auto1.mover(20)
print(auto1.obtener_posicion())
auto1.mover(30)
print(auto1.obtener_posicion())
auto1.mover(100)
print(auto1.obtener_posicion())
auto1.mover(300)
print(auto1.obtener_posicion())