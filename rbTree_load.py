import rbTree_main;
import random;
import timeit;

sizes = [1000,2000,4000,8000,16000,32000,64000,128000]

def rbt_insert(sizes):
    tree = rbTree_main.RBTree();
    for i in range(sizes):
        tree.rb_insert(random.random());
    pass

def bst_insert(sizes):
    tree = rbTree_main.BinarySearchTree();
    for i in range(sizes):
        tree.insert(random.random())


def test_treverse(test_tree):
    test_tree.tree.traverse_infix()



for n in sizes:
    print "RBT Insertion Used Time: ", "n=", n, \
        timeit.repeat(stmt="rbt_insert("+str(n)+")", \
                      setup="from rbTree_load import rbt_insert", \
                      repeat=10, \
                      number=1);
    pass
print "\n \n \n"
for n in sizes:
    print "BST Insertion Used Time: ", "n=", n, \
        timeit.repeat(stmt="bst_insert("+str(n)+")", \
                      setup="from rbTree_load import bst_insert", \
                      repeat=10, \
                      number=1);

print "\n \n \n"
for n in sizes:
    print "n is now", n
    rbt_tree = rbTree_main.RBTree();
    bst_tree = rbTree_main.BinarySearchTree();
    for counter in range(10):
        for i in range(n):
            rbt_tree.rb_insert(random.random());
            bst_tree.insert(random.random());
        print rbt_tree.height(rbt_tree.tree), "-", rbt_tree.height(bst_tree.tree)
    print "\n"