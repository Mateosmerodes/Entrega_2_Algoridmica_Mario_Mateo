from Class_Conjuntos import Conjunto

a = Conjunto()
b = Conjunto()
c = Conjunto()

a.inserta(1)
a.inserta(2)
a.inserta(3)
a.inserta(5)

b.inserta(3)
b.inserta(4)

c.inserta(2)
c.inserta(5)

print("Union:", a.union(b))
print("Interseccion:", a.interseccion(b))
print("Diferencia:", a.diferencia(b))
print("Incluye:", a.incluye(c))