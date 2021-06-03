from trees.trees_ds import BinaryTree, LinkedBinaryTree


def count_leaves_in_binary_tree_parents(T, p=None):
    """
    Counts the number of leaves in a Binary Tree that are left child of their respective parent
    :return number of leaves
    """
    # if not isinstance(T, BinaryTree):
    #     raise TypeError("tree argument must be an instance of BinaryTree, got: ", type(T))
    c = 0
    print("count up: ", c)
    if p is None:
        p = T.root()
    print(p.element())
    if T.is_leaf(p):
        c += 1
        if T.sibling(p):
            print("sibling: ", c, p.element())
            return count_leaves_in_binary_tree_parents(T, T.left(T.sibling(p)))
        return c
    if T.left(p) is None and T.right(p) is None:
        return 0
    else:
        return count_leaves_in_binary_tree_parents(T, T.left(p))


def count_leaves_tree_parents(T):
    """
    Counts the number of leaves in a Binary Tree that are left child of their respective parent
    :return number of leaves
    """
    if not isinstance(T, (BinaryTree, LinkedBinaryTree)):
        raise TypeError("tree argument must be an instance of BinaryTree, got: ", type(T))
    cc = 0
    for c in T.preorder():
        if T.is_root(c):
            pass
        else:
            pa = T.parent(c)
            if T.left(pa) == c and T.is_leaf(c):
                cc += 1
    return cc


def btree_character():
    t = LinkedBinaryTree()
    p = t.add_root('E')
    p1 = t.add_left(p, 'X')
    p2 = t.add_right(p1, 'U')
    p = t.add_left(p1, 'A')
    t.add_right(p, 'F')
    t.add_right(p2, 'N')
    t.add_left(p, 'M')

    print("Preorder: ", end="")
    for c in t.preorder():
        print(c.element(), end=' ')
    print("\nInorder: ", end="")
    for c in t.inorder():
        print(c.element(), end=' ')
    print('\n')


def post_pre_traversal():
    T = LinkedBinaryTree()
    r = T.add_root(1)
    r1 = T.add_left(r, 2)
    T.add_right(r, 3)
    T.add_right(r1, 4)
    T.add_left(r1, 5)
    a = [c.element() for c in T.preorder()]
    b = [c.element() for c in T.postorder()]
    print("a: ", a)
    print("b: ", b)


def breadth_traversal_count():
    T = LinkedBinaryTree()
    r = T.add_root(1)
    r1 = T.add_left(r, 2)
    r2 = T.add_right(r, 3)
    r3 = T.add_left(r1, 4)
    r4 = T.add_right(r1, 6)
    r5 = T.add_left(r2, 7)
    r6 = T.add_right(r2, 8)
    T.add_left(r3, 9)
    T.add_right(r3, 10)
    T.add_left(r4, 11)
    T.add_right(r4, 12)
    T.add_left(r5, 13)
    T.add_right(r5, 14)
    T.add_left(r6, 15)
    T.add_right(r6, 16)

    for c in T.breadthfirst():
        print(c.element())


def in_ext_tree_nodes():
    T = LinkedBinaryTree()
    r = T.add_root(1)
    r1 = T.add_left(r, 2)
    r2 = T.add_right(r, 3)
    r3 = T.add_left(r1, 4)
    r4 = T.add_right(r1, 6)
    r5 = T.add_left(r2, 7)
    r6 = T.add_right(r2, 8)
    T.add_left(r3, 9)
    T.add_right(r3, 10)
    T.add_left(r4, 11)
    T.add_right(r4, 12)
    T.add_left(r5, 13)
    T.add_right(r5, 14)
    T.add_left(r6, 15)
    T.add_right(r6, 16)

    int_depth = 0
    ext_depth = 0
    proper = False
    nodes = 0
    for p in T.positions():
        if T.is_leaf(p) or T.num_children(p) == 2:
            nodes += 1
        if not T.is_leaf(p):
            int_depth += T.depth(p)
        else:
            ext_depth += T.depth(p)
    if nodes == len(T):
        proper = True
        print("Proper Binary Tree")
    print(f"int_depth: {int_depth} == ext_depth: {ext_depth}")


def d_omega_tree(T):
    n_c = 0
    for c in T.positions():
        if T.is_leaf(c):
            n_c += T.depth(c)
    return n_c


def is_isomorphic(T1, T2):
    if not isinstance(T1, (BinaryTree, LinkedBinaryTree)) and not isinstance(T2, (BinaryTree, LinkedBinaryTree)):
        raise ValueError("T1 and T2 must be an instance of BinaryTree or LinkedBinaryTree")
    if T1.is_empty() and T2.is_empty():
        return True
    if not len(T1) and len(T2):
        return False
    t1_pos = [i.element() for i in T1.positions()]
    t2_pos = [i.element() for i in T2.positions()]
    if t1_pos == t2_pos:
        return True
    return False


def test_delete_subtree():
    T = LinkedBinaryTree()
    r = T.add_root(1)
    r1 = T.add_left(r, 2)
    r2 = T.add_right(r, 3)
    r3 = T.add_left(r1, 4)
    r4 = T.add_right(r1, 6)
    r5 = T.add_left(r2, 7)
    r6 = T.add_right(r2, 8)
    T.add_left(r3, 9)
    T.add_right(r3, 10)
    T.add_left(r4, 11)
    T.add_right(r4, 12)
    r10 = T.add_left(r5, 13)
    T.add_right(r5, 14)
    T.add_left(r6, 15)
    T.add_right(r6, 16)
    print("Elements len: ", len(T))
    print("Elements: ")
    for c in T.positions():
        print(c.element(), end=" ")
    T.delete_subtree(r3)
    print("Elements len after: ", len(T))
    print("Elements after: ")
    for c in T.positions():
        print(c.element(), end=" ")
    T.delete_subtree(r6)
    print("2 Elements len after: ", len(T))
    print("2 Elements after: ")
    for c in T.positions():
        print(c.element(), end=" ")
    T.delete_subtree(r10)
    print("\n3 Elements len after: ", len(T))
    print("3 Elements after: ")
    for c in T.positions():
        print(c.element(), end=" ")


def compute_print_positions(T):
    for p in T.positions():
        print("Element: {} ==> subtree height: {}".format(p.element(), T.height(p)))

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    p = tree.add_root("deda1")
    p1 = tree.add_left(p, "deda3")
    p2 = tree.add_right(p, "deda4")
    p3 = tree.add_left(p1, "deda5")
    p4 = tree.add_right(p1, "deda6")
    tree.add_left(p2, "deda7")
    tree.add_right(p2, "deda8")
    tree.add_left(p3, "deda9")
    tree.add_right(p3, "deda10")
    tree.add_left(p4, "deda11")

    # i = count_leaves_in_binary_tree_parents(tree)
    # i = count_leaves_tree_parents(tree)
    # print("i: ", i)
    # btree_character()
    # post_pre_traversal()
    # breadth_traversal_count()
    # in_ext_tree_nodes()
    T = LinkedBinaryTree()
    r = T.add_root(1)
    r1 = T.add_left(r, 2)
    r2 = T.add_right(r, 3)
    r3 = T.add_left(r1, 4)
    r4 = T.add_right(r1, 6)
    r5 = T.add_left(r2, 7)
    r6 = T.add_right(r2, 8)
    T.add_left(r3, 9)
    T.add_right(r3, 10)
    T.add_left(r4, 11)
    T.add_right(r4, 12)
    r10 = T.add_left(r5, 13)
    T.add_right(r5, 14)
    T.add_left(r6, 15)
    T.add_right(r6, 16)
    # print("is_isomorphic: ", is_isomorphic(T, tree))
    compute_print_positions(T)
    