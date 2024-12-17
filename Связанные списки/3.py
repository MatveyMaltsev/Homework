class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def add(self, value, position=None):
        new_node = ListNode(value)
        if position is None:
            self.append(value)
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.value != value:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def to_list(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

    def difference(self):
        if not self.head:
            return []
        last_value = None
        current_node = self.head
        while current_node:
            last_value = current_node.value
            current_node = current_node.next
        differences = []
        current_node = self.head
        while current_node:
            differences.append(current_node.value - last_value)
            current_node = current_node.next
        return differences


linked_list = LinkedList()
elements = list(map(int, input().split()))
for value in elements:
    linked_list.append(value)

print(*linked_list.to_list())

value_to_add = int(input())
position_to_add = int(input())
linked_list.add(value_to_add, position_to_add)
print(*linked_list.to_list())

value_to_delete = int(input())
linked_list.delete_by_value(value_to_delete)
print(*linked_list.to_list())

print(*linked_list.difference())
