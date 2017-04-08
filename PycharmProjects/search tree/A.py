class Node:
    def __init__(self, data):
        # self.parent = None
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self, root=None):
        self.root = root

    # def add(self, data):
    #     prev = None
    #     p = self.root
    #     while p:
    #         prev = p
    #         if p.key < data:
    #             p = p.right
    #         elif p.key > data:
    #             p = p.left
    #         else:
    #             return

    def add(self, data, curr=None):
        if curr is None:
            curr = self.root
        if self.root:
            if curr.data > data:
                next_node = curr.left
                if next_node is None:
                    curr.left = Node(data)
                    return
            elif curr.data < data:
                next_node = curr.right
                if next_node is None:
                    curr.right = Node(data)
                    return
            else:
                return
        else:
            self.root = Node(data)
            return
        self.add(data, next_node)

    def print(self, node='begin'):
        if node == 'begin':
            node = self.root
        if node == None:
            return
        self.print(node.left)
        print(node.data, end=' ')
        self.print(node.right)








