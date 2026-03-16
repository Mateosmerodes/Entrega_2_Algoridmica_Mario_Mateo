class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaNoOrdenada:
    """
        Los valores del TAD Lista son listas de items del tipo tipoelem.
        Las posiciones de los items de la lista y la posición fin de la lista 
        son del tipo int.
        Las listas son mutables: agregar, insertar, anexar, borrar y modificar,
        añaden, eliminan y modifican items en la lista.
    """

    def __init__(self):
        """
            efecto: Crea y devuelve la lista vacía
        """
        self.cabeza = None
        self.numElementos=0

    def estaVacia(self):
        """
            requerimientos: Una lista 
            efecto: Devuelve TRUE si es lista vacía, y FALSE en caso contrario
        """
        return self.cabeza == None
    
    def agregar(self,item):
        """
            requerimientos: Una lista y un item
            modifica: La lista
            efecto: Inserta el item en la lista como primer item de la lista.

        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        self.numElementos+=1

    def tamano(self):
        """
            requerimientos: Una lista
            efecto: devuelve int como numero de items de la lista   
        """
       #la nueva complejidad temporal es 1, ya que devuelve un numero en vez de recorrer toda la lista
        return self.numElementos

    def buscar(self,item):
        """
            requerimientos: Una lista no vacía y el ítem a buscar
            efecto: Devuelve TRUE si esta en la lista y FALSE en caso contrario. 
        """
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
        """
            requerimientos: Una lista no vacía y un item
            modifica: La lista
            efecto: Elimina el item de la lista

        """
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
    
        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
        self.numElementos-=1


    def imprimir(self):
            actual = self.cabeza
            while actual is not None:
                print(actual.obtenerDato(), end=" -> ")
                actual = actual.obtenerSiguiente()
            print("None")