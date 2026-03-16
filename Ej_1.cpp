#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <regex>
#include <algorithm>
#include <stdexcept>

using namespace std;

// --- IMPLEMENTACIÓN DE TU LIBRERÍA DE PILAS (Corregida y completada) ---
template <class T>
class MiPila {
public:
    struct node {
        T node_data;
        node *next;
        // Constructor del nodo para facilitar la asignación
        node(T data) : node_data(data), next(nullptr) {} 
    };

    // Constructor de la pila
    MiPila() : root_node(nullptr), elements(0) {}

    // Destructor (Corregido: ahora borra todos los nodos al destruir la pila)
    ~MiPila() {
        while (!empty()) {
            pop();
        }
    }

    void push(T val) {
        node* new_node = new node(val);
        new_node->next = root_node;
        root_node = new_node;
        elements++;
    }

    bool empty() { 
        return root_node == nullptr; 
    }

    T top() {
        if (empty()) throw runtime_error("Error: Pila vacia");
        return root_node->node_data;
    }

    void pop() {
        if (empty()) return;
        node* temp = root_node;
        root_node = root_node->next;
        delete temp; // Liberamos la memoria del nodo
        elements--;
    }

    int size() { 
        return elements; 
    }

private:
    node *root_node;
    int elements;
};
// ----------------------------------------------------------------------

class EvaluadorPrefijo {
private:
    unordered_map<string, double> variables;

    int precedencia(const string& op) {
        if (op == "+" || op == "-") return 1;
        if (op == "*" || op == "/") return 2;
        return 0;
    }

    vector<string> tokenizar(const string& expresion) {
        regex re("([A-Za-z_]+|\\d+\\.\\d+|\\d+|[-+*/()])");
        sregex_iterator inicio(expresion.begin(), expresion.end(), re), fin;
        vector<string> tokens;
        
        for (auto it = inicio; it != fin; ++it) {
            tokens.push_back(it->str());
        }
        return tokens;
    }

public:
    EvaluadorPrefijo(const unordered_map<string, double>& vars) : variables(vars) {}

    vector<string> infijaAPrefija(const string& expresion) {
        vector<string> tokens = tokenizar(expresion);
        
        reverse(tokens.begin(), tokens.end());
        for (auto& t : tokens) {
            if (t == "(") t = ")";
            else if (t == ")") t = "(";
        }

        // Usamos tu clase personalizada
        MiPila<string> pila_operadores;
        vector<string> salida_postfija;

        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                while (!pila_operadores.empty() && pila_operadores.top() != "(" && 
                       precedencia(pila_operadores.top()) > precedencia(token)) {
                    salida_postfija.push_back(pila_operadores.top());
                    pila_operadores.pop();
                }
                pila_operadores.push(token);
            } 
            else if (token == "(") {
                pila_operadores.push(token);
            } 
            else if (token == ")") {
                while (!pila_operadores.empty() && pila_operadores.top() != "(") {
                    salida_postfija.push_back(pila_operadores.top());
                    pila_operadores.pop();
                }
                if (pila_operadores.empty()) {
                    throw invalid_argument("Paréntesis desbalanceados");
                }
                pila_operadores.pop(); 
            } 
            else {
                salida_postfija.push_back(token);
            }
        }

        while (!pila_operadores.empty()) {
            if (pila_operadores.top() == "(") {
                throw invalid_argument("Paréntesis desbalanceados");
            }
            salida_postfija.push_back(pila_operadores.top());
            pila_operadores.pop();
        }

        reverse(salida_postfija.begin(), salida_postfija.end());
        return salida_postfija;
    }

    double evaluarPrefija(const vector<string>& tokens_prefijos) {
        // Usamos tu clase personalizada
        MiPila<double> pila;

        for (auto it = tokens_prefijos.rbegin(); it != tokens_prefijos.rend(); ++it) {
            string token = *it;

            if (token == "+" || token == "-" || token == "*" || token == "/") {
                if (pila.size() < 2) throw invalid_argument("Faltan operandos");
                
                double op1 = pila.top(); pila.pop();
                double op2 = pila.top(); pila.pop();

                if (token == "+") pila.push(op1 + op2);
                else if (token == "-") pila.push(op1 - op2);
                else if (token == "*") pila.push(op1 * op2);
                else if (token == "/") {
                    if (op2 == 0.0) throw runtime_error("División por cero detectada");
                    pila.push(op1 / op2);
                }
            } 
            else {
                try {
                    size_t pos;
                    double valor = stod(token, &pos);
                    if (pos != token.length()) throw invalid_argument("No es un número puro");
                    pila.push(valor);
                } 
                catch (const invalid_argument&) {
                    if (variables.find(token) == variables.end()) {
                        throw invalid_argument("Variable no definida: " + token);
                    }
                    pila.push(variables[token]);
                }
            }
        }

        if (pila.size() != 1) throw invalid_argument("Sobran operandos en la expresión");
        
        return pila.top();
    }
};

int main() {
    unordered_map<string, double> valores = {
        {"A", 10.0}, {"B", 5.5}, {"C", 2.0}, 
        {"D", 100.0}, {"E", 0.0}, {"F", 4.2}
    };

    EvaluadorPrefijo evaluador(valores);

    vector<string> expresiones = {
        "(A+B)*(C+D)*(E+F)",
        "A+((B+C)*(D+E))",
        "A*B*C*D+E+F"
    };

    cout << "--- EVALUACION CON PILA PERSONALIZADA ---\n\n";

    for (const auto& exp : expresiones) {
        try {
            cout << "Infija Original : " << exp << "\n";
            vector<string> prefija = evaluador.infijaAPrefija(exp);
            
            cout << "Formato Prefijo : ";
            for (const auto& t : prefija) cout << t << " ";
            cout << "\n";

            double resultado = evaluador.evaluarPrefija(prefija);
            cout << "Resultado       : " << resultado << "\n\n";
        } catch (const exception& e) {
            cout << "ERROR al evaluar: " << e.what() << "\n\n";
        }
    }

    return 0;
}