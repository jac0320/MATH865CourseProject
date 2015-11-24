import rbTree_main

people3 = ['Doug','Bob','Alice','Kathy','Tom','Carol']
bst3 = rbTree_main.RBTree()
for p in people3:
	bst3.rb_insert(p)
	
print bst3.tree.traverse_infix()
rbTree_main.plot_tree(bst3.tree)
bst3.rb_delete('Kathy')

print bst3.tree.traverse_infix()
rbTree_main.plot_tree(bst3.tree)
