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


#Question 3
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



#Question 4
def Kthlargest(nums, k):

    #Approach 1: MaxHeap ##build maxheap by putting negative sign on num so the the largest number becomes the smallest number and is the first for minsheap. since we want the kth largest so we pop k-1 times and the next pop will return the kth largest
    maxheap = [-num for num in nums]
    heapq.heapify(maxheap)

    for _ in range(k-1):
        heapq.heappop(maxheap)
    return heapq.heappop(maxheap)*-1

     #Approach2: MinHeap
def largest(nums, k):
    minheap = []
        
    for num in nums:
        heapq.heappush(minheap, -num)
        
    for _ in range(k-1):
        heapq.heappop(minheap)
        
    return -minheap[0]

    #Approach 3: MinHeap
def largest(nums, k):
    heapq.heapify(nums)

    while len(nums)>k:
        heapq.heappop(nums)

    return nums[0]



