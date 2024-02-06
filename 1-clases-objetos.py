class Celular:
    def __init__(self,marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self, usuario):
        print(f"Estas haciendo un llamado a {usuario} desde un celular marca {self.marca}")

    def cortar(self, usuario):
        print(f"Estas cortando un llamado a {usuario} desde un celular marca {self.marca}")
    
celular1 = Celular("Apple","iphone 15","48MP")
print(celular1.camara)
celular1.llamar("Amigo1")