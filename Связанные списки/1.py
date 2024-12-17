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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next
        return False


linked_list = LinkedList()
elements = list(map(int, input().split()))
for element in elements:
    linked_list.append(element)

key = int(input())
if linked_list.search(key):
    print(True)
else:
    print(False)
