class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_ancestors(node, target):
    """
    Находит и выводит предков узла с ключом target.
    """
    if not node:
        return False

    if node.key == target:
        return True


    if find_ancestors(node.left, target) or find_ancestors(node.right, target):
        print(node.key)
        return True

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

point = int(input("Введите ключ узла: "))

print(f"Предки для узла {point}:")
if not find_ancestors(root, point):
    print("Узел не найден.")
