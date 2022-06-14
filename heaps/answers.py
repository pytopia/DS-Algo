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


#Question 2
def smallest(stones):
    stones = [-s for s in stones] #make Max Heap
    heapq.heapify(stones) #making a heap outof stones

    while len(stones) > 1: #as long as we have stones
        first =  heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0) #append the first - second value to the stones
    return abs(stones[0])


#Qestion 3
def closestPoint(points, k):
    pts = [] #create a minHeap
    for x, y in points: #calculate the distance from origin [0,0]
        dist = (abs(x-0)**2) + (abs(y - 0)**2)
        pts.append([dist, x, y])

    res = []
    heapq.heapify(pts)
    for i in range(k):
        dist, x, y = heapq.heappop(pts) #pop from the heap in increasing order cuz its a meanHeap
    res.append([x,y]) #to get the point as requested in the question
    return res