class MyCircularQueue {
public:
    MyCircularQueue(int k) {
        a_size = k;
        cq.resize(k);
    }
    
    bool enQueue(int value) {
        if (isFull()) 
            return false;
        if (isEmpty()){
            head = tail = 0;
            cq[tail] = value;
            size++;
            return true;
        }
        tail++;
        tail %= a_size;
        cq[tail] = value;
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        
        head = (head + 1) % a_size;
        size--;
        return true;
    }
    
    int Front() {
        return isEmpty() ? -1 : cq[head];
    }
    
    int Rear() {
        return isEmpty() ? -1 : cq[tail];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == a_size;
    }
    
    private:
        int head = 0, tail = 0, size = 0, a_size = 0;
        vector<int> cq;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */