from Class_Estructuras_lineales import ListaOrdenada

#Cola_prioridad.py
class ColaPrioridad:
    def __init__(self):
        
        self.cola=ListaOrdenada()

    def añade(self,elemento):
        self.cola.agregar(elemento)

    def primero(self):
        if self.cola.estaVacia():
            return None
        actual = self.cola.cabeza
        while actual.obtenerSiguiente() != None:
            actual = actual.obtenerSiguiente()

        return actual.obtenerDato()

    def extrae(self):
        if self.cola.estaVacia():
            return None
        actual = self.cola.cabeza
        previo = None

        while actual.obtenerSiguiente() != None:
            previo = actual
            actual = actual.obtenerSiguiente()

        dato = actual.obtenerDato()

        if previo == None:
            self.cola.cabeza = None
        else:
            previo.asignarSiguiente(None)

        return dato
    
    def tamano(self):
        return self.cola.tamano()

    def esta_Vacia(self):
        return self.cola.estaVacia()
           
        
    def buscar(self, item):
        return self.cola.buscar(item)
        


