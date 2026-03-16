class Conjunto:
    def __init__(self):
        self.elementos=[]
    def inserta(self,elemento):
        if not (elemento in self.elementos):
            self.elementos.append(elemento)
    def __str__(self):
        cadena='{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena=cadena+str(elemento)+', '
            cadena=cadena+str(self.elementos[-1])
        return cadena+'}'
    def tamaño(self):
        return len(self.elementos)
    def pertenece(self, elemento):
        return elemento in self.elementos
    
    def elimina(self, elemento):

        if self.pertenece(elemento):
            posicion=self.elementos.index(elemento)
            self.elementos.pop(posicion)

    def union(self, otroConjunto):
        resultado = Conjunto()

        for elemento in self.elementos:
            resultado.inserta(elemento)

        for elemento in otroConjunto.elementos:
            resultado.inserta(elemento)

        return resultado
        
    def interseccion(self, otroConjunto):
        resultado = Conjunto()

        for elemento in self.elementos:
            if elemento in otroConjunto.elementos:
                resultado.inserta(elemento)

        return resultado
    
    def diferencia(self, otroConjunto):
        resultado = Conjunto()

        for elemento in self.elementos:
            if elemento not in otroConjunto.elementos:
                resultado.inserta(elemento)

        return resultado
    
    def incluye(self, otroConjunto):

        incluye=True
        for elemento in otroConjunto.elementos:
            if  not self.pertenece(elemento):
                incluye=False
        return incluye