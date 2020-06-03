# 6. Даний корінь A1 непорожнього дерева. Для кожного з рівнів даного дерева, починаючи з нульового,
# вивести кількість вершин, що знаходяться на цьому рівні. Вважати, що глибина дерева не перевищує 10.

class Node(object):
    def __init__(self, branches = None):
        self.branches = branches
        self.id = 1

def width(tree = None, quantity = 0, subquantity = 0):
    if tree == None:
        return None
    for i in tree.branches:
        quantity += 1
        if i.branches is not None:
            subquantity += width(i)
    print(subquantity)
    return quantity


list1 = [Node([Node(),Node()]),Node([Node(),Node()]),Node([Node(),Node()])]
tree1 = Node(list1)
print(width(tree1))