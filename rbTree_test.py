import unittest, sys;
import rbTree_main;

def treverse_property_test(node, color_counter=0, total_black=1):
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
        assert (node._color is 'BLACK' or node._color is 'RED')
        if node._color is 'RED':
            assert(node._left._color is 'BLACK');
            assert(node._right._color is 'BLACK');
        if node._left._data is None and node._right._data is None:
            assert (color_counter == total_black)
        if node._left._data is not None:
            if node._left._color is 'BLACK':
                color_counter += 1;
            treverse_property_test(node._left,color_counter,total_black);
            if node._left._color is 'BLACK':
                color_counter -= 1;
        if node._right._data is not None:
            if node._right._color is 'BLACK':
                color_counter += 1;
            treverse_property_test(node._right,color_counter,total_black);
            if node._right._color is 'BLACK':
                color_counter -= 1;
        return

#The following is the test target
class TestRBTree(unittest.TestCase):
    """
        Test Data
        NameA : ['Alice','Bob','Carol','Doug','Site','Jobs','Mac','Kathy','UNIX','Tom']
        NameB : ['Carol','Jobs','Alice','UNIX','Bob','Site','Mac','Doug','Kathy','Tom']
    """

    def property_test(self):
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
        # Test Property 1: The root node is black
        test_package = [4,5,3,2,7,9,9,10,15];
        rbt_test = rbTree_main.RBTree();
        for p in test_package:
            rbt_test.rb_insert(p);
        assert (rbt_test.tree._color is "BLACK")
        start_node = rbt_test.tree;
        count_black = 1;
        while start_node._left._data is not None:
            start_node = start_node._left;
            if start_node._color is 'BLACK':
                count_black += 1;
        treverse_property_test(rbt_test.tree, 1, count_black)
        pass

    def test_root_insert_delete(self):
        bst_test = rbTree_main.RBTree();
        bst_test.rb_insert(5);
        assert (bst_test.tree._data == 5);
        bst_test.rb_delete(5);
        assert (bst_test.tree._data is None);
        pass

    def test_bst_insert_nameA(self):
        peopleA = ['Alice', 'Bob', 'Carol', 'Doug', 'Site', 'Jobs', 'Mac', 'Kathy', 'UNIX', 'Tom']
        bst1 = rbTree_main.BinarySearchTree()
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
        bst2 = rbTree_main.BinarySearchTree()
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
        rbt1 = rbTree_main.RBTree()
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
        rbt1 = rbTree_main.RBTree()
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

suite = unittest.TestLoader().loadTestsFromTestCase(TestRBTree)
unittest.TextTestRunner(verbosity=1).run(suite)