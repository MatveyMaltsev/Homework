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
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def print_reverse(self):
        if not self.head:
            print("Empty list")
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.prev

        print(" ".join(map(str, values)))


values = list(map(int, input().split()))
dll = DoublyLinkedList()

for value in values:
    dll.append(value)

dll.print_reverse()
