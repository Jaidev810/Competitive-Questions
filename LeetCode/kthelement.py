import heapq

def Maxheap(arr, k):

    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        if heap[0] < arr[i]:
            heapq.heapreplace(heap, arr[i])

    heapq.heapify(heap)
    return heap

arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
temp = Maxheap(arr, 4)
print(temp)