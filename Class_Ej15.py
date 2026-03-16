class NodoCircular:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, x, y, z):
        nuevo_nodo = NodoCircular(x, y, z)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

class Robot:
    def Coger_pieza(self, x, y, z):
        print(f"coger pieza de ({x}, {y}, {z})")

    def Dejar_pieza(self, x, y, z):
        print(f"dejar pieza en ({x}, {y}, {z})")

    def Go_to(self, x, y, z):
        print(f"trasladándose a ({x}, {y}, {z})")