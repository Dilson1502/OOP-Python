# from abc import ABC, abstractclassmethod

# class Trabajador(ABC):
#     @abstractclassmethod
#     def comer(self):
#         pass

#     @abstractclassmethod
#     def trabajar(self):
#         pass

#     @abstractclassmethod
#     def dormir(self):
#         pass

# class Human(Trabajador):
#     def comer(self):
#         print("El humano está comiendo")

#     def trabajar(self):
#         print("El humano está trabajando")

#     def dormir(self):
#         print("El humano está durmiendo")

# class Robot(Trabajador):
#     def comer(self):
#         pass

#     def trabajar(self):
#         pass

#     def dormir(self):
#         print("El humano está durmiendo")

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("el robot está trabajando")

robot = Robot()
robot.trabajar()

Humano = Humano()
Humano.dormir()
