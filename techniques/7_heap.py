import heapq

def heap_example(nums, k):
    # Crear min-heap
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Mantener tamaño k
    
    return min_heap[0]  # K-ésimo elemento más grande

# Ejemplo: Kth Largest Element (LeetCode 215)