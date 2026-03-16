#include "Class_Ej_16.hpp"

int main() {
    PriorityQueueDLL pq;
    pq.enqueue("TareaA", 2);
    pq.enqueue("TareaB", 5);
    pq.enqueue("TareaC", 1);
    
    while (!pq.isEmpty()) {
        std::cout << pq.dequeue() << std::endl;
    }
    return 0;
}