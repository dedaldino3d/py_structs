from trees.abc import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:
        """Non public class for storing a node"""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element at this position """
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    # --------------- utility methods -----------------------------
    def _validate(self, p):
        """Return associated node if position p is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            return ValueError("p does not belongs to this container")
        if p._node._parent is p._node:
            return ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        """Return the position instance for the given Node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    # ----------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # ----------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size

    def root(self):
        """Return the root position of the tree (or None if empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left child (or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child (or None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """ 
            Create a root for an empty tree, storing e as the element,
            and return the position of that root; an error occurs if the
            tree is not empty
        """
        if self._root is not None:
            raise ValueError("root exists")
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """ 
            Create a new node storing element e, link the node as the
            left child of position p, and return the resulting position;
            an error occurs if p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left child exists")
        node._left = self._Node(e, node)  # node is its parent
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, p, e):
        """ 
            Create a new node storing element e, link the node as the
            right child of position p, and return the resulting position;
            an error occurs if p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("right child exists")
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def replace(self, p, e):
        """ 
            Replace the element stored at position p with element e,
            and return the previously stored element.
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """ 
            Remove the node at position p, replacing it with its child,
            if any, and return the element that had been stored at p;
            an error occurs if p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if child is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def attach(self, p, t1, t2):
        """ 
            Attach the internal structure of trees t1 and t2, respectively, as the left and right subtrees of leaf position p of
            T, and reset t1 and t2 to empty trees; an error condition
            occurs if p is not a leaf.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):  # all trees must be same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attach t2 as right subtree of node
            t2._root._parent = node
            node._left = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0

    def delete_subtree(self, p):
        node = self._validate(p)
        parent = node._parent
        if node is parent._left:
            parent._left = None
        else:
            parent._right = None
        h = self.num_children(p) + 1
        self._size -= h


class MutableLinkedBinaryTree(LinkedBinaryTree):
    def add_left(self, p, e):
        pass

    def add_right(self, p, e):
        pass

    def add_root(self, e):
        pass

    def delete(self, p):
        pass

    def attach(self, p, t1, t2):
        pass

    def replace(self, p, e):
        pass
