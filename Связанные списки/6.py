class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top_node = None
        self.stack_size = 0

    def append(self, value):
        new_node = ListNode(value)
        if self.top_node is not None:
            new_node.prev = self.top_node
        self.top_node = new_node
        self.stack_size += 1

    def pop(self):
        if self.top_node is None:
            print("Stack is empty. Cannot pop.")
            return
        self.top_node = self.top_node.prev
        self.stack_size -= 1

    def peek(self):
        if self.top_node is None:
            print("Stack is empty. No top element.")
            return None
        return self.top_node.value

    def size(self):
        return self.stack_size

    def is_empty(self):
        return self.stack_size == 0

    def print_stack(self):
        current = self.top_node
        while current is not None:
            print(current.value, end=" ")
            current = current.prev
        print()

# Пример использования
stack = Stack()
print("Is stack empty?:", stack.is_empty())

# Ввод элементов
elements = list(map(int, input("Введите элементы через пробел: ").split()))
for element in elements:
    stack.append(element)

# Печать стека
print("Содержимое стека:")
stack.print_stack()

# Удаление элемента
stack.pop()
print("Содержимое стека после pop:")
stack.print_stack()

# Текущий верхний элемент
print("Верхний элемент:", stack.peek())
