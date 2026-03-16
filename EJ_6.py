from Class_Impresion import Impresora
from Class_Impresion import Tarea
import random
from Class_Colas_prioridad import ColaPrioridad

def nuevaTareaImpresion():
    num = random.randrange(1,181)
    return num == 180
def simulacion(numSegundos, paginasPorMinuto):

    impresora = Impresora(paginasPorMinuto)
    colaImpresion = ColaPrioridad()
    tiemposEspera = []

    for segundoActual in range(numSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.añade(tarea)

        if (not impresora.ocupada()) and (not colaImpresion.esta_Vacia()):
            siguiente = colaImpresion.extrae()
            tiemposEspera.append(siguiente.tiempoEspera(segundoActual))
            impresora.iniciarNueva(siguiente)

        impresora.tictac()
    suma_tiempos=0
    
    for tiempo in range(len(tiemposEspera)):
        suma_tiempos=suma_tiempos+tiemposEspera[tiempo]  

    if len(tiemposEspera) > 0:
        esperaPromedio = suma_tiempos / len(tiemposEspera)
    else:
        esperaPromedio = 0

    print("Tiempo medio de espera:", esperaPromedio)

for i in range(10):
    simulacion(3600, 10)