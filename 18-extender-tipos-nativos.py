lista = list([1, 2, 3])
lista.append(4)
lista.insert(0, 0)
print(f"la lista original es {lista}")

# creando el opuesto a append
# agrega los elementos al comienzo (como el método list.insert())


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista2 = Lista([1, 2, 3])
lista2.append(4)
lista2.prepend(10)

print(f"la nueva lista es {lista2} ")
