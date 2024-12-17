class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add(self, value, position=None):
        new_node = ListNode(value)
        if position is None:
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        else:
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for _ in range(position - 1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def delete_by_value(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def calculate_differences(self):
        if not self.head:
            return []
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        n = len(values)
        differences = []
        for i in range(n // 2):
            differences.append(values[i] - values[n - i - 1])
        return differences

# Пример использования
linked_list = DoublyLinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Список:", linked_list.to_list())

linked_list.add(10, 1)
print("Список после добавления 10 на позицию 1:", linked_list.to_list())

linked_list.delete_by_value(2)
print("Список после удаления элемента со значением 2:", linked_list.to_list())

print("Разности пар:", linked_list.calculate_differences())
