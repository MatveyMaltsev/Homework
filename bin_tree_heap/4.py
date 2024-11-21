class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def mirror_tree(node):
    if not node:
        return
    node.left, node.right = node.right, node.left

    mirror_tree(node.left)
    mirror_tree(node.right)

