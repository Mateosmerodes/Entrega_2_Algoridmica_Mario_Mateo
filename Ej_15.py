from Class_Ej15 import *

ruta = ListaCircular()
ruta.agregar(0, 0, 0)
ruta.agregar(10, 10, 5)
ruta.agregar(20, 20, 5)
ruta.agregar(30, 30, 5)

robot = Robot()
actual = ruta.cabeza

for i in range(4):
    robot.Go_to(actual.x, actual.y, actual.z)
    
    if i % 2 == 0:
        robot.Coger_pieza(actual.x, actual.y, actual.z)
    else:
        robot.Dejar_pieza(actual.x, actual.y, actual.z)
        
    actual = actual.siguiente