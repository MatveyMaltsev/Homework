class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right or left.key != right.key:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)

# Пример дерева
root = Node(10,
            left=Node(5, Node(1), Node(15)),
            right=Node(5, Node(15), Node(1)))

print("yes" if is_symmetric(root) else "no")
