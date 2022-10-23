import heapq


def kth_largest(input_array, k):
    # python heap is minheap
    heap = []
    for e in input_array:
        if len(heap) > k:
            heapq.heappop(heap)
        heapq.heappush(heap, e)

    if k == len(input_array):
        return heapq.heappop(heap)
    heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    input_array = [1, 5, 3, 7, 4]
    for k in range(len(input_array)):
        print(k + 1, kth_largest(input_array, k + 1))
