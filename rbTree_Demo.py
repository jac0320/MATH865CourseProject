import rbTree_main
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt;
from pylab import rcParams;


def plot_node(node, level=1, posx=0, posy=0):
    """Graphical Representation of the tree. Perform a DFS travel"""
    width = 1000.0 * (0.5 ** (level))
    if node._color == 'RED':
        plt.text(posx, posy, str(node._data), horizontalalignment='center', fontsize=12, color='r');
    else:
        plt.text(posx, posy, str(node._data), horizontalalignment='center', fontsize=12);
    if node._left._data is not None:
        px = [posx, posx - width]
        py = [posy - 2, posy - 15]
        plt.plot(px, py, 'b-', hold=True, color='b')
        plot_node(node._left, level + 1, posx - width, posy - 20)
    if node._right._data is not None:
        plot_node(node._right, level + 1, posx + width, posy - 20)
        px = [posx, posx + width]
        py = [posy - 2, posy - 15]
        plt.plot(px, py, 'b-', hold=True, color='b')
    if level == 1 and node._data is not None:
        plt.text(posx, posy, str(node._data), horizontalalignment='center', fontsize=12);
        px = [posx, posx]
        py = [posy - 2, posy - 60]
        plt.plot(px,py,'b-', hold=True, color='b',visible=False)


def plot_tree(node, figsize=(12, 9)):
    """Plot the tree by inputting the root node and figure size."""
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node,1,500)
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()


def plot_two_tree(title,nodeA,nodeB,figsize=(12,9)):
    """Plot two trees side by side to see comparison."""
    rcParams['figure.figsize'] = figsize;
    fig, ax = plt.subplots();
    plt.subplots_adjust(top=0.8,bottom=0.25);
    ax.axis('off');
    plot_node(nodeA,1,0,0);
    plot_node(nodeB,1,2500,0);
    plt.text(1250, 5, str(title), horizontalalignment='center', fontsize=15, color='g');
    plt.show();


def plot_two_tree_insert(figsize=(12,9)):
    """Used to demostrate the insertion opertion and how the trees are rebalance with Red-Black Tree scheme."""
    peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy'];
    rbt = rbTree_main.RBTree();
    for p in peopleB:
        rcParams['figure.figsize'] = figsize;
        fig, ax = plt.subplots()
        plt.subplots_adjust(top=0.83,bottom=0.1);
        ax.axis('off');
        if rbt.tree is not None:
            plot_node(rbt.tree,1,0,0);
        if p is 'Carol':
            plt.plot([0,0],[0,-60],'b-', hold=True, color='b',visible=False)
        rbt.rb_insert(p);
        plot_node(rbt.tree, 1, 2500, 0);
        plt.text(1250, 5, 'Insertion Example: just inserted '+p, horizontalalignment='center', fontsize=15, color='g');
        plt.text(1250, -65, 'Close this window to see next step...', horizontalalignment='center', fontsize=15)
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show();
    pass


plot_two_tree_insert()


def plot_two_tree_delete(figsize=(12,8)):
    """Used to demostrate the deletion opertion and how the trees are rebalance with Red-Black Tree scheme."""
    peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy'];
    rbt = rbTree_main.RBTree();
    for p in peopleB:
        rbt.rb_insert(p);
    for p in peopleB:
        if p is not 'Kathy':
            rcParams['figure.figsize'] = figsize;
            fig, ax = plt.subplots();
            plt.subplots_adjust(top=0.83,bottom=0.1);
            ax.axis('off');
            plot_node(rbt.tree,1,0,0);
            rbt.rb_delete(p);
            plot_node(rbt.tree, 1, 2500, 0);
            plt.text(1250, 5, 'Deletion Example: just deleted '+p, horizontalalignment='center', fontsize=15, color='g');
            plt.text(1250, -65, 'Close this window to see next step...', horizontalalignment='center', fontsize=15);
            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
            plt.show();
    pass


plot_two_tree_delete()



#Comparison 1: We use both Binary Search Tree and Red-Black Tree to indicate how the tree end up differently with the
#               test insertion package peopleB
peopleB = ['Carol', 'Jobs', 'Alice', 'UNIX', 'Bob', 'Site', 'Mac', 'Doug', 'Kathy'];
bst1 = rbTree_main.BinarySearchTree()
for p in peopleB:
    bst1.insert(p);
rbt1 = rbTree_main.RBTree();
for p in peopleB:
    rbt1.rb_insert(p);
plot_two_tree('Comparison 1: Binary Search Tree vs Red Black Tree',bst1.tree,rbt1.tree)


#Comparison 2: We use both Binary Search Tree and Red-Black Tree to indicate how the tree end up differently with the
#               test insertion package peopleA. This time, the package is sorted and it will result in a unbalanced tree
#               when using Binary Search Tree. You can see how Red-Black Tree would rebalance the tree so that the height
#               is modified to a reasonable level.
peopleA = ['Alice', 'Bob', 'Carol', 'Doug', 'Site', 'Jobs', 'Mac', 'Kathy', 'UNIX'];
bst2 = rbTree_main.BinarySearchTree()
for p in peopleA:
    bst2.insert(p);
rbt2 = rbTree_main.RBTree();
for p in peopleA:
    rbt2.rb_insert(p);
plot_two_tree('Comparison 2: Binary Search Tree vs Red Black Tree',bst2.tree,rbt2.tree)

