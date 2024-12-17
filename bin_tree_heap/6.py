def heapify(arr, size, root):

    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2


    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child


    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child


    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, size, largest)

def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


numbers = list(map(int, input().split()))


heap_sort(numbers)


print(" ".join(map(str, numbers)))
