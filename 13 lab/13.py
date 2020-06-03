# 13. Даний корінь A1 непорожнього дерева. Подвоїти значення кожної вершини дерева.

class Node(object):
    def __init__(self,left = None,right = None,data = None):
        self.left = left
        self.right = right
        self.data = data


def treewidth(tree = None):
    if tree == None:
        return 0
    if tree.data is not None:
      tree.data *= 2
    if tree.right != None:
        treewidth(tree.right)
    if tree.left != None:
        treewidth(tree.left)
    print (tree.data)


# --TEST DATA--
tree1 =  Node(Node(Node(Node(),Node(),3),Node(Node(),Node(),3),2), Node(Node(),Node(),2),1)

print(treewidth(tree1))