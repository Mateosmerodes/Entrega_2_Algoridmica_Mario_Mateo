from Class_Colas_prioridad import ColaPrioridad
import random

x=ColaPrioridad()    #creamos numeros aleatorios para rellenar la cola
for i in range (random.randint(300, 400)):
    num=random.randint(1,500)  #creamos numeros aleatorios
    if not x.buscar(num):
        x.añade(random.randint(1,500))

print(f'el primer elemento es {x.primero()}')
print(f'El tamaño de la cola es de {x.tamano()} elementos')

print(f'Se va a extraer el elemento  {x.primero()}')
x.extrae()

print(f'el nuevo primer elemento es {x.primero()}')

print("Vamos a extraer todos los elementos")
for i in range (300):
    x.extrae()

if x.esta_Vacia:
    print("La cola esta vacia")