# 1. Даний об'єкт A1 типу Node, що має відкриті властивості Data (цілого типу), Left і Right (типу Node).
# Властивості Left і Right цього об'єкта (кореня дерева) містять посилання на ліву і праву дочірні вершини
# (того ж типу Node). Вивести значення властивостей Data кореня,
# його лівої і правої дочірніх вершин, а також посилання на ліву і праву дочірні вершини в зазначеному порядку.
class Node(object):
    def __init__(self,left = None,right = None,data = 0):
        self.left = left
        self.right = right
        self.data = data

def treewidth(tree = None):
    if tree == None:
        return 0
    print(tree.data)
    if tree.right != None:
        treewidth(tree.right)
    if tree.left != None:
        treewidth(tree.left)

A1 =  Node(Node(Node(Node(),Node(),3),Node(Node(),Node(),3),2), Node(Node(),Node(),2),1)

print(treewidth(A1))