def is_min_heap(arr):
    for i in range(len(arr) // 2):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(arr) and arr[i] > arr[left]:
            return 0
        if right < len(arr) and arr[i] > arr[right]:
            return 0
    return 1

arr = list(map(int, input().split()))
print(is_min_heap(arr))
