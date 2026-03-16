class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.cabeza = None
        self.cola_ultimo = None
        self._tamano = 0

    def estaVacia(self):
        return self.cabeza is None

    def agregar(self, item):
        nuevo_nodo = Nodo(item)
        if self.estaVacia():
            self.cabeza = nuevo_nodo
            self.cola_ultimo = nuevo_nodo
        else:
            self.cola_ultimo.siguiente = nuevo_nodo
            self.cola_ultimo = nuevo_nodo
        self._tamano += 1

    def avanzar(self):
        if self.estaVacia():
            return None
        dato_eliminado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola_ultimo = None
        self._tamano -= 1
        return dato_eliminado

    def tamano(self):
        return self._tamano

    def frente(self):
        if self.estaVacia():
            return None
        return self.cabeza.dato

    def ultimo(self):
        if self.estaVacia():
            return None
        return self.cola_ultimo.dato

    def print(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos))