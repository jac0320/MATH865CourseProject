import rbTree_main;
import random;
import timeit;

sizes = [1000,2000,4000,8000,16000,32000,64000,128000]

def rbt_insert(sizes):
    """
        Do Random Insertion on a Red-Black Tree with a certain test size. This function is mainly used to
        measure the insertion operation time so as to compare to Binary Search Tree.
    """
    tree = rbTree_main.RBTree();
    for i in range(sizes):
        tree.rb_insert(random.random());
    pass

def bst_insert(sizes):
    """
        Do Random Insertion on a Binary Search Tree with a certain test size. This function is mainly used to
        measure the insertion operation time so as to compare to Red-Black Tree.
    """
    tree = rbTree_main.BinarySearchTree();
    for i in range(sizes):
        tree.insert(random.random())

# The following loops are used to measure the insertion operation time with different sizes of random instances
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

# The following loops are used to detect difference in heights with the same input for both Binary Search Tree and Red-Black Tree.
for n in sizes:
    print "n is now", n
    rbt_tree = rbTree_main.RBTree();
    bst_tree = rbTree_main.BinarySearchTree();
    for counter in range(10):
        for i in range(n):
            target = random.random();
            rbt_tree.rb_insert(target);
            bst_tree.insert(target);
        print rbt_tree.height(rbt_tree.tree), "-", rbt_tree.height(bst_tree.tree)
    print "\n"