# class Diccionario:
#     def verificar_palabra(self,palabra):
#         # logica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self,texto):
#         #usamos el diccionario para corregir el texto
#         

from abc import ABC, abstractclassmethod

class verificador_ortografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self,palabra):
        #logica para verificar palabras
        pass

class Diccionario(verificador_ortografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras si está en el diccionario
        pass

class ServivicoOnline(verificador_ortografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador

    def corregir_texto(self,texto):
        #usamos el verificador para corregir texto
        pass