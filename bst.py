class Node:


    def __init__(self,data=None):

        self.data = data

        self.left = None

        self.right = None

class Bst:


    def __init__(self):

        self.root=None

    def insert_node(self,newNode):

        self.root= self.insert(self.root,newNode)

    def insert(self,root,newNode):

        if root is None:
            return newNode

        if newNode.data<root.data:
            root.left= self.insert(root.left,newNode)

        else:
            root.right=self.insert(root.right,newNode)

        return root

    def traverse1(self):

        self.traverse(self.root)
    def traverse(self,root):
        if root is None:
            return
        self.traverse(root.left)
        print(root.data)
        self.traverse(root.right)

    def min(self):
        return self.min_value(self.root)
    def min_value(self,root):
        if root is None:
            return None
        val = self.min_value(root.left)
        if val is None:
            val = root.data
        return val

    def max(self):
        return self.max_value(self.root)
    def max_value(self,root):
        if root is None:
            return None
        val = self.max_value(root.right)
        if val is None:
            val = root.data
        return val

tree = Bst()
for i in range(190,195):
    new_node = Node(i)
    tree.insert_node(new_node)

for i in range(0,10):
    new_node = Node(i)
    tree.insert_node(new_node)

for i in range(5,9):
    new_node =Node(-i)
    tree.insert_node(new_node)

while True:
    x = input("enter another no to test the bst")
    if x == "-1":
        break
    new_node = Node(int(x))
    tree.insert_node(new_node)

max = tree.max()
min = tree.min()
print(str(max)+"  "+str(min))


