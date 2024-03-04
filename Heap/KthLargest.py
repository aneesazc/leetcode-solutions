import heapq  # Import the heapq module for heap operations.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize the KthLargest class with the integer k and the list of numbers nums.
        self.minHeap = nums  # Store the numbers in an internal list, which will be turned into a min-heap.
        self.k = k  # Store the value of k.
        heapq.heapify(self.minHeap)  # Transform the list into a min-heap in-place.
        
        # Ensure the heap only contains the k largest elements by popping the smallest
        # elements until only k remain. This step is crucial to maintain the property of
        # the min-heap where the smallest element of the top k elements is always at the root.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove and return the smallest item from the heap.

    def add(self, val: int) -> int:
        # Add a new value to the heap. This function will be used to add a new number to the data structure
        # while still maintaining the min-heap properties.
        heapq.heappush(self.minHeap, val)  # Add the new value to the heap.
        
        # If adding the new value causes the heap to have more than k elements,
        # remove the smallest one to maintain the size. This ensures the heap
        # always contains the k largest elements of all numbers added so far.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # Remove and return the smallest item from the heap.

        # Return the root of the heap, which is the kth largest element.
        # In a min-heap of the k largest elements, the smallest (root) is the kth largest overall.
        return self.minHeap[0]



class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
