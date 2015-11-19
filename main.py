
class rbTreeNode(object):
    """
    #TODO: Description
    """
    def __init__(self,data,left_child=None,right_child=None):
        """Some basic properties that I am thinking of..."""
        self._data = data;
        self._left = left_child;
        self._right = right_child;
        self._color = "r"    #TODO: may need modification
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
        self.parent = parent;

    def _set_left(self,left_child):
        """Update a node's left child with a new tree node."""
        self._left = left_child;

    def _set_right(self,right_child):
        """Update a node's right child with a new tree node."""
        self._right = right_child

    def _set_color(self,color):
        """Set a tree node to a new color"""
        if color == 'red' or color == 'black'
            self._color = color;
        else:
            print "Typo! Typo! Use only 'red' or 'black' for color"

    def _rebalance(self):
        #TODO
        pass


class rbTree(object):
    """
        #TODO:Description
    """
    def __init__(self):
        #TODO
        pass

    def insertion( self, x ) :
        #TODO
        pass

    def deletion (self,x):
        #TODO
        pass

    def depth(self):
        #TODO
        pass

    def is_empty(self):
        #TODO
        pass

    def print_tree(self):
        #TODO
        pass


def randomTest():
    pass

def randomLargeTest():
    pass

