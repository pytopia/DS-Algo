import heapq


#Question 1
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.heap)

    def add(self,val):
        heapq.heappush(self.heap, val)

        if len (self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


