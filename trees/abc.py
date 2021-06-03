from linked_list.linked_list import LinkedQueue


class Tree:
    """Abstract Base Class representing a tree data structure"""

    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at position p"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """"The opposite of __eq__"""
            return not (self == other)

    def root(self):
        """Return the position of the root of tree T, or None if T is empty"""
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """Return True if position p is the root of T"""
        return self.root() == p

    def parent(self, p):
        """Return the position of the parent of position p, or None if p is the root of T"""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children of position p"""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of the children of position p"""
        raise NotImplementedError("must be implemented by subclass")

    def is_leaf(self, p):
        """Return True if position p does not contain any positions"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree T not contain any positions"""
        return len(self) == 0

    def positions(self):
        """Generate an iteration of all position of tree T"""
        return self.preorder()

    def __iter__(self):
        """Generate an iteration of all elements stored within tree T"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions int the tree"""
        if not self.is_empty():
            for p in self._sub_tree_preorder(self.root()):
                yield p  # visit p

    def _sub_tree_preorder(self, p):
        """Generate a preorder iteration of position in the tree, Non-public"""
        yield p  # visit p before its subtrees
        for c in self.children(p):  # for each child c
            for other in self._sub_tree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        """Generate a postorder iteration of position in the tree"""
        if not self.is_empty():
            for p in self._sub_tree_postorder(self.root()):
                yield p

    def _sub_tree_postorder(self, p):
        """Generate a postorder iteration of position in the tree, Non-public"""
        for c in self.children(p):
            for other in self._sub_tree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a Breadth-First iteration of the positions of the tree"""
        if not self.is_empty():
            ge = LinkedQueue()  # known positions not yet yielded
            ge.enqueue(self.root())  # starting with the root
            while not ge.is_empty():
                p = ge.dequeue()  # remove from front of the queue
                yield p  # report this position
                for c in self.children(p):
                    ge.enqueue(c)  # add children to back of queue

    def __len__(self):
        """Return the number of position (and hence elements) that are contained in tree T"""
        raise NotImplementedError("must be implemented by subclass")

    def depth(self, p):
        """
        Return the number of levels separating position p from the root

        Complexity: O(dp + 1)        
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self, p):
        """
        Return the height of the subtree rooted at Position p

        Complexity: O(n)        
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(i) for i in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p
        If p is None, then return the height of the entire  tree

        Complexity: O(n)
        """
        if p is None:
            p = self.root()
        return self._height2(p)


class BinaryTree(Tree):
    """Abstract base class representing a binary tree data structure"""

    # --------------------- abstract methods ------------------------
    def left(self, p):
        """Return a position representing p's left child
            Return None if p does not contain a left child
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """
            Return a position representing p's right child

            Return None if p does not contain a right child
        """
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ------------------
    def sibling(self, p):
        """Return a Position representing p sibling (or None if p does not contain siblings)"""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root as no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def num_children(self, p):
        c = 0
        if self.left(p) is not None:
            c += 1
        if self.right(p) is not None:
            c += 1
        return c

    def children(self, p):
        """"Generate an iteration of Position's representing p's children    """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for c in self._sub_tree_inorder(self.root()):
                yield c

    def _sub_tree_inorder(self, p):
        """Generate an inorder iteration of position int the tree"""
        if self.left(p) is not None:  # if left exists traverse its subtree
            for c in self._sub_tree_inorder(self.left(p)):
                yield c
        yield p  # visit p between its subtrees
        if self.right(p) is not None:  # if right exists traverse its subtree
            for c in self._sub_tree_inorder(self.right(p)):
                yield c

    def positions(self):
        """
            Override inherited version from super class to make inorder the default

            Generate an iteration of the tree's positions
        """
        return self.inorder()
