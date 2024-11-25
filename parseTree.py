from treeplotter.tree import Node, Tree

root = Node(value=1.0, name=None)
child1 = Node(value=0.5, name=None)
child2 = Node(value=1.0, name=None)
child3 = Node(value=3.0, name="A")
root.children = {child1, child2, child3}

tree = Tree(root=root)

from treeplotter.plotter import create_tree_diagram
create_tree_diagram(tree=tree, save_path="", webshot=True, verbose=True)

# This will display some logs and save an image of the tree to your desired directory.
