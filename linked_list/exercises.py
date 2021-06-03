# from .linked_list import LinkedStack, LinkedQueue, LinkedDeque

class EmptyList(Exception):
    pass


class SinglyLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node._element
            node = node._next

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise EmptyList("empty list")
        return self._head._element

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyList("empty list")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

    def swap(self, x, y):
        pass


def concat_lists(L, M):
    if not isinstance(L, SinglyLinkedList) and not isinstance(M, SinglyLinkedList):
        raise TypeError("pass instance of SinglyLinkedList")
    for i in M:
        L.push(i)
    return L


def last_node_singly_list(L):
    if not isinstance(L, SinglyLinkedList):
        return TypeError("L must be aa instance of type SinglyLinkedList")
    s = len(L)
    i = s - 1
    for j in L:
        if i == s:
            return j
        s -= 1


def counts_nodes_recursively(L, size):
    if not isinstance(L, SinglyLinkedList):
        raise TypeError("L is not an instance of type SinglyLinkedList")
    if size == 0:
        return 0
    else:
        nodes = L.first()
        return counts_nodes_recursively(L, size - 1)


if __name__ == '__main__':
    l = SinglyLinkedList()
    m = SinglyLinkedList()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(6000)
    m.push(10)
    m.push(20)
    m.push(30)
    m.push(40)
    m.push(5000)
    # newL = concat_lists(l,m)
    # for i in newL:
    #     print(i)
    print(last_node_singly_list(m))
