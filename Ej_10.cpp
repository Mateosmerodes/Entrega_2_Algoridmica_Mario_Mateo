
#include<iostream>
#include "Class_Listas_No_Ordenadas.hpp"  //importamos la clase 


int main()
{
    UnorderedList lista1;
    UnorderedList lista2;

    // añadir elementos a la primera lista
    lista1.add(3);
    lista1.add(2);
    lista1.add(1);

    // añadir elementos a la segunda lista
    lista2.add(6);
    lista2.add(5);
    lista2.add(4);

    cout << "Lista 1:" << endl;
    cout << lista1 << endl;

    cout << "Lista 2:" << endl;
    cout << lista2 << endl;

    // anexar lista2 al final de lista1
    lista1.anexar(lista2);

    cout << "Lista 1 despues de anexar lista2:" << endl;
    cout << lista1 << endl;

    return 0;
}