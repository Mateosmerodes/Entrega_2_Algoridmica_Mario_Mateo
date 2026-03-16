#include <iostream>
#include <string>

class DoubleNode {
public:
    std::string key;
    int priority;
    DoubleNode* next;
    DoubleNode* prev;
    
    DoubleNode(std::string k, int p) : key(k), priority(p), next(nullptr), prev(nullptr) {}
};

class PriorityQueueDLL {
private:
    DoubleNode* head;
    DoubleNode* tail;
public:
    PriorityQueueDLL() : head(nullptr), tail(nullptr) {}
    
    void enqueue(std::string key, int priority) {
        DoubleNode* newNode = new DoubleNode(key, priority);
        if (!head) {
            head = tail = newNode;
            return;
        }
        if (head->priority < priority) {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
            return;
        }
        DoubleNode* current = head;
        while (current->next && current->next->priority >= priority) {
            current = current->next;
        }
        newNode->next = current->next;
        if (current->next) current->next->prev = newNode;
        else tail = newNode;
        current->next = newNode;
        newNode->prev = current;
    }
    
    std::string dequeue() {
        if (!head) return "";
        DoubleNode* temp = head;
        std::string res = temp->key;
        head = head->next;
        if (head) head->prev = nullptr;
        else tail = nullptr;
        delete temp;
        return res;
    }
    
    bool isEmpty() { return head == nullptr; }
};