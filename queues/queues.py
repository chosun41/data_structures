class Queue:
    def __init__(self,limit=10):
        self.array = []
        self.limit=limit
    def size(self):
        return len(self.array)
    def isEmpty(self):
        return len(self.array) == 0
    def isFull(self):
        return len(self.array) == self.limit
    def front(self):
        if self.isEmpty():
            return None
        return self.array[0]
    def dequeue(self):
        if self.isEmpty():
            raise Exception("QueueUnderflow")
        return self.array.pop(0)
    def enqueue(self, data):
        if self.isFull():
            raise Exception("QueueOverflow")
        self.array.append(data)

if __name__ == "__main__":

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.front())
