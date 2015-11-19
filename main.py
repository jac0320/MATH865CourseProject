
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
            if self._parent == None:
                return None
            else:
                parent_node = self._parent
                return parent_node._parent # Node Sure about this

        def _find_uncle(self):
            """Find the uncle of a tree node, namely it's grandparent's other child.
                If parent is None or no grandparent, return None."""
            if self._parent == None or self._find_grandparent() == None:
                return None
            else:
                grandpa = self._find_grandparent(self);
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
        #TODO:Description
    """
    def __init__(self):
        """"""

    def insert(self,target):
        if self.tree == None:
            self.tree = TreeNode(target)
        else:
            #TODO
        pass

    def delet(self,x):
        pass


