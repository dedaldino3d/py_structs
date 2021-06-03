import time, sys


class EmptyQueue(Exception):
    pass


class ArrayQueue:
    """FIFO Queue implementation using a Python list as underlying storage"""
    DEFAULT_CAPACITY = 10  # moderate capacity for all queues

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        """Add element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            raise EmptyQueue("Queue is empty")
        a = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._size -= 1
        return a

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Queue is empty")
        return self._data[self._front]

    def benchmark(self, n):
        """Compute a simple benchmark for enqueue and dequeue operation """
        i = time.time()
        for i in range(n):
            self.enqueue(i)
            if i % 4 == 0:
                print(f"Size: {self._size} Bytes: {sys.getsizeof(self._data)}")
        f = time.time()
        print('\n')
        i2 = time.time()
        for i in range(n):
            self.dequeue()
            if i % 4 == 0:
                print(f"Size: {self._size} Bytes: {sys.getsizeof(self._data)}")
        f2 = time.time()
        print('\n')
        print(f"Elapsed enqueue time: {f - i}\nElapsed dequeue time: {f2 - i2}")

    def _resize(self, c):
        old = self._data
        self._data = [None] * c  # allocate list with new capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


class Deque:
    """Implementation of a double ended queue, known as deque"""
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=None):
        """
        :param capacity: default capacity when full raise a deque full exception
        """
        self._data = [None] * (capacity or Deque.DEFAULT_CAPACITY)
        print("capacity: ", len(self._data))
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def last(self):
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        l = (self._front + self._size - 1) % len(self._data)
        self._data[l + 1] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise EmptyQueue("Deque is empty")
        a = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)  # shrink the underlying array
        return a

    def delete_last(self):
        if self.is_empty():
            raise EmptyQueue("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        l = self._data[back]
        self._data[back] = None
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._size -= 1
        return l

    def _resize(self, cap):
        old = self._data
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(self._data)
        self._front = 0


if __name__ == '__main__':
    deque = Deque(100)
    deque.add_first(1)
    deque.add_first(2)
    deque.add_first(3)
    deque.add_first(4)
    deque.delete_first()
    deque.delete_last()
    deque.add_last(30)
    deque.add_last(40)
    deque.add_last(50)
    deque.add_last(9000)
    print(deque.first())
    print(deque.last())
