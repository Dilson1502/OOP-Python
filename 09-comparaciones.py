# Cuando tratamos de comparar con los operadores de igualdad en python, la acción que ejecutará es verificar si las instancias están en mismos espacios de memoria
# para lograr el comportamiento deseado al utilizar operadores debemos utilizar métodos mágicos
class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# implementemos métodos mágicos
# __eq__ cambiará el comportamiento del operador ==
# pasar self, otro (haciendo referencia a otra instancia)
# magic method equal

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
# magic method not equal

    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
# magic method lower than

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
# magic method lower than or equal

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)
print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)
