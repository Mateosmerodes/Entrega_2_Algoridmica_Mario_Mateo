#include <iostream>
#include "Class_Listas_No_Ordenadas.hpp"
using namespace std;

int main()
{
    UnorderedList lista1;
    UnorderedList lista2;

    // Agregar elementos a lista1
    lista1.add(3);
    lista1.add(2);
    lista1.add(1);

    cout << "Lista1:" << endl;
    cout<<lista1;
    cout << "Tamaño lista1: " << lista1.size() << endl;

    // Agregar elementos a lista2
    lista2.add(6);
    lista2.add(5);
    lista2.add(4);

    cout << "\nLista2:" << endl;
    cout << lista2;
    cout << "Tamaño lista2: " << lista2.size() << endl;

    // Anexar lista2 a lista1
    lista1.anexar(lista2);

    cout << "\nLista1 después de anexar lista2:" << endl;
    cout <<lista1;
    cout << "Tamaño lista1: " << lista1.size() << endl;

    // Borrar un elemento
    lista1.remove(2);
    cout << "\nLista1 después de borrar 2:" << endl;
    cout <<lista1;
    cout << "Tamaño lista1: " << lista1.size() << endl;

    return 0;
}