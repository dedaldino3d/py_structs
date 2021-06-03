from linked_list.linked_list import PositionalList
from queue import EmptyQueue


class PriorityQueueBase:
    """Abstract base class for a Priority Queue"""

    class _Item:
        """Lightweight composite to store key and value"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

        def __gt__(self, other):
            return self._key > self._key

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if priority queue is empty"""
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        """Create new empty Priority Queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def _find_min(self):
        """Return position of minimum key"""
        if self.is_empty():
            raise EmptyQueue("priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.elment():
                small = walk

            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """Add a key-value pair"""
        self._data.add_last(self._Item(key, value))

    def minimum(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value,)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value,)


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with sorted list"""

    def __init__(self):
        """Create a new empty priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        newest = self._Item(key, value)  # make a Item instance
        walk = self._data.last()  # walk backward looking for smaller value
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)  # new key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        if self.is_empty():
            raise EmptyQueue("priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minum key"""
        if self.is_empty():
            raise EmptyQueue("priority queue is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
