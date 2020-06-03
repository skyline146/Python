# 12. Даниц корінь A1 непорожнього дерева. Створити копію даного дерева і вивести посилання A2 на корінь створеної копії.

class Node(object):
    def __init__(self,left = None,right = None):
        self.left = left
        self.right = right
    def setleft(self,left):
        self.left = left
    def setright(self,right):
        self.right = right

def treewidth(tree = None,tree2 = None):
    if tree == None:
        return tree2
    if tree.right != None:
        tree2.setright(treewidth(tree.right,Node()))
    if tree.left != None:
        tree2.setleft(treewidth(tree.left,Node()))
    return tree2

tree1 =  Node(Node(Node(),Node()), Node(Node(),Node()))
tree2 = Node()

print(treewidth(tree1, tree2))