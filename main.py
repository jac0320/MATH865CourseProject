import matpolotlib.pyplot as plt;
from pylab import rcParams;
import unittest, sys;
import random;

def plot_node(node, level = 1, posx = 0, posy = 0):
    """Graphical Representation of the tree. Perform a DFS travel..."""
    width = 2000.0 * (0.5**(level))
    if node._color == 'RED':
        plt.text(posx, posy, str(node._data), horizontalalignment='center',fontsize=10,color='r');
    else:
        plt.text(posx, posy, str(node._data), horizontalalignment='center',fontsize=10);
    if node.left:
        px = [posx, posx-width]
        py = [posy-2, posy-15]
        plt.plot(px,py,'b-',hold=True)
        plot_node(node._left, level+1, posx-width, posy-20)
    if node.right:
        plot_node(node._right, level+1, posx+width, posy-20)
        px = [posx, posx+width]
        py = [posy-2, posy-15]
        plt.plot(px,py,'b-',hold=True)

def plot_tree(node, figsize=(10,6)):
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node)
    plt.show()

class TreeNode(object):
        """
        #TODO: Description
        """
        def __init__(self,data,left_child=None,right_child=None):
            """Some basic properties that I am thinking of..."""
            self._data = data;
            self._left = left_child;
            self._right = right_child;
            self._color = 'RED'    #TODO: may need modification
            self._parent = None

        def _find_parent(self):
            """Find the parent of a tree node. Could be None."""
            return self._parent

        def _find_grandparent(self):
            """Find the grand parent of a tree node. If grand parent
                not exist, return None."""
            if self._parent is None:
                return None
            else:
                parent_node = self._parent
                return parent_node._parent # Node Sure about this

        def _find_uncle(self):
            """Find the uncle of a tree node, namely it's grandparent's other child.
                If parent is None or no grandparent, return None."""
            if self._parent is None or self._find_grandparent() is None:
                return None
            else:
                grandpa = self._find_grandparent();
                if self._parent == grandpa._left:
                    return grandpa._right
                else:
                    return grandpa._left

        def _find_left(self):
            """Find left child of a tree node, return None if not exist"""
            return self._left;

        def _find_right(self):
            """Find right child of a tree node, return None if not exist"""
            return self._right;

        def _set_parent(self,parent):
            """Update a node's parent"""
            # May have issue, need test...
            self._parent = parent;

        def _set_left(self,left_child):
            """Update a node's left child with a new tree node."""
            self._left = left_child;

        def _set_right(self,right_child):
            """Update a node's right child with a new tree node."""
            self._right = right_child

        def _set_color(self,color):
            """Set a tree node to a new color"""
            if color == 'RED' or color == 'BLACK':
                self._color = color;
            else:
                print "Typo! Typo! Use only 'RED' or 'BLACK' for color"

        def _rotate_left(self):
            #Implementation going on... Not sure if needed...
            #
            """This function rotate a tree node from right to left
                    x             y
                   / \           / \
                  t  y    ->    x  t
                    / \        / \
                   t  t       t  t
            This can be a useful function called when re-balancing the tree.
            """
            if self._right is None:
                return
            else:
                new_head = self._right;
                self._right = new_head._left;
                if new_head._left is None:
                    new_head._left._parent = self;
                new_head._parent = self._parent;
                if self._parent is None:
                    self.tree = new_head; #Not sure how this should go...
                elif self is self._parent._left:
                    self._parent._left = new_head;
                else:
                    self._parent._right = new_head;
                new_head._left = self;
                self._parent = new_head;

        def _rotate_right(self):
            #Implementation going on... Not sure if needed...
            #
            """This function rotate a tree node from left to right
                    x             y
                   / \           / \
                  y  t    ->    t  x
                 / \              / \
                t  t             t  t
            This can be a useful function called when re-balancing the tree.
            """
            if self._left is None:
                pass
            else:
                new_head = self._left;
                self._left = new_head._right;
                if new_head._right is not None:
                    new_head._right._parent = self;
                new_head._parent = new_head._parent;
                if self._parent is None:
                    BinarySearchTree.tree = new_head;
                elif self is self._parent._right:
                    self._parent._right = new_head;
                else:
                    self._parent._left = new_head;
                new_head._right = self;
                self._parent = new_head

        def traverse_infix(self, result = None):
            if result == None:
                result = []
            if self._left:
                self._left.traverse_infix(result)
            result.append(self._data)
            if self._right:
                self._right.traverse_infix(result)
            return result

        def traverse_prefix(self, result = None):
            if result == None:
                result = []
            result.append(self._data)
            if self._left:
                self._left.traverse_infix(result)
            if self._right:
                self._right.traverse_infix(result)
            return result

        def traverse_postfix(self, result = None):
            if result == None:
                result = []
            if self._left:
                self._left.traverse_infix(result)
            if self._right:
                self._right.traverse_infix(result)
            result.append(self._data)
            return result

class BinarySearchTree(object):
    """This is the object of binary search tree"""
    def __init__(self):
        self.tree = None

    def _find_node(self, node, obj):
        if node == None:
            return None
        if node._data == obj:
            return node
        if obj < node._data:
            return self._find_node(node._left, obj)
        else: # so obj > node.data
            return self._find_node(node._right, obj)

    def is_element(self, obj):
        node = self._find_node(self.tree, obj)
        if node:
            return True
        else:
            return False

    def _insert(self, node, obj):
        if obj < node._data:
            if node._left:
                self._insert(node.left, obj)
            else:
                node._left = TreeNode(obj)
        elif obj > node.data:
            if node._right:
                self._insert(node._right, obj)
            else:
                node._right = TreeNode(obj)
        else:
            pass

    def insert(self, obj):
        if self.tree == None:
            self.tree = TreeNode(obj)
        else:
            self._insert(self.tree, obj)

    def _replace_child(self, node, old, new):
        if node==None:
            self.tree = new
        elif node._left == old:
            node._left = new
        elif node._right == old:
            node._right = new
        else:
            assert(False) #May need to change

    def _delete_node(self, parent, node, obj):
        if node == None:
            return
        if obj < node._data:
            self._delete_node(node, node._left, obj)
        elif obj > node._data:
            self._delete_node(node, node._right, obj)
        elif node._data == obj:
            if node._left == None:
                self._replace_child(parent, node, node._right)
            elif node.right == None:
                self._replace_child(parent, node, node._left)
            else:
                pred = node._left
                pred_parent = node
                while pred._right != None:
                    pred_parent = pred
                    pred = pred._right
                node._data = pred._data
                self._replace_child(pred_parent, pred, pred._left)
                pass

    def delete(self, obj):
        if self.tree == None:
            return
        self._delete_node(None, self.tree, obj)

class RBTree(BinarySearchTree):
    """
        Red-Black Tree is a special type of Binary Search Tree that has the ability
        of balancing itself in order to avoid uneven tree which could result in long
        computational performance when performing traversal.
    """
    def __init__(self):
        """"""
    '''
    _insert_case1: When is red-black tree is empty.
    '''
    def _insert_case1(node):
        if 


    def insert(self,node):
        self.tree

        if self.tree == None:
            self.tree = TreeNode(target)
        else:
            #TODO
        pass

    def delet(self,x):
        pass

class TestRBTree(unittest.TestCase):
    def test_insert_small_random(self):
        small_random = [];
        rbt = RBTree();
        for i in range(10):
            target = random.random();
            small_random.append(target)
            rbt.insert(target);
        ####NOT FINISHED...



