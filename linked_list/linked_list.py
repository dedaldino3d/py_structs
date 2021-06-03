class EmptyLinkedList(Exception):
    pass


class Linked:
    """Base class for Linked Lists (or Stacks, Queues, Deques)"""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):  # initializes node's fields
            self._element = element
            self._next = next

    def __init__(self):
        self._size = 0

    def is_empty(self):
        return self._size == 0


class LinkedStack(Linked):

    def __init__(self):
        super().__init__()
        self._head = None

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyLinkedList("Linked list is empty")
        a = self._head._element
        self._head = self._head._next
        self._size -= 1
        return a

    def top(self):
        if self.is_empty():
            raise EmptyLinkedList("Linked list is empty")
        return self._head._element


class LinkedQueue(Linked):
    def __init__(self):
        super().__init__()
        self._head = None
        self._tail = None

    def __iter__(self):
        node = self._head
        s = self._size
        while s > 0:
            yield node._element
            node = node._next
            s -= 1

    def first(self):
        if self.is_empty():
            raise EmptyLinkedList("Linked queue is empty")
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyLinkedList("Linked queue is empty")
        a = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return a

    def rotate(self):
        if self.is_empty():
            raise EmptyLinkedList("Linked queue is empty")
        next = self._head._next
        self._tail._next = self._head
        self._head = next

    def _extend(self, q):
        """
        Extend a LinkedQueue with another queue
        :param q: Queue to add
        :return: q
        """
        if not isinstance(q, LinkedQueue):
            raise ValueError("q must be a LinkedQueue instance")

        if self.is_empty():
            pass


class LinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, e):
        if self._size == 0:
            raise EmptyLinkedList()
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise EmptyLinkedList()
        a = self._head._element
        self._head = self._head._next
        self._size -= 1
        return a


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._size = 0
        self._tail = None

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyLinkedList()
        head = self._tail._next
        return head._element

    def last(self):
        if self.is_empty():
            raise EmptyLinkedList()
        return self._tail._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        oldHead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldHead._next
        self._size -= 1
        return oldHead._element

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, e):
        predecessor = e._prev
        successor = e._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = e._element
        e._prev = e._next = e._element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    def __init__(self):
        super().__init__()
        pass

    def first(self):
        if self.is_empty():
            raise EmptyLinkedList("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise EmptyLinkedList("Deque is empty")
        return self._trailer._prev._element

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise EmptyLinkedList("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise EmptyLinkedList("Deque is empty")
        return self._delete_node(self._trailer._prev)


class PositionalList(_DoublyLinkedBase):
    """A sequencial container of elements allowing positional access"""

    # ! CHECK ALGORITHMS [add_first, __iter__, make_position] and class Position,
    # ! do not iterating all entries in the List when call __iter__

    class Position:
        """An abstract Position representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """"Return the element stored at this position"""
            return self._node._element

        def __eq__(self, other):
            """Return true if other is a Positional representing the same location """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return false if other represent the same location"""
            return not (self == other)

    # --------------------------------- utility method -----------------------------

    def _validate(self, p):
        """Return position's node or raise an appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # conversion for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node(or None if sentinel)"""
        if node is self._header or node is self._trailer:
            print("not make_position", node)
            return None  # boundary violation
        else:
            print("make_position", node)
            return self.Position(self, node)  # legitimate position

    # -------------------------- accessors ---------------------------

    def first(self):
        """Return the first position in the list"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the position just before Position p (or None if invalid)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """"Return the position just after Position p (or None if invalid)"""
        node = self._validate(p)
        print("after ", node)
        print("node._next", node._next)
        return self._make_position(node._next)

    def __iter__(self):
        """Generates a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            print("iter ", cursor)

    # ------------------------------- mutators ---------------------------

    def _insert_between(self, e, predecessor, successor):
        """
        Override inherited version to return Position, rather than Node
        Add element between existing nodes and return new Position.
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """"Add element to first position in the list"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Add element to last position in the last"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Add element e into list before Position p return new Position"""
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        """Add element e into list after Position p return new Position"""
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """
            Replace element at position p with element e

            Return the element formerly at Position p.
        """
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value

    def find(self, e):
        """Find an element, return e if found, None otherwise"""
        cursor = self.first()
        while cursor is not None:
            if cursor.element() == e:
                print(cursor.element(), end=" ")
            else:
                print(cursor)
                cursor = self.after(cursor)
                print(cursor)
        return None


if __name__ == '__main__':
    p = PositionalList()
    pos = [p.add_first(2), p.add_first(3), p.add_first(4)]
    # pos.append(p.add_first(1))
    for i in p:
        print(i)
