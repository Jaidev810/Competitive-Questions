import heapq

def kFrequent(arr, k):
    
    n = len(arr)
    freq = list()
    d = dict()

    for i in arr:
        d[i] = d.get(i, 0) + 1

    for i in d:
        freq.append(d[i])

    
    heap = freq[:k]
    heapq.heapify(heap)


    for i in range(k, len(freq)):
        if heap[0] < freq[i]:
            heapq.heapreplace(heap, freq[i])

    li = list()
    key = list(d.keys())
    values = list(d.values())

    for i in range(len(heap)-1, -1, -1):
        temp = heap[i]
        li.append(key[values.index(temp)])
        s = values.index(temp)
        values[s] = 0
    
    return li


arr = [3, 0, 1, 0]
k = 1
li = kFrequent(arr, k)
print(li)