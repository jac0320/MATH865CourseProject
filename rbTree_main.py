import matplotlib
matplotlib.use('TKAgg')
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
import matplotlib.pyplot as plt;
from pylab import rcParams;
import unittest, sys;
import random;

# Plotting area...

def plot_node(node, level=1, posx=0, posy=0):
    """Graphical Representation of the tree. Perform a DFS travel..."""
    width = 2000.0 * (0.5 ** (level))
    if node._color == 'RED':
        plt.text(posx, posy, str(node._data), horizontalalignment='center', fontsize=10, color='r');
    else:
        plt.text(posx, posy, str(node._data), horizontalalignment='center', fontsize=10);
    if node._left._data is not None:
        px = [posx, posx - width]
        py = [posy - 2, posy - 15]
        plt.plot(px, py, 'b-', hold=True)
        plot_node(node._left, level + 1, posx - width, posy - 20)
    if node._right._data is not None:
        plot_node(node._right, level + 1, posx + width, posy - 20)
        px = [posx, posx + width]
        py = [posy - 2, posy - 15]
        plt.plot(px, py, 'b-', hold=True)

def plot_tree(node, figsize=(10, 6)):
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node,1,500)
    plt.show()

# Plotting area...

class NullTreeNode(object):
    def __init__(self):
        self._data = None;
        self._left = None;
        self._right = None;
        self._parent = None;
        self._color = "BLACK"
        pass

class TreeNode(object):
    """
        A leaf of a the tree is constructed in here. Since we have a binary tree, each node
        has at most two children. The left child is the smaller child and the right child is
        the bigger child. Or you can call minimum and maximum if you prefer.
                Node
                /  \
              min  max
        The object contains the following properties:
            _data | _left | _right | _color | _parent;
            - _data: represent the value of the tree node/leaf;
            - _left: denotes the left child(object) of the node. It's _data should be less than leaf's value;
            - _right: denotes the right child(object) of the node. It's _data should be grater than leaf's value;
            - _color: denotes the color of the node. Only "BLACK" or "RED" is allowed to describe the color;
            - _parent: denotes the parent(object) of a leaf;
        """

    def __init__(self, data, left_child=None, right_child=None):
        self._data = data;
        self._left = NullTreeNode();
        self._right = NullTreeNode();
        self._color = 'RED';
        self._parent = None;

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
            return parent_node._parent  # Node Sure about this

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

    def _set_parent(self, parent):
        """Update a node's parent"""
        # May have issue, need test...
        self._parent = parent;

    def _set_left(self, left_child):
        """Update a node's left child with a new tree node."""
        self._left = left_child;

    def _set_right(self, right_child):
        """Update a node's right child with a new tree node."""
        self._right = right_child

    def _set_color(self, color):
        """Set a tree node to a new color"""
        if color == 'RED' or color == 'BLACK':
            self._color = color;
        else:
            print "Typo! Typo! Use only 'RED' or 'BLACK' for color"

    def traverse_infix(self, result=None):
        if result is None:
            result = []
        if self._left._data:
            self._left.traverse_infix(result)
        result.append(self._data)
        if self._right._data:
            self._right.traverse_infix(result)
        return result

    def traverse_prefix(self, result=None):
        if result is None:
            result = []
        result.append(self._data)
        if self._left._data:
            self._left.traverse_infix(result)
        if self._right._data:
            self._right.traverse_infix(result)
        return result

    def traverse_postfix(self, result=None):
        if result is None:
            result = []
        if self._left._data:
            self._left.traverse_infix(result)
        if self._right._data:
            self._right.traverse_infix(result)
        result.append(self._data)
        return result

class BinarySearchTree(object):
    """This is the object of binary search tree"""

    def __init__(self):
        self.tree = None;
        self._height = 0;

    def _find_node(self, node, target):
        if node is None:
            return None
        if node._data == target:
            return node
        if target < node._data:
            return self._find_node(node._left, target)
        else:  # so target > node.data
            return self._find_node(node._right, target)

    def is_element(self, target):
        node = self._find_node(self.tree, target)
        if node:
            return True
        else:
            return False

    def _insert(self, node, target):
        if target < node._data:
            if node._left._data:
                self._insert(node._left, target)
            else:
                InsertNode = TreeNode(target);
                node._left = InsertNode;
                node._left._parent = node;

        elif target > node._data:
            if node._right._data:
                self._insert(node._right, target)
            else:
                InsertNode = TreeNode(target);
                node._right = TreeNode(target);
                node._right._parent = node;
        else:
            pass

    def insert(self, target):
        if self.tree == None:
            self.tree = TreeNode(target)
        else:
            self._insert(self.tree, target)

    def _replace_child(self, node, old, new):
        if node is None:
            self.tree = new
        elif node._left == old:
            node._left = new
            node._left._parent = node
        elif node._right == old:
            node._right = new
            node._left._parent = node
        else:
            assert (False)  # May need to change

    def _delete_node(self, parent, node, target):
        if node is None:
            return
        if target < node._data:
            self._delete_node(node, node._left, target)
        elif target > node._data:
            self._delete_node(node, node._right, target)
        elif node._data == target:
            if node._left._data is None:
                self._replace_child(parent, node, node._right)
            elif node._right._data is None:
                self._replace_child(parent, node, node._left)
            else:
                pred = node._left
                pred_parent = node
                while pred._right._data != None:
                    pred_parent = pred
                    pred = pred._right
                node._data = pred._data
                self._replace_child(pred_parent, pred, pred._left)
                pass

    def delete(self, target):
        if self.tree is None:
            return
        self._delete_node(None, self.tree, target)

    def height(self, node):
        """This function return the height of a tree starting from the """
        if self.tree is None:
            return 0
        else:
            if node._left is None:
                return self.height(node._right) + 1
            elif node._right is None:
                return self.height(node._left) + 1
            else:
                return max(self.height(node._left), self.height(node._right)) + 1

class RBTree(BinarySearchTree):
    """
        Red-Black Tree is a special type of Binary Search Tree that has the ability
        of balancing itself in order to avoid uneven tree which could result in long
        computational performance when performing traversal.

        Xiang's Note:
        _insert_case1: When the red-black tree is empty. Just add the node and paint the color to black.
    """

    def _insert_case1(self, node):
        if node._parent == None:
            node._set_color('BLACK')
        else:
            self._insert_case2(node)

    def _insert_case2(self, node):
        parent_node = node._find_parent()
        if parent_node._color == 'BLACK':
            return
        else:
            self._insert_case3(node)

    def _insert_case3(self, node):
        parent_node = node._find_parent()
        # The variable names of uncle_node and grandparent_node are different from the previous.
        uncle_node = node._find_uncle()
        grandparent_node = node._find_grandparent()
        if uncle_node._color == 'RED':
            parent_node._color = 'BLACK'
            uncle_node._color = 'BLACK'
            grandparent_node._color = 'RED'
            self._insert_case1(grandparent_node)
        else:
            self._insert_case4(node)

    def _insert_case4(self, node):
        parent_node = node._find_parent()
        grandparent_node = node._find_grandparent()

        if node == parent_node._right and parent_node == grandparent_node._left:
            self._rotate_left(parent_node)
            node = node._left
        elif node == parent_node._left and parent_node == grandparent_node._right:
            self._rotate_right(parent_node)
            node = node._right
        self._insert_case5(node)

    def _insert_case5(self, node):
        # Switch the color of current node and its parent
        parent_node = node._find_parent()
        grandparent_node = node._find_grandparent()
        parent_node._color = 'BLACK'
        grandparent_node._color = 'RED'
        if node == parent_node._left:
            self._rotate_right(grandparent_node)
        else:
            self._rotate_left(grandparent_node)

    def rb_insert(self, target):
        '''
        Convert the target to a tree node, the original color is red.
        Add it to the BinarySearchTree object.
        '''
        # node = TreeNode(target)
        self.insert(target)
        root = self.tree
        node = self._find_node(root, target)
        # TODO-1.The above, the input, node is different from target in original method, modify the previous one lated
        # TODO-2.Besides, set_parent should be added to the binarysearchtree insert method,
        # So, I'd better not heritate the binarysearchtree or modify it to be bi-directional

        # Balance the tree.
        self._insert_case1(node);

    def _find_sibling(self, target):
        if target._parent is None:
            raise "calling sibling on root"
        if target == target._parent._left:
            return target._parent._right
        else:
            return target._parent._left

    def _delete_node(self, parent, node, target):
        if node is None:
            return
        if target < node._data:
            self._delete_node(node, node._left, target)
        elif target > node._data:
            self._delete_node(node, node._right, target)
        elif node._data == target:
            if node._left._data is None:
                self._replace_child(parent, node, node._right)
            elif node._right._data is None:
                self._replace_child(parent, node, node._left)
            else:
                pred = node._left
                pred_parent = node
                while pred._right._data != None:
                    pred_parent = pred
                    pred = pred._right
                node._data = pred._data
                if pred._color is 'RED':
                    self._replace_child(pred_parent, pred, pred._left)
                elif pred._color is 'BLACK':
                    if pred._left._color is 'RED':
                        pred._left._color = 'BLACK'
                        self._replace_child(pred_parent, pred, pred._left)
                    else:
                        self._replace_child(pred_parent, pred, pred._left)
                        self._delete_case1(pred_parent._right)
                else:
                    raise "violate the RB tree rule"

    def _delete_case1(self, target):
        if target._parent is not None:
            self._delete_case2(target)

    def _delete_case2(self, target):
        brother = self._find_sibling(target)
        if brother is 'RED':
            brother._color = 'BLACK'
            target._parent = 'RED'
            if target == target._parent._left:
                self._rotate_left(target._parent)
            else:
                self._rotate_right(target._parent)
        self._delete_case3(target)

    def _delete_case3(self, target):
        brother = self._find_sibling(target)
        if target._parent._color is 'BLACK' and brother._color is 'BLACK' and brother._left._color is 'BLACK' and brother._right._color is 'BLACK':
            brother._color = 'RED'
            self._delete_case1(target._parent)
        else:
            self._delete_case4(target)

    def _delete_case4(self, target):
        brother = self._find_sibling(target)
        if target._parent._color is 'RED' and brother._color is 'BLACK' and brother._left._color is 'BLACK' and brother._right._color is 'BLACK':
            brother._color = 'RED'
            target._parent._color = 'BLACK'
        else:
            self._delete_case5(target)

    def _delete_case5(self, target):
        brother = self._find_sibling(target)
        if brother._color is 'BLACK':
            if target == target._parent._left and brother._right._color is 'BLACK' and brother._left._color is 'RED':
                brother._color = 'RED'
                brother._left._color = 'BLACK'
                self._rotate_right(brother)
            elif target == target._parent._right and brother._left._color is 'BLACK' and brother._right._color is 'RED':
                brother._color = 'RED'
                brother._right._color = 'BLACK'
                self._rotate_left(brother)
        self._delete_case6(target)

    def _delete_case6(self, target):
        brother = self._find_sibling(target)
        brother._color = target._parent._color
        target._parent._color = 'BLACK'
        if target == target._parent._left:
            brother._right._color = 'BLACK'
            self._rotate_left(target._parent)
        else:
            brother._left._color = 'BLACK'
            self._rotate_right(target._parent)

    def rb_delete(self, target):
        self._delete_node(None, self.tree, target)

    def _rotate_left(self, node):
        # Implementation going on... Not sure if needed...
        #
        """This function rotate a tree node from right to left
                x             y
               / \           / \
              t  y    ->    x  t
                / \        / \
               t  t       t  t
        This can be a useful function called when re-balancing the tree.
        """
        if node._right is None:
            return
        else:
            new_head = node._right;
            node._right = new_head._left;
            if new_head._left is not None:
                new_head._left._parent = node;
            new_head._parent = node._parent;
            if node._parent is None:
                self.tree = new_head;  # Not sure how this should go...
            elif node is node._parent._left:
                node._parent._left = new_head;
            else:
                node._parent._right = new_head;
            new_head._left = node;
            node._parent = new_head;

    def _rotate_right(self, node):
        # Implementation going on... Not sure if needed...
        #
        """This function rotate a tree node from left to right
                x             y
               / \           / \
              y  t    ->    t  x
             / \              / \
            t  t             t  t
        This can be a useful function called when re-balancing the tree.
        """
        if node._left is None:
            pass
        else:
            new_head = node._left;
            node._left = new_head._right;
            if new_head._right is not None:
                new_head._right._parent = node;
            new_head._parent = node._parent;
            if node._parent is None:
                self.tree = new_head;  # May need modification
            elif node is node._parent._right:
                node._parent._right = new_head;
            else:
                node._parent._left = new_head;
            new_head._right = node;
            node._parent = new_head

class DEMO_RBTree(BinarySearchTree):
    """
        This Class is designed to show in class how out implementation works.
        We will present log now.
        Hopefully with animation. Working on it right now.
    """
    def _insert_case1(self, node):
        if node._parent is None:
            print "Insertion Case 1(ROOT Node) Activated: set node ", node._data, "'s color to BLACK.";
            node._set_color('BLACK')
        else:
            self._insert_case2(node)

    def _insert_case2(self, node):
        parent_node = node._find_parent()
        if parent_node._color == 'BLACK':
            print "Insertion Case 2 Actiavted: Found that node ", node._data, "'s parent's color is BLACK. Do nothing.";
            return
        else:
            self._insert_case3(node)

    def _insert_case3(self, node):
        parent_node = node._find_parent()
        # The variable names of uncle_node and grandparent_node are different from the previous.
        uncle_node = node._find_uncle()
        grandparent_node = node._find_grandparent()
        if uncle_node._color == 'RED':
            print "Insertion Case 3 Activated: Found that node's uncle's color is RED. Do the following operations: ";
            print "Set node ", node._data, "'s parent's color to BLACK. ", parent_node._data, "'s color is now BLACK. ";
            print "Set node ", node._data, "'s uncle's color to BLACK. ", uncle_node._color, "'s color is now BLACK. ";
            print "Set node ", node._data, "'s grandparent's color to RED ", grandparent_node._color, "'s color is now RED. ";
            parent_node._color = 'BLACK'
            uncle_node._color = 'BLACK'
            grandparent_node._color = 'RED'
            self._insert_case1(grandparent_node)
        else:
            self._insert_case4(node)

    def _insert_case4(self, node):
        parent_node = node._find_parent()
        grandparent_node = node._find_grandparent()
        if node == parent_node._right and parent_node == grandparent_node._left:
            print "Insertion Case 4 Activated: Perform LEFT rotation with pivot node ", parent_node._data;
            print "Swithing focus to left child after LEFT rotation, now looking at node ", node._left._data;
            self._rotate_left(parent_node)
            node = node._left
        elif node == parent_node._left and parent_node == grandparent_node._right:
            print "Insertion Case 4 Activated: Perform RIGHT rotation with pivot node ", parent_node._data;
            print "Swithing focus to left child after RIGHT rotation, now looking at node ", node._right._data;
            self._rotate_right(parent_node)
            node = node._right
        self._insert_case5(node)

    def _insert_case5(self, node):
        # Switch the color of current node and its parent
        parent_node = node._find_parent()
        grandparent_node = node._find_grandparent()
        parent_node._color = 'BLACK'
        grandparent_node._color = 'RED'
        print "Insertion Case 5 Activated: Switch the color of current focus node ", node._data, " with node ", parent_node._data;
        if node == parent_node._left:
            print "Perform LEFT rotation with pivot node ", grandparent_node._data, "\n.";
            self._rotate_right(grandparent_node)
        else:
            print "Perform RIGHT rotation with pivot node ", grandparent_node._data, "\n.";
            self._rotate_left(grandparent_node)

    def rb_insert(self, target):
        """
        Convert the target to a tree node, the original color is red.
        Add it to the BinarySearchTree object.
        """
        print "-----------------------------------Inserting Node ", target, "---------------------------------------"
        # node = TreeNode(target)
        self.insert(target)
        root = self.tree
        node = self._find_node(root, target)
        # Balance the tree.
        self._insert_case1(node);
        print "----------------------------------------Finish Insertion----------------------------------------\n \n"

    def _rotate_left(self, node):
        # Implementation going on... Not sure if needed...
        #
        """This function rotate a tree node from right to left
                x             y
               / \           / \
              t  y    ->    x  t
                / \        / \
               t  t       t  t
        This can be a useful function called when re-balancing the tree.
        """
        if node._right is None:
            return
        else:
            new_head = node._right;
            node._right = new_head._left;
            if new_head._left is not None:
                new_head._left._parent = node;
            new_head._parent = node._parent;
            if node._parent is None:
                self.tree = new_head;  # Not sure how this should go...
            elif node is node._parent._left:
                node._parent._left = new_head;
            else:
                node._parent._right = new_head;
            new_head._left = node;
            node._parent = new_head;

    def _rotate_right(self, node):
        # Implementation going on... Not sure if needed...
        #
        """This function rotate a tree node from left to right
                x             y
               / \           / \
              y  t    ->    t  x
             / \              / \
            t  t             t  t
        This can be a useful function called when re-balancing the tree.
        """
        if node._left is None:
            pass
        else:
            new_head = node._left;
            node._left = new_head._right;
            if new_head._right is not None:
                new_head._right._parent = node;
            new_head._parent = node._parent;
            if node._parent is None:
                self.tree = new_head;  # May need modification
            elif node is node._parent._right:
                node._parent._right = new_head;
            else:
                node._parent._left = new_head;
            new_head._right = node;
            node._parent = new_head

peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy', 'Tom'];
bst1 = BinarySearchTree()
for p in peopleB:
    bst1.insert(p);
plot_tree(bst1.tree)

rbt1 = RBTree();
for p in peopleB:
    rbt1.rb_insert(p);
plot_tree(rbt1.tree)

peopleA = ['Alice', 'Bob', 'Carol', 'Doug', 'Site', 'Jobs', 'Mac', 'Kathy', 'UNIX', 'Tom'];
bst2 = BinarySearchTree()
for p in peopleA:
    bst2.insert(p);
plot_tree(bst2.tree)

rbt2 = RBTree();
for p in peopleA:
    rbt2.rb_insert(p);
plot_tree(rbt2.tree)




class TestRBTree(unittest.TestCase):
    """
        Test Data
        NameA : ['Alice','Bob','Carol','Doug','Site','Jobs','Mac','Kathy','UNIX','Tom']
        NameB : ['Carol','Jobs','Alice','UNIX','Bob','Site','Mac','Doug','Kathy','Tom']
    """

    def property_test(self, tree):
        """
            The input of this function must be the tree root.
            This function test the properties of a red black tree. It can be used
            for testing to indicate that no propoerty is violated in the red black tree
            self-balancing procedures.
            Property 1: The root node is black;
            Property 2: Every node is either red or black;
            Property 3: If a node is red, then both its children are black;
            Property 4: For each node, all path from the node to descendant leaves contain
                        the same number of black nodes - All path from the node have the
                        same black height
        """
        # Test Property 1
        # assert (testTree.tree._color is "BLACK")
        # Test Property 2
        # Test Property 3
        # Test Property 4
        pass

    def test_bst_insert_nameA(self):
        peopleA = ['Alice', 'Bob', 'Carol', 'Doug', 'Site', 'Jobs', 'Mac', 'Kathy', 'UNIX', 'Tom']
        bst1 = BinarySearchTree()
        for p in peopleA:
            bst1.insert(p)
        assert isinstance(bst1.tree, object)
        TestNode = bst1.tree
        assert (TestNode._data == 'Alice')
        TestNode = bst1.tree._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Bob')
        TestNode = bst1.tree._right._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Carol')
        TestNode = bst1.tree._right._right._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Doug')
        TestNode = bst1.tree._right._right._right._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Site')
        TestNode = bst1.tree._right._right._right._right._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Jobs')
        TestNode = bst1.tree._right._right._right._right._left._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Mac')
        TestNode = bst1.tree._right._right._right._right._left._right._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Kathy')
        TestNode = bst1.tree._right._right._right._right._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'UNIX')
        TestNode = bst1.tree._right._right._right._right._right._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Tom')

    def test_bst_insert_nameB(self):
        peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy', 'Tom']
        bst2 = BinarySearchTree()
        for p in peopleB:
            bst2.insert(p)
        TestNode = bst2.tree
        assert isinstance(bst2.tree._left, object)
        assert (TestNode._data == 'Carol')
        assert (TestNode._parent is None)
        TestNode = bst2.tree._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Alice')
        assert (TestNode._parent._data == 'Carol')
        assert (TestNode._left._data is None)
        TestNode = bst2.tree._left._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Bob')
        assert (TestNode._parent._data == 'Alice')
        TestNode = bst2.tree._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Jobs')
        assert (TestNode._parent._data == 'Carol')
        TestNode = bst2.tree._right._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Doug')
        assert (TestNode._parent._data == 'Jobs')
        assert (TestNode._left._data is None)
        assert (TestNode._right._data is None)
        TestNode = bst2.tree._right._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'UNIX')
        assert (TestNode._parent._data == 'Jobs')
        assert (TestNode._right._data is None)
        TestNode = bst2.tree._right._right._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Site')
        assert (TestNode._parent._data == 'UNIX')
        assert (TestNode._right._data == 'Tom')
        assert (TestNode._left._data == 'Mac')
        TestNode = bst2.tree._right._right._left._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Mac')
        assert (TestNode._parent._data == 'Site')
        assert (TestNode._right._data is None)
        assert (TestNode._left._data == 'Kathy')
        TestNode = bst2.tree._right._right._left._right
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Tom')
        assert (TestNode._parent._data == 'Site')
        assert (TestNode._right._data is None)
        assert (TestNode._left._data is None)
        TestNode = bst2.tree._right._right._left._left._left
        assert isinstance(TestNode, object)
        assert (TestNode._data == 'Kathy')
        assert (TestNode._parent._data == 'Mac')
        assert (TestNode._right._data is None)
        assert (TestNode._left._data is None)

    def test_rbt_insert_nameA(self):
        """
            rbTree initial test. No deletion.
            solid results obtained from https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
            Results looks like:
                                                Doug
                                               /    \
                                          Bob(R)    Mac(R)
                                          /  \      /    \
                                      Alice Carol  Mac   Tom
                                                    \   /   \
                                                 Kathy Site UNIX   #This line is all red.
        """
        peopleA = ['Alice', 'Bob', 'Carol', 'Doug', 'Site', 'Jobs', 'Mac', 'Kathy', 'UNIX', 'Tom']
        rbt1 = RBTree()
        for p in peopleA:
            rbt1.rb_insert(p)
        # plot_tree(rbt1.tree)
        # Root Test
        TestNode = rbt1.tree
        assert (TestNode._data == 'Doug');
        assert (TestNode._parent is None);
        assert (TestNode._color == 'BLACK');
        # Tree Test
        TestNode = rbt1.tree._left
        assert (TestNode._data == 'Bob');
        assert (TestNode._parent._data == 'Doug');
        assert (TestNode._color == 'RED');
        TestNode = rbt1.tree._left._left
        assert (TestNode._data == 'Alice');
        assert (TestNode._parent._data == 'Bob');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == None);
        TestNode = rbt1.tree._left._right
        assert (TestNode._data == 'Carol');
        assert (TestNode._parent._data == 'Bob');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == None);
        TestNode = rbt1.tree._right
        assert (TestNode._data == 'Mac');
        assert (TestNode._parent._data == 'Doug');
        assert (TestNode._color == 'RED');
        TestNode = rbt1.tree._right._left
        assert (TestNode._data == 'Jobs');
        assert (TestNode._parent._data == 'Mac');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == "Kathy")
        TestNode = rbt1.tree._right._left._right
        assert (TestNode._data == 'Kathy');
        assert (TestNode._parent._data == 'Jobs');
        assert (TestNode._color == 'RED');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == None);
        TestNode = rbt1.tree._right._right
        assert (TestNode._data == 'Tom');
        assert (TestNode._parent._data == 'Mac');
        assert (TestNode._color == 'BLACK');
        TestNode = rbt1.tree._right._right._left
        assert (TestNode._data == 'Site');
        assert (TestNode._parent._data == 'Tom');
        assert (TestNode._color == 'RED');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == None);
        TestNode = rbt1.tree._right._right._right
        assert (TestNode._data == 'UNIX');
        assert (TestNode._parent._data == 'Tom');
        assert (TestNode._color == 'RED');
        assert (TestNode._left._data == None);
        assert (TestNode._right._data == None);
        pass

    def test_rbt_insert_nameB(self):
        """
            rbTree initial test. No deletion.
            solid results obtained from https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
            Results looks like:
                                                Jobs
                                               /    \
                                           Carol(R) Site(R)
                                          /    \   /    \
                                      Alice  Doug Mac   UNIX
                                          \       /     /
                                         Bob(R) Kathy(R)Tom(R)
        """
        peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy', 'Tom']
        rbt1 = RBTree()
        for p in peopleB:
            rbt1.rb_insert(p)
        #plot_tree(rbt1.tree)
        # Root Test
        TestNode = rbt1.tree
        assert (TestNode._data == 'Jobs');
        assert (TestNode._parent is None);
        assert (TestNode._color == 'BLACK');
        # Tree Test: Node Carol
        TestNode = rbt1.tree._left
        assert (TestNode._data == 'Carol');
        assert (TestNode._parent._data == 'Jobs');
        assert (TestNode._color == 'RED');
        # Tree Test: Node Alice
        TestNode = rbt1.tree._left._left
        assert (TestNode._data == 'Alice');
        assert (TestNode._parent._data == 'Carol');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._left._data is None);
        # Tree Test: Node Bob
        TestNode = rbt1.tree._left._left._right
        assert (TestNode._data == 'Bob');
        assert (TestNode._parent._data == 'Alice');
        assert (TestNode._color == 'RED');
        assert (TestNode._right._data is None);
        assert (TestNode._left._data is None);
        # Tree Test: Node Doug
        TestNode = rbt1.tree._left._right
        assert (TestNode._data == 'Doug');
        assert (TestNode._parent._data == 'Carol');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._right._data is None);
        assert (TestNode._left._data is None);
        # Tree Test: Node Site
        TestNode = rbt1.tree._right
        assert (TestNode._data == 'Site');
        assert (TestNode._parent._data == 'Jobs');
        assert (TestNode._color == 'RED');
        # Tree Test: Node Mac
        TestNode = rbt1.tree._right._left
        assert (TestNode._data == 'Mac');
        assert (TestNode._parent._data == 'Site');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._right._data is None);
        # Tree Test: Node Kathy
        TestNode = rbt1.tree._right._left._left
        assert (TestNode._data == 'Kathy');
        assert (TestNode._parent._data == 'Mac');
        assert (TestNode._color == 'RED');
        assert (TestNode._left._data is None);
        assert (TestNode._right._data is None);
        # Tree Test: Node UNIX
        TestNode = rbt1.tree._right._right
        assert (TestNode._data == 'UNIX');
        assert (TestNode._parent._data == 'Site');
        assert (TestNode._color == 'BLACK');
        assert (TestNode._right._data is None);
        # Tree Test: Node Tom
        TestNode = rbt1.tree._right._right._left
        assert (TestNode._data == 'Tom');
        assert (TestNode._parent._data == 'UNIX');
        assert (TestNode._color == 'RED');
        assert (TestNode._left._data is None);
        assert (TestNode._right._data is None);

# people3 = ['Doug','Bob','Alice','Kathy','Tom','Carol']
# bst3 = RBTree()
# for p in people3:
# 	bst3.rb_insert(p)
# print bst3.tree.traverse_infix()
# plot_tree(bst3.tree)
# bst3.rb_delete('Kathy')

# print bst3.tree.traverse_infix()
# plot_tree(bst3.tree)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRBTree)
unittest.TextTestRunner(verbosity=1).run(suite)
