class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    pass

class F:
     def hablar(self):
        print("Hola desde F")

class C(F):
    pass

class D(B,C):
    pass

d = D()
d.hablar()

print(D.mro())

F.hablar(d)
