from Class_Estructuras_lineales import Cola

primera=Cola()
segunda=Cola()

for i in range (21):
    primera.agregar(i)

for j in range (7):
    segunda.agregar(j)
print(primera)
print("\n")
print(segunda)
print("\n")
concatenada=primera.concatenar(segunda)
print(primera.concatenar(segunda))
