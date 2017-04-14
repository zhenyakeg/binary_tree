class Node:
    def __init__(self, data):
        # self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.count_times = 0


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, data, curr=None):
        if curr is None:
            curr = self.root
        if self.root:
            if curr.data > data:
                next_node = curr.left
                if next_node is None:
                    curr.left = Node(data)
                    curr.left.count_times += 1
                    return
            elif curr.data < data:
                next_node = curr.right
                if next_node is None:
                    curr.right = Node(data)
                    curr.right.count_times += 1
                    return
            else:
                curr.count_times += 1
                return
        else:
            self.root = Node(data)
            self.root.count_times += 1
            return
        self.add(data, next_node)

    def print(self, node='begin'):
        if node == 'begin':
            node = self.root
        if node is None:
            return
        self.print(node.left)
        print(node.data, node.count_times)
        self.print(node.right)

    def find_height(self, curr='START'):
        if curr == 'START':
            curr = self.root
        if curr is None:
            return 0
        return max(self.find_height(curr.left), self.find_height(curr.right)) + 1

    def print_leafs(self, node='begin'):
        if node == 'begin':
            node = self.root
        if node is None:
            return
        parent = node
        node1 = parent.left
        node2 = parent.right
        self.print_leafs(node.left)
        if node1 is None and node2 is None:
            print(node.data, end=' ')
        self.print_leafs(node.right)

    def check_balance(self, node="START"):
        if node == "START":
            node = self.root
        if node is None:
            return True
        if -1 <= self.find_height(node.left) - self.find_height(node.right) <= 1:
            if self.check_balance(node.left) and self.check_balance(node.right):
                return True
        else:
            return False
    def bfs(self, start):
        Q = [start]
        way = []
        while Q:
            curr = Q.pop()
            way.append(curr)
            if curr.left is not None:
                Q.append(curr.left)
            if curr.right is not None:
                Q.append(curr.right)
        return way


def build_tree():
    input_str = input()
    tree = Tree()
    for num in input_str.split():
        tree.add(int(num))
    return tree

tree = build_tree()
tree.print()
